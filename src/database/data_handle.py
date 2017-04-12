from urllib2 import urlopen,HTTPError
from bs4 import	BeautifulSoup
from database import Page, Link
import re
from src.settings import session

#global variable to store pages that already existed in database to avoid checking duplication
existed_url	=	set() 

class DataHandle:
	def __init__(self): return
	
	def	update_pages_table(self,url):
		""" updating page table
		Parameters
		--------------
		url: string, wiki page in the form of '/wiki/something'

		Returns
		--------------	
		None
		
		"""
		
		global existed_url
		page_list = session.query(Page).filter(Page.url==url).all()

		if page_list.len()==0:
			existed_url.add(url)
			page = Page(url = url)
			session.add(link)
			session.commit()
			
	def	update_links_table(self,from_id,to_id,current_separation):
		"""Updating table 'links_from_starting_page' 
		Parameters
		--------------
		from_id: int
		
		to_id: int
		
		current_separation: int
		Returns
		--------------		
		None
		"""

		links_from_starting_page_list = session.query(Link).filter(Link.from_page_id==from_id,
																Link.to_page_id==to_id).all()
		if	links_from_starting_page_list.len() ==0:

			link = Link(from_page_id=from_id,  to_page_id=to_id, no_of_separation=current_separation)
			session.add(link)
			session.commit()
		
	def	retrieve_data(self, url, ending_url, number_of_separation):
		"""Scraping the given url and updating database links found from scraping given url
		   Return True if ending_page found
		
		Parameters
		--------------
		url: string, wiki page in the form of '/wiki/something'
		
		ending_url: string, wiki page in the form of '/wiki/something'
		
		current_separation: int
		Returns
		--------------			
		Boolean
		
		"""
		
		global existed_url
		from_page_id_list = session.query(Link.from_page_id).filter(Link.number_of_separation==number_of_separation-1,
																Link.to_page_id==ending_url).all()
		
		for url_id in from_page_id_list:
			new_url = session.query(Page.url).filter(Page.id == url_id).all()

			#handle exception where page not found or server down or url mistyped
			try:
				html	=	urlopen('https://en.wikipedia.org'+new_url[0])
			except HTTPError:
				return
			else:
				if html is None:
					return
				else:
					soup	=	BeautifulSoup(html)
					
			#update all wiki links with tag 'a' and attribute 'href' start with '/wiki/'
			for	link in	soup.findAll("a",href=re.compile("^(/wiki/)[^:#]")):
				
				#only insert link starting with /wiki/
				inserted_url = link.attrs['href']
				
				if	inserted_url not in	existed_url:
					#update page table 
					self.update_pages_table(inserted_url)
					
				#update links table
				inserted_id= session.query(Page.id).filter(Page.url == inserted_url).first()
				self.update_links_table(int(url_id[0]),int(inserted_id[0]),number_of_separation)

				if inserted_url is ending_url:
					return True
		return False
				
