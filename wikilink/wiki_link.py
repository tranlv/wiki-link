#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide Wikilink- Main class of the project"""

# built-in modules
from re import compile
from multiprocessing import Process, Queue, Event, cpu_count, Value
from time import sleep
from queue import Empty
from sys import exit
from collections import deque
from contextlib import contextmanager

# third-party modules
from requests import get, HTTPError
from bs4 import BeautifulSoup
from sqlalchemy.exc import DisconnectionError, NoSuchColumnError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker



# own modules
from .db import Connection
from .db import Page
from .db import Link


__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__credits__ = ["Tranlyvu"]
__license__ = "Apache License 2.0"
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Beta"


class WikiLink:
	def __init__(self):
		pass

	def setup_db(self, db, name, password, ip="127.0.0.1", port=3306):

		""" Setting up database
		Args:
			db(str): Database engine, currently support "mysql" and "postgresql"
			name(str): database username
			password(str): database password
			ip(str): IP address of database (Default = "127.0.0.1")
			port(str): port that databse is running on (default=3306)

		Returns:
			None
		"""

		self.db = Connection(db, name, password, ip, port)


	@contextmanager
	def _session_scope(self):
		"""Provide a transactional scope around a series of operations.

		Args:
			None

		Returns:
			session

		Raises:
			DisconnectionError: error connecting to DB

		"""

		Session = sessionmaker()
		Session.configure(bind=self.db.engine)
		session = Session()

		try:
			yield session
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
			self.db.engine.dispose()


	def min_link(self, source, destination, limit=6, multiprocessing=False):

		""" Return minimum number of link

		Args:
			source(str): source wiki url,
					i.e. "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
			destination(str): Destination wiki url,
					ie. "https://en.wikipedia.org/wiki/Cristiano_Ronaldo"
			limit(int): max number of links from the
					source that will be considered (default=6)
			multiprocessing(boolean): enable/disable
					multiprocessing mode (default=False)

		Returns:
			(int) minimum number of sepration bw source and destination urls
			return None and print messages if exceeding limits or no path found

		Raises:
			DisconnectionError: error connecting to DB
		"""

		if source == destination:
			return 0

		self.source = source
		self.destination = destination
		self.limit = limit

		with self._session_scope() as session:

			try:
				self.source_id = _insert_url(session,
											 source.split("/wiki/")[-1])
				self.dest_id = _insert_url(session,
					                       destination.split("/wiki/")[-1])

				if  session.query(Link.number_of_separation).filter_by(
								from_page_id=self.source_id,
								to_page_id=self.dest_id).scalar() is not None:

					sep = session.query(Link.number_of_separation).filter_by(
								from_page_id=self.source_id,
								to_page_id=self.dest_id).one()[0]
					return sep

			except DisconnectionError:
				print("There is error with DB connection")
				exit(1)

		if multiprocessing:
			return self._multiprocessing_scraper()
		else:
			return self._single_threaded_scraper()
	
	
	def _single_threaded_scraper(self):

		""" Return minimum number of link using single threaded scraper

		Args:
			None

		Returns: 
			(int) minimum number of sepration bw source and destination urls
			return None and print messages if exceeding limits or no path found

		Raises:
			DisconnectionError: error connecting to DB
		"""	

		number_of_separation = 0
		queue = deque()
		queue.appendleft(self.source_id)
		queue.appendleft(None)
		visited_set = set()
		visited_set.add(self.source_id)

		with self._session_scope() as session:

			while number_of_separation <= self.limit and len(queue) > 0:
				number_of_separation += 1		
				url_id = queue.pop()

				if url_id is None:
					if len(queue) > 0:
						queue.appendleft(None)
					elif len(queue) == 0:
						continue

				else:
					
					_scraper(session, url_id)

					try:
						neighbors = session.query(Link).filter(
							Link.from_page_id == url_id,
							Link.number_of_separation == 1).all()

					except DisconnectionError:
						print("There is error with DB connection")
						exit(1)

					for n in neighbors:

						if n.to_page_id not in visited_set:

							visited_set.add(n.to_page_id)
							queue.appendleft(n.to_page_id)

							_insert_link(session, 
										 self.source_id, 
										 url_id,
										 number_of_separation)

						if n.to_page_id == self.dest_id:
							return number_of_separation
				
		if number_of_separation > self.limit:
			print("No solution within limit! Consider to increase the limit.")
		else:
			print("there is no path from {} to {}".format(self.source, 
														  self.destination))
		exit(1)


	def _multiprocessing_scraper(self):

		""" Return minimum number of link using single multiprocessing scraper

		Args:
			None

		Returns: 
			(int) minimum number of sepration bw source and destination urls
			return None and print messages if exceeding limits or no path found

		Raises:
			Empty
		"""	

		execution_queue = Queue()
		storage_queue = Queue() 
		separation_queue = Queue()

		# putting source id first
		storage_queue.put(self.source_id)
		separation_queue.put(0)

		session_factory = sessionmaker(bind=self.db.engine)
		self.DBSession = scoped_session(session_factory)
		
		answer = Value('i', 0)
		event = Event()
		 
		delegator = Process(target=self._delegator, args=(
											execution_queue, 
											storage_queue, 
											separation_queue, 
											event, 
											answer))

		processes = [delegator] 

		for i in range((cpu_count())):
			p = Process(target=self._worker, args=(
											execution_queue, 
											storage_queue, 
											separation_queue, 
											event))

			processes.append(p)
		
		for p in processes:
			p.start()

		while not event.is_set():
			continue

		for p in processes:
			p.terminate()

		self.DBSession.remove()
		self.db.engine.dispose()

		if answer.value > self.limit:
			print("No solution within limit! Consider to increase the limit.")
			exit(1)
		elif answer.value > 0:
			return answer.value


	def _delegator(self, 
		          execution_queue,
		          storage_queue,
		          separation_queue,
		          event,
		          answer):

		""" The function acts as jobs delegator, picking up url_id from 
			storage_queue and put into execution queue

		Args:
			execution_queue: queue that store url_id to scrape
			storage_queue: queue that store url_id after found from scraping
			separation_queue: queue that store number of seperation of 
							url after found from scraping
			event: to signal when scraping is finished
			answer: shared-stated value that store answer

		Returns: 
			None

		Raises:
			Empty: if storage queue have no url for 15 minutes
		"""	


		while not event.is_set():
			while not storage_queue.empty() and not separation_queue.empty():
				try:
					url_id = storage_queue.get(timeout=15.0)
					sep = separation_queue.get(timeout=15.0)

					print("take url_id {} with sep {} out of queues" \
						.format(url_id, sep))
					
					session = self.DBSession()
					_insert_link(session, self.source_id, url_id, sep)

					if url_id == self.dest_id:
						answer.value = sep
						event.set()
						exit(1)

					print("put url_id {} into execution queue".format(url_id))
					execution_queue.put(url_id)
			
				except Empty:
					event.set()
					exit(1)


	def _worker(self, execution_queue, storage_queue, separation_queue, event):
		
		""" The worker function that pick up url_id from
			 execution_queue and scrape

		Args:
			execution_queue: queue that store url_id to scrape
			storage_queue: queue that store url_id after found from scraping
			separation_queue: queue that store number of
							 seperation of url after found from scraping
			event: to signal when scraping is finished

		Returns:
			None

		Raises:
			MultipleResultsFound
			NoResultFound
			NoSuchColumnError
		"""
		
		visited_set = set()

		while not event.is_set():
			while execution_queue.empty():
				sleep(0.1)

			url_id = execution_queue.get()
			visited_set.add(url_id)
			print("take url_id {} out of execution queue".format(url_id))
			sleep(1)
			try:
				session = self.DBSession()
				number_of_sep = session.query(Link.number_of_separation) \
									.filter_by(from_page_id=self.source_id,
									           to_page_id=url_id).first()
			except MultipleResultsFound:
				print("Many rows found in DB to find seperation from {} to {}"
					.format(self.source_id, url_id))
				event.set()
				exit(1)

			except (NoResultFound, NoSuchColumnError):
				print("No result found")
				exit(1)

			else:
				number_of_sep = int(number_of_sep.number_of_separation)
				if number_of_sep >= self.limit:
					print("No solution within limit! Increse the limit")
					event.set()
					exit(1)

				session = self.DBSession()
				neighbors = _scraper(session, url_id)

				if len(neighbors) == 0 and number_of_sep <= self.limit:
					print("there is no path from {} to {}".format(self.source,
												      		self.destination))
					event.set()
					exit(1)

				for n in neighbors:
					if n not in visited_set:
						visited_set.add(n)
						storage_queue.put(n)
						separation_queue.put(number_of_sep + 1)

	def _print_path(self):
		""" 
			Function prints the sequence of paths from source to destination 
			with the shortest number of link.
		Args:
			None
		Returns:
			None
		"""
		dest_node = LinkNode(self.dest_id)

		successful_paths = []

		with self._session_scope() as session:
			def find_route_to_parent(node, source_root_id, depth=0, session=session):
				parents = get_all_my_parents(node.node_id, session)
				parent_ids = get_parent_id_list(parents)
				depth += 1
				if source_root_id in parent_ids and depth < self.limit:
					node.path.append(node.node_id)
					node.path.append(source_root_id) 
					successful_paths.append(node.path)
					return True

				if depth > self.limit:
					return

				for every_parent in parents:
					every_parent.path.extend(node.path)
					every_parent.path.append(node.node_id)
					if find_route_to_parent(every_parent, source_root_id, depth):
						break

			#recursively backtrack from dest id to source id
			find_route_to_parent(dest_node, self.source_id)

			success_path_url = [] #store url paths from page id
			if successful_paths:
				success_path_url = get_url_path_from_page_ids(session,min(successful_paths, key=len))
				print("{}".format("=>".join(success_path_url)))

			return

