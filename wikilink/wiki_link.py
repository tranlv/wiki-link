from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
import re
from requests import get, HTTPError
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
import os, sys

Base = declarative_base()  # metadata


class Page(Base):
	__tablename__ = 'page'

	id = Column(Integer(), primary_key=True)
	url = Column(String(225))
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Page(page_id = '%s', url ='%s', created='%s')>" % (self.page_id, self.url, self.created)


class Link(Base):
	__tablename__ = 'link'

	id = Column(Integer, primary_key=True)
	from_page_id = Column(Integer, ForeignKey('page.id'))
	to_page_id = Column(Integer, ForeignKey('page.id'))
	number_of_separation = Column(Integer, nullable=False)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
			self.from_page_id, self.to_page_id, self.number_of_separation, self.created)


def get_database_url():
	config = ConfigParser()
	try:
		config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'wiki_link.ini'))
	except Exception as e:
		print(str(e))

	try:
		connection = config.get('database', 'connection')
	except Exception as e:
		print(str(e), 'could not read from configuration file')
		sys.exit()

	return connection


class WikiLink:
	def __init__(self, starting_url, ending_url, limit=6):

		new_db_name = 'wikilink'
		db_conn_format = get_database_url()
		engine = create_engine(db_conn_format, echo=True)
		engine.execute("CREATE DATABASE IF NOT EXISTS %s" % new_db_name)
		wikilink_engine = create_engine(db_conn_format + "/" + new_db_name, echo=True)
		# If table don't exist, Create.
		if not wikilink_engine.dialect.has_table(wikilink_engine, 'link'):
			if not wikilink_engine.dialect.has_table(wikilink_engine, 'page'):
				Base.metadata.create_all(wikilink_engine)

		Session = sessionmaker(wikilink_engine)
		self.session = Session()  # having conversation with database

		self.limit = limit
		self.starting_url = starting_url
		self.ending_url = ending_url
		self.found = False
		self.number_of_separation = 0

		# update page for both starting and ending url
		self.update_page_if_not_exists(starting_url)
		self.update_page_if_not_exists(ending_url)

		# update link for starting_url, no of separation between 1 url to itself is zero of course
		self.starting_id = self.session.query(Page.id).filter(Page.url == starting_url).all()
		self.update_link(self.starting_id[0], self.starting_id[0], 0)

		# update link for ending_url, no of separation between 1 url to itself is zero of course
		self.ending_id = self.session.query(Page.id).filter(Page.url == ending_url).all()
		self.update_link(self.ending_id[0], self.ending_id[0], 0)

	def update_page_if_not_exists(self, url):

		""" insert into table Page if not exist
		:param: url
		:return: null
		"""

		page_list = self.session.query(Page).filter(Page.url == url).all()
		if len(page_list) == 0:
			# self.existed_url.add(url)
			page = Page(url=url)
			self.session.add(page)
			self.session.commit()

	def update_link(self, from_page_id, to_page_id, no_of_separation):

		""" insert entry into table link if the entry has not existed
		:param from_page_id:
        :param to_page_id:
		:param no_of_separation:
		:return: null
		"""

		link_between_2_pages = self.session.query(Link).filter(Link.from_page_id == from_page_id,
															   Link.to_page_id == to_page_id).all()
		if len(link_between_2_pages) == 0:
			link = Link(from_page_id=from_page_id, to_page_id=to_page_id, number_of_separation=no_of_separation)
			self.session.add(link)
			self.session.commit()

	def search(self):

		""" print smallest number of separation
		:return: null
		"""

		separation = self.session.query(self.number_of_separation).filter(Link.from_page_id == self.starting_id,
																		  Link.to_page_id == self.ending_id).first()
		if separation != 0:
			self.number_of_separation = separation
			self.found = True

		while self.found is False:
			self.found = self.retrieve_data(self.starting_url, self.ending_url, self.number_of_separation)
			if self.number_of_separation > self.limit:
				print("No solution within limit! Consider to increase the limit.")
				return
			self.number_of_separation += 1

		return str(self.number_of_separation)

	def retrieve_data(self, starting_id, ending_id, number_of_separation):

		""" return true if one of the link within a given number of separation from starting url is ending url

		:param starting_id:
		:param ending_id:
		:param number_of_separation:
		:return: boolean
		"""

		# query all the page id where from_page_id is the starting url
		# when separation is 0, the starting page retrieve itself
		to_page_id_list = self.session.query(Link.from_page_id).filter(Link.number_of_separation == number_of_separation,
																		Link.from_page_id == starting_id).all()

		for url_id in to_page_id_list:

			# retrieve url from id
			url = self.session.query(Page.url).filter(Page.id == url_id).all()

			# handle exception where page not found or server down or url mistyped
			try:
				html = get('https://en.wikipedia.org' + url[0])
			except HTTPError:
				return
			else:
				if html is None:
					return
				else:
					soup = BeautifulSoup(html)

			# update all wiki links with tag 'a' and attribute 'href' start with '/wiki/'
			for link in soup.findAll("a", href=re.compile("^(/wiki/)[^:#]")):

				# only insert link starting with /wiki/ and update Page if not exist
				inserted_url = link.attrs['href']
				self.update_page_if_not_exists(inserted_url)

				# update links table with starting page if it not exists
				inserted_id = self.session.query(Page.id).filter(Page.url == inserted_url).first()
				self.update_link(starting_id, inserted_id[0], number_of_separation + 1)

				if inserted_id is ending_id:
					return True
		return False

	def print_links(self):

		""" Print all the links between starting and ending urls
		:return: null
		"""

		if self.found is False:
			self.search()

		list_of_links = [self.ending_url]

		while self.starting_url not in list_of_links:
			# retrieve entry in Page with current url
			current_url_id = self.session.query(Page.id).filter(Page.url == self.ending_url).first()

			# retrieve the the shortest path to the current url using id
			min_separation = self.session.query(func.min(Link.number_of_separation)). \
				filter(Link.to_page_id == current_url_id[0])

			# retrieve all the id of pages which has min no of separation to current url
			from_page_id = self.session.query(Link.from_page_id).filter(Link.to_page_id == current_url_id[0],
																		Link.number_of_separation == min_separation)

			#
			url = self.session.query(Page.url).filter(Page.id == from_page_id[0]).first()
			if url[0] not in list_of_links:
				list_of_links.append(url[0])

		list_of_links.reverse()

		for x in list_of_links:
			print(x)


def main():
	starting_url = '/wiki/Barack_Obama'
	ending_url = '/wiki/Bill_Clinton'
	model = WikiLink(starting_url, ending_url)
	print("Smallest number of separation is " + model.search())
	# model.print_links()

if __name__ == "__main__": main()
