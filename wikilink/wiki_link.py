#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide Wikilink- Main class of the project"""

# built-in modules
from re import compile
from multiprocessing import Process, Queue, Value
from time import sleep
from queue import Empty
from sys import exit

#third-party modules
from requests import get, HTTPError
from bs4 import BeautifulSoup
from sqlalchemy.exc import DisconnectionError, NoSuchColumnError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

# own modulesf
from wikilink.db.connection import Connection
from wikilink.db.page import Page
from wikilink.db.link import Link

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__credits__ = ["Tranlyvu"]
__license__ = "Apache License 2.0"
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Production"


class WikiLink:
	def __init__(self):
		self.alive = True
		self.visited_set = set()
		pass

	def setup_db(self, db, name, password, ip, port):
		"""Setting up database
		Args:
			db(str): Database engine, currently support "mysql" and "postgresql"
			name(str): database username
			password(str): database password
			ip(str): IP address of database
			port(str): port that databse is running on

		Returns: 
			None
		"""
		
		self.db = Connection(db, name, password, ip, port)

	def min_link(self, source_url, dest_url, limit=6, number_of_processors=1):
		"""return minimum number of link
		Args:
			db(str): Database engine, currently support "mysql" and "postgresql"
			name(str): database username
			password(str): database password
			ip(str, optional): IP address of database. Default to "127.0.0.1"
			port(str): port that databse is running on

		Returns: 
			int: minimum number of sepration between startinga nd ending urls

		Raise:
			queue.Empty
			DisconnectionError
		"""		

		self.source_id = self._insert_url(source_url.split("/wiki/")[-1])
		self.dest_id = self._insert_url(dest_url.split("/wiki/")[-1])

		try:
			separation = self.db.session.query(Link.number_of_separation) \
		                            .filter(Link.from_page_id == self.source_id,
		                            Link.to_page_id == self.dest_id).all()	
		except DisconnectionError:
			print("There is error with DB connection")
			return


		# check if the link already exists
		if str(separation) is not None and len(separation) != 0:
			return separation[0][0]

		self.limit = limit

		execution_queue = Queue()
		storage_queue = Queue() 
		storage_queue.put(self.source_id)
		self.visited_set.add(self.source_id)
		processes = []
		answer = Value("i", 0)

		for _ in range(number_of_processors):
			processes.append(Process(target=self._worker, 
									args=(answer, execution_queue, 
				                          storage_queue)))

		for p in processes:
			p.start()
		

		while True:		
			try: 
				url_id = storage_queue.get(timeout=20.0)	
				execution_queue.put(url_id)
			except Empty:
				for p in processes:
					p.terminate()
				return answer.value if answer.value > 0 else exit(1)
	
				
	def _worker(self, answer, execution_queue, storage_queue):

		while self.alive:
			while execution_queue.empty():
				sleep(0.1)

			url_id = execution_queue.get()
			print(url_id)
			print(self.visited_set)
			try:
				number_of_sep = self.db.session.query(Link.number_of_separation) \
									.filter(Link.from_page_id == self.source_id, 
									        Link.to_page_id == url_id).one()
			except MultipleResultsFound:
				print("Many rows found in DB to find seperation from {} to {}".format(self.source_id,url_id))
				self.alive = False
				sleep(0.1)

			else:
				number_of_sep = number_of_sep[0]		
				if number_of_sep >= self.limit:
					print("No solution within limit! Consider increse the limit")
					self.alive =  False
					sleep(0.1)

				sleep(1)
				neighbors = self._scraper(url_id)

				if len(neighbors) == 0 and number_of_sep <= self.limit:
					print("there is no path from {} to {}".format(starting_url, 
															      ending_url))	
					self.alive = False
					sleep(0.1)
			
				for n in neighbors:
					if n not in self.visited_set:
						self.visited_set.add(n)
						self._insert_link(self.source_id, n, number_of_sep + 1)
						if n == self.dest_id:
							self.alive = False
							answer.value = number_of_sep + 1
							sleep(0.1)
						else:				
							storage_queue.put(n)

				
	def _scraper(self, url_id):

		""" Scrap urls from given url id and insert into database
		
		Args:
			url_id(int): the id of url to be scraped

		Returns:
			list 

		Raises:
        	HTTPError: if An HTTP error occurred

		"""

		# retrieve url from id
		url = self.db.session.query(Page.url).filter(Page.id == url_id).first()

		if url == None:
			return

		# handle exception where page not found or server down or url mistyped
		try:
			response = get('https://en.wikipedia.org/wiki/' + str(url[0]))
			html = response.text
		except HTTPError:
			return
		else:
			if html is None:
				return
			else:
				soup = BeautifulSoup(html, "html.parser")

		# (?!...) : match if ... does not match next
		links = soup.find("div", {"id":"bodyContent"}).findAll("a", 
										    href=compile("(/wiki/)((?!:).)*$"))
		
		new_links_id = []
		for link in links:
			# only insert link starting with /wiki/ and update Page if not exist
			inserted_url = link.attrs['href'].split("/wiki/")[-1]
			inserted_id = self._insert_url(inserted_url)

			new_links_id.append(inserted_id)

			# update links table with starting page if it not exists
			self._insert_link(url_id, inserted_id, 1)
		return new_links_id


	def _insert_url(self, url):

		""" insert into table Page if not exist and return the url id
		Args:
			url(str): wiki url to update

		Returns: 
			int: url id

		Raise:
			DisconnectionError
			NoResultFound
		"""
		try:
			exist = self.db.session.query(Page.id).filter(Page.url == url).one()

		except (NoResultFound, NoSuchColumnError):
			page = Page(url=url)
			self.db.session.add(page)
			self.db.session.commit()

			url_id = self.db.session.query(Page.id).filter(Page.url == url).one()[0]
			self._insert_link(url_id, url_id, 0)
		
		except DisconnectionError:
			print("There is error with DB connection")
			return

		else:
			url_id = exist[0]

		finally: 
			return url_id


	def _insert_link(self, from_page_id, to_page_id, no_of_separation):

		""" insert link into database if link is not existed

		Args:
			from_page_id: id of "from" page
        	to_page_id: id of "to" page
			no_of_separation:
		
		Returns:
			None

		Raise
			NoResultFound
			DisconnectionError
			NoSuchColumnError
		"""
		try:

			exist = self.db.session.query(Link).filter(
								Link.from_page_id==from_page_id,
								Link.to_page_id==to_page_id,
								Link.number_of_separation==no_of_separation)\
									.one()

		except (NoResultFound, NoSuchColumnError):
			link = Link(from_page_id=from_page_id, 
				        to_page_id=to_page_id, 
						number_of_separation=no_of_separation)

			self.db.session.add(link)
			self.db.session.commit()

		except DisconnectionError:
			raise DisconnectionError("There is error with DB connection")

		except MultipleResultsFound:
			print("Many rows found in DB to store link from {} to {} with number of seperation {}".format(from_page_id,
			 											to_page_id, 
			 							 				no_of_separation))