def _scraper(session, url_id):

	""" Scrap urls from given url id and insert into database

	Args:
		url_id(int): the id of url to be scraped

	Returns:
		list of new url ids

	Raises:
    	HTTPError: if An HTTP error occurred
	"""

	# retrieve url from id

	if session.query(Page.url).filter_by(id=url_id).scalar is None:
		print("There is no url for id {}".format(url_id))
		exit(1)
	else:
		url = session.query(Page.url).filter_by(id=url_id).first()

	if url is None:
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
	links = soup.find("div", {"id": "bodyContent"}).findAll("a",
									    href=compile("(/wiki/)((?!:).)*$"))

	new_links_id = []
	for link in links:
		# only insert link starting with /wiki/ and update Page if not exist
		inserted_url = link.attrs['href'].split("/wiki/")[-1]
		inserted_id = _insert_url(session, inserted_url)

		new_links_id.append(inserted_id)

		# update links table with starting page if it not exists
		_insert_link(session, url_id, inserted_id, 1)

	return new_links_id


def _insert_url(session, url):

	""" insert into table Page if not exist and return the url id
	Args:
		url(str): wiki url to update

	Returns:
		int: url id

	Raise:
		DisconnectionError
		MultipleResultsFound
	"""
	try:

		if session.query(Page.id).filter_by(url=url).scalar() is None:
			page = Page(url=url)
			session.add(page)
			session.commit()
			url_id = session.query(Page).filter_by(url=url).first().id
			_insert_link(session, url_id, url_id, 0)

	except DisconnectionError:
		raise DisconnectionError("There is error with DB connection")

	except MultipleResultsFound:
		raise MultipleResultsFound("Many rows found in DB to find url \
									id of {}".format(url))

	url_id = session.query(Page.id).filter_by(url=url).first()

	return url_id.id


