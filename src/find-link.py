from retrieveData.data-handle import DataHandle
from settings import my_user, my_password, my_host
from searchEngine.searcher import Searcher
import MySQLdb


class FindLink:
    def __init__(self, starting_url, ending_url, limit=6):
        """ Main class of the application

        Parameters
        --------------
        starting_url: string, wiki page in the form of '/wiki/something'

        ending_url : string, wiki page in the form of '/wiki/something'

        Returns
        --------------
        self : object
           Returns self.
        """

        self.limit = limit
        self.starting_url = starting_url
        self.ending_url = ending_url
        self.create_database(my_user, my_password, my_host)

        # insert starting page into 'pages' table
        self.data = dataHandle()
        self.data.update_pages_table(starting_url)

        # insert link from 'starting_url' to 'starting_url' with 0 number of separation
        self.cur.execute("""SELECT id FROM pages WHERE url='%s' """ % (self.starting_url))
        self.starting_url_id = self.cur.fetchone()
        self.data.update_links_table(self.starting_url_id[0], self.starting_url_id[0], 0)

    def create_database(self, my_user, my_password, my_host):
        """ Generating database 'findLink' with 2 tables 'pages' and 'links'

            Table 'findLink'.'pages'
        +--------+--------------+------+
        | Field  | Type	        | Key  |
        +--------|--------------+------+
        | id	 | int(11)      | pri  |
        | url	 | varchar(255) |      |
        +--------+---------------------+

            Table 'findLink'.'links_from_starting_page'
        +--------------    +--------------+------+
        | Field            | Type	      | Key  |
        +------------------|--------------+------+
        | id	           | int(11)      | pri  |
        | from_page_id     | int(11)      |      |
        | to_page_id       | int(11)      |      |
          no_of_separation | int(11)      |      |
        +--------+-------------------------------+

        """
        # starting self.connection
        self.conn = MySQLdb.connect(host=my_host, user=my_user, passwd=my_password)
        self.cur = self.conn.cursor()

        # creating database and tables
        self.cur.execute("""CREATE DATABASE IF NOT EXISTS %s charset=utf8 """ % ('findLink'))

        self.cur.execute("""USE %s""" % ('findLink'))

        self.cur.execute("""CREATE TABLE IF NOT EXISTS %s(
						%s INT NOT NULL AUTO_INCREMENT,
						%s VARCHAR(255) NOT NULL,
						PRIMARY KEY(%s))
					""" % ('pages', 'id', 'url', 'id')
                         )

        self.cur.execute("""CREATE TABLE IF NOT EXISTS %s (
						%s INT NOT NULL AUTO_INCREMENT,
						%s INT NULL,
						%s INT NULL,
						%s INT NULL,
						PRIMARY KEY(%s) )
					""" % ('links_from_starting_page', 'id', 'from_page_id', 'to_page_id', 'no_of_separation', 'id')
                         )

    def search(self):
        """ return out the smallest number of links between 2 given urls

        Parameters
        --------------

        None

        Returns
        --------------

        None
        """

        self.number_of_separation = 1
        self.found = self.data.retrieveData(self.starting_url, self.ending_url, self.number_of_separation)

        while self.found == False:
            self.number_of_separation += 1
            if self.number_of_separation > self.limit:
                print ("Number of separation is exceeded number of limit. Stop searching!")
                return
            self.found = self.data.retrieveData(self.starting_url, self.ending_url, self.number_of_separation)

        print ("Smallest number of separation is " + str(self.number_of_separation))

    def printLinks(self):
        """ return the links between 2 given urls

        Parameters
        --------------

        None

        Returns
        --------------
        prints links between 2 given urls
        """
        if self.number_of_separation > self.limit or self.found == False:
            print ("No solution within limit!")
            return
        my_search = searcher(self.starting_url, self.ending_url)
        my_list = [self.ending_page] + searcher.list_of_links()
        my_list.reverse()
        for x in my_list:
            print x
