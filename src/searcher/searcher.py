from src.settings import session
from src.database.database import Page,Link

class Searcher:

	def __init__(self,starting_page,ending_page):
		self.starting_page=starting_page
		self.ending_page=ending_page
		self.my_list=[]
		
	def	link_search(self,current_page,starting_page):
		""" Updating list
		Parameters
		--------------
		current_page : string, wiki page in the form of '/wiki/something'
		
		starting_page:  string, wiki page in the form of '/wiki/something'

		Returns
		--------------	
		self : object
		  Returns self.
		"""
		
		while starting_page not in self.my_list:
			current_url_id = session.query(Page.id).filter(Page.url==current_page).first()

			min = sesion.query()
			cur.execute("""SELECT from_page_id
						FROM links_from_starting_page
						WHERE to_page_id= %s 
						AND no_of_separation=(SELECT min(no_of_separation) FROM links_from_starting_page
						WHERE to_page_id=%s))
						""" %(current_url_id[0],current_url_id[0]))
			from_page_id = session.query(Link.from_page_id).filter(Link.to_page_id==current_url_id[0])
			cur.execute("""SELECT url FROM pages WHERE id= %s""" %(int(from_page_id[0])))
			url=cur.fetchone()
			if url[0] not in self.my_list:
				self.my_list.append( url[0])	
			self.linkSearch(url[0],starting_page)
			
	def list_of_links(self):
		""" returning list of links, excluding ending_page url
		Parameters
		--------------
		None

		Returns
		--------------	
		List
		
		"""
		
		self.linkSearch(self.ending_page,self.starting_page)
		return self.my_list
	