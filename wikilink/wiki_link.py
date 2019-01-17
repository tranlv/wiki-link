from re import compile
from requests import get, HTTPError
from bs4 import BeautifulSoup
from wikilink.db.connection import Connection
from wikilink.db.page import Page
from wikilink.db.link import Link
from sqlalchemy import func

class WikiLink:
	def __init__(self):
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

	def min_link(self, source_url, dest_url, limit=6):
		"""return minimum number of link
		Args:
			db(str): Database engine, currently support "mysql" and "postgresql"
			name(str): database username
			password(str): database password
			ip(str, optional): IP address of database. Default to "127.0.0.1"
			port(str): port that databse is running on

		Returns: 
			int: minimum number of sepration between startinga nd ending urls
		"""		

		# update page for both starting and ending url
		source_id = self.insert_url(source_url.split("/wiki/")[-1])
		dest_id = self.insert_url(dest_url.split("/wiki/")[-1])


		separation = self.db.session.query(Link.number_of_separation).filter(Link.from_page_id == source_id, \
																		  Link.to_page_id == dest_id).all()
		# check if the link already exists
		if str(separation) is not None and len(separation) != 0:
			return separation[0][0]

		number_of_separation = 0
		queue = [source_id]
		already_seen = set(queue)

		while number_of_separation <= limit and len(queue) > 0:
			number_of_separation += 1
			temporary_queue = queue
			queue = []
			# find outbound links from current url
			for url_id in temporary_queue:		
				self.update_url(url_id)

				neighbors = self.db.session.query(Link).filter(Link.from_page_id == url_id, \
											Link.number_of_separation == 1).all()
				for n in neighbors:
					if n.to_page_id == dest_id:
						self.insert_link(source_id, dest_id, number_of_separation)
						return number_of_separation

					if n.to_page_id not in already_seen:
						already_seen.add(n.to_page_id)
						queue.append(n.to_page_id)
			
		if number_of_separation > limit:
			print("No solution within limit! Consider to increase the limit.")
			return
		else:
			print("there is no path from {} to {}".format(starting_url, ending_url))


	def update_url(self, url_id):

		""" Scrap urls from given url id and insert into database
		
		Args:
			starting_id: the stripped starting url
			ending_id: the stripped ending url
			number_of_separation:
		
		Returns:
			None  

		Raises:
        	HTTPError: if An HTTP error occurred

		"""

		# retrieve url from id
		url = self.db.session.query(Page.url).filter(Page.id == url_id).first()

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

		# update all wiki links with tag 'a' and attribute 'href' start with '/wiki/'
		# (?!...) : match if ... does not match next
		links = soup.findAll("a", href=compile("(/wiki/)((?!:).)*$"))
		for link in links:
			# only insert link starting with /wiki/ and update Page if not exist
			inserted_url = link.attrs['href'].split("/wiki/")[-1]
			inserted_id = self.insert_url(inserted_url)

			# update links table with starting page if it not exists
			self.insert_link(url_id, inserted_id, 1)


	def insert_url(self, url):

		""" insert into table Page if not exist and return the url id
		Args:
			url(str): wiki url to update

		Returns: 
			int: url id
		"""

		page_list = self.db.session.query(Page).filter(Page.url == url).all()
		if len(page_list) == 0:
			page = Page(url=url)
			self.db.session.add(page)
			self.db.session.commit()
			url_id = self.db.session.query(Page.id).filter(Page.url == url).all()[0][0]
			self.insert_link(url_id, url_id, 0)
			return url_id
		else:
			return self.db.session.query(Page.id).filter(Page.url == url).all()[0][0]

	def insert_link(self, from_page_id, to_page_id, no_of_separation):

		""" insert link into database if link is not existed

		Args:
			from_page_id: id of "from" page
        	to_page_id: id of "to" page
			no_of_separation:
		
		Returns:
			None
		"""

		link_between_2_pages = self.db.session.query(Link).filter(Link.from_page_id == from_page_id,
															   Link.to_page_id == to_page_id).all()
		if len(link_between_2_pages) == 0:
			link = Link(from_page_id=from_page_id, to_page_id=to_page_id, number_of_separation=no_of_separation)
			self.db.session.add(link)
			self.db.session.commit()