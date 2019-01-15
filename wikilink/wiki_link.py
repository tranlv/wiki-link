from re import compile
from requests import get, HTTPError
from bs4 import BeautifulSoup
from db import db, 

class WikiLink:

	def setup_db(self, db, name, password, ip="127.0.0.1", port):
		"""Setting up database
		Args:
			db(str): Database engine, currently support "mysql" and "postgresql"
			name(str): database username
			password(str): database password
			ip(str, optional): IP address of database. Default to "127.0.0.1"
			port(str): port that databse is running on

		Returns: 
			None
		"""
		
		self.db = db(db, name, password, ip, port)

	def min_link(self, starting_url, ending_url, limit=6):
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

		self.limit = limit
		self.starting_url = starting_url.split("/wiki/")[-1]
		self.ending_url = ending_url.split("/wiki/")[-1]
		self.found = False
		self.number_of_separation = 0

		# update page for both starting and ending url
		self.update_page_if_not_exists(self.starting_url)
		self.update_page_if_not_exists(self.ending_url)

		self.starting_id = self.db.session.query(Page.id).filter(Page.url == self.starting_url).all()[0][0]
		self.ending_id = self.db.session.query(Page.id).filter(Page.url == self.ending_url).all()[0][0]

		separation = self.db.session.query(Link.number_of_separation).filter(Link.from_page_id == self.starting_id, \
																		  Link.to_page_id == self.ending_id).all()

		if str(separation) is not None and len(separation) != 0:
			self.number_of_separation = separation[0][0]
			self.found = True

		while self.found is False:
			self.found = self.retrieve_data(self.starting_id, self.ending_id, 0)

			if self.number_of_separation > self.limit:
				print("No solution within limit! Consider to increase the limit.")
				return
			self.number_of_separation += 1

		if self.number_of_separation  != None:
			return self.number_of_separation 
		else:
			print("There is no path from {} to {}.".format(starting_url, ending_url))
			return 	

	def update_page_if_not_exists(self, url):

		""" insert into table Page if not exist
		Args:
			url(str): wiki url to update

		Returns: 
			None
		"""

		page_list = self.db.session.query(Page).filter(Page.url == url).all()
		if len(page_list) == 0:
			# self.existed_url.add(url)
			page = Page(url=url)
			self.db.session.add(page)
			self.db.session.commit()
			self.update_link(url, url, 0)

	def retrieve_data(self, starting_id, ending_id, number_of_separation):

		""" return true if one of the link within a given number of separation from starting url is ending url
		Args:
			starting_id: the stripped starting url
			ending_id: the stripped ending url
			number_of_separation:
		
		Returns:
			bool:  
		"""

		# query all the page id where from_page_id is the starting url
		# when separation is 0, the starting page retrieve itself
		to_page_id_list = self.db.session.query(Link.to_page_id).filter(Link.number_of_separation == number_of_separation,
																	 Link.from_page_id == starting_id).all()

		for url_id in to_page_id_list:

			# retrieve url from id
			url = self.db.session.query(Page.url).filter(Page.id == url_id[0]).first()

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
			for link in soup.findAll("a", href=compile("(/wiki/)((?!:).)*$")):
				# only insert link starting with /wiki/ and update Page if not exist
				inserted_url = link.attrs['href'].split("/wiki/")[-1]
				self.update_page_if_not_exists(inserted_url)

				# update links table with starting page if it not exists
				inserted_id = self.session.query(Page.id).filter(Page.url == inserted_url).first()[0]
				self.update_link(starting_id, inserted_id, number_of_separation + 1)

				if inserted_id is ending_id:
					return True
		return False

	def update_link(self, from_page_id, to_page_id, no_of_separation):

		""" insert entry into table link if the entry has not existed
		Args:
			from_page_id:
        	to_page_id:
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


	def print_links(self):

		""" print all the links between starting and ending urls with smallest number of links

		Args:
			None

		Returns: 
		"""

		if self.found is False:
			self.search()

		list_of_links = [self.ending_url]

		while self.starting_url not in list_of_links:
			# retrieve entry in Page with current url
			current_url_id = self.db.session.query(Page.id).filter(Page.url == self.ending_url).first()

			# retrieve the the shortest path to the current url using id
			min_separation = self.db.session.query(func.min(Link.number_of_separation)). \
												filter(Link.to_page_id == current_url_id[0])

			# retrieve all the id of pages which has min no of separation to current url
			from_page_id = self.db.session.query(Link.from_page_id).filter(Link.to_page_id == current_url_id[0],
																		Link.number_of_separation == min_separation)

			url = self.db.session.query(Page.url).filter(Page.id == from_page_id[0]).first()
			if url[0] not in list_of_links:
				list_of_links.append(url[0])

		list_of_links.reverse()

		for x in list_of_links:
			print(x)


