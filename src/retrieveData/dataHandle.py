"""
	The module retrieve links found from a given wiki page with a certain number of separation and store in mysql database
"""
from urllib2 import urlopen,HTTPError
from bs4 import	BeautifulSoup
from findLink.settings import my_user,my_password,my_host
import MySQLdb
import re

#starting self.connection
conn	=	MySQLdb.connect(host=my_host, user=my_user,passwd=my_password)
cur	=	conn.cursor()
cur.execute(""" show databases like '%s'""" %('findLink'))
if cur.rowcount!=0:
	cur.execute("""USE %s""" %('findLink') )



#global variable to store pages that already existed in database to avoid checking duplication
existed_url	=	set() 

class dataHandle:
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
		cur.execute("""SELECT * FROM pages WHERE url='%s' """ %(url))
		
		if	cur.rowcount==0:
			existed_url.add(url)
			cur.execute("""INSERT INTO pages(url) VALUES('%s')""" %(url) )
			conn.commit()
			
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
		cur.execute("""SELECT * FROM links_from_starting_page
								WHERE from_page_id = %s AND to_page_id = %s""" %(int(from_id),int(to_id)))
		
		if	cur.rowcount ==0:
			cur.execute("""INSERT INTO links_from_starting_page
						(from_page_id, to_page_id,no_of_separation) 
						VALUES (%s, %s,%s)""" %(int(from_id),int(to_id),int(current_separation)))
			
			conn.commit()
		
	def	retrieveData(self,url,ending_url,number_of_separation):
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
		cur.execute("""SELECT from_page_id FROM links_from_starting_page 
					WHERE no_of_separation=%s""" %(number_of_separation-1)) 
		
		for url_id in cur.fetchall():	
			cur.execute("""SELECT url FROM pages WHERE id=%s""" %(int(url_id[0])))
			#handle exception where page not found or server down or url mistyped
			new_url=cur.fetchone()
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
				inserted_url=link.attrs['href']
				
				if	inserted_url not in	existed_url:
					#update page table 
					self.update_pages_table(inserted_url)
					
				#update links table
				cur.execute("""SELECT id FROM pages WHERE url='%s'""" %(inserted_url))
				inserted_id=cur.fetchone()
				self.update_links_table(int(url_id[0]),int(inserted_id[0]),number_of_separation)	

				if inserted_url is ending_url:
					return True
		return False
				