def _insert_link(session, from_page_id, to_page_id, no_of_separation):

	""" insert link into database if link is not existed

	Args:
		from_page_id(int): id of "from" page
    	to_page_id(int): id of "to" page
		no_of_separation(int)

	Returns:
		None

	Raise
		DisconnectionError
		MultipleResultsFound
	"""

	try:

		if session.query(Link).filter_by(
						from_page_id=from_page_id,
						to_page_id=to_page_id,
						number_of_separation=no_of_separation).scalar() is None:

			link = Link(from_page_id=from_page_id,
				        to_page_id=to_page_id, 
						number_of_separation=no_of_separation)

			session.add(link)
			session.commit()

	except DisconnectionError:
		raise DisconnectionError("There is error with DB connection")

	except MultipleResultsFound:
		raise MultipleResultsFound(
			"Many rows found in DB to store link from {} to {}\
			 with number of seperation {}".format(from_page_id, to_page_id,
		 								          no_of_separation))

class LinkNode(object):
    def __init__(self, node_id):
        self.node_id = node_id
        self.path = [] #parent urls

def get_all_my_parents(node_id, session):
    parent_list = []
    for every_parent in session.query(Link).filter(Link.to_page_id==node_id,Link.number_of_separation==1):
        parent_node = LinkNode(every_parent.from_page_id)
        parent_list.append(parent_node)
    return parent_list

def get_parent_id_list(parent_list):
    return [parent_node.node_id for parent_node in parent_list]

def get_url_path_from_page_ids(session, page_ids_list):
    path_url = []
    for page_id in page_ids_list:
        page_url = session.query(Page).filter(Page.id == page_id).first()
        path_url.append(page_url.url)
    path_url.reverse()
    return path_url
