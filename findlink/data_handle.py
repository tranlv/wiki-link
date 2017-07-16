import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from requests import get, HTTPError
from bs4 import BeautifulSoup
from database import Page, Link

# global variable to store pages that already existed in database to avoid checking duplication
existed_url = set()
engine = create_engine('sqlite:///:memory', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class DataHandle:

	def __init__(self):
		return

	def retrieve_data(self, ending_url, number_of_separation):
		global existed_url

		from_page_id_list = session.query(Link.from_page_id).filter(
								Link.number_of_separation == number_of_separation - 1, Link.to_page_id == ending_url).all()

		for url_id in from_page_id_list:
			url = session.query(Page.url).filter(Page.id == url_id).all()

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

				# only insert link starting with /wiki/
				inserted_url = link.attrs['href']

				if inserted_url not in existed_url:
					# update page table
					self.update_page_if_not_exists(inserted_url)

				# update links table
				inserted_id = session.query(Page.id).filter(Page.url == inserted_url).first()
				self.update_link(int(url_id[0]), int(inserted_id[0]), number_of_separation)

				if inserted_url is ending_url:
					return True
		return False

	@staticmethod
	def update_page_if_not_exists(url):
		global existed_url
		page_list = session.query(Page).filter(Page.url == url).all()
		if page_list.len() == 0:
			existed_url.add(url)
			page = Page(url=url)
			session.add(page)
			session.commit()

	@staticmethod
	def update_link(from_page_id, to_page_id, separation):
		link_between_2_pages = session.query(Link).\
										filter(Link.from_page_id == from_page_id, Link.to_page_id == to_page_id).all()
		if link_between_2_pages.len() == 0:
			link = Link(from_page_id=Link.from_page_id,  to_page_id=to_page_id, no_of_separation=separation)
			session.add(link)
			session.commit()

