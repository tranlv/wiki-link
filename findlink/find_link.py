from database import database,data_handle
from findlink import searcher
from settings import session

class FindLink:
    def __init__(self, starting_url, ending_url, limit = 6):
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

        page = database.Page(url='starting_url')
        session.add(page)

        page = database.Page(url='ending_url')
        session.add(page)

        link = database.Link(from_page_id='starting_url',
                             to_page_id='starting_url',
                             no_of_separation=0)
        session.add(link)
        session.commit()

    def search(self):
        """ return the smallest number of links between 2 given urls
        Parameters
        --------------
        None

        Returns
        --------------
        None
        """

        self.number_of_separation = 1
        self.found = data_handle.retrieveData(self.starting_url, self.ending_url, self.number_of_separation)

        while self.found == False:
            self.number_of_separation += 1
            if self.number_of_separation > self.limit:
                print ("Number of separation is exceeded number of limit. Stop searching!")
                return
            self.found = self.data.retrieveData(self.starting_url, self.ending_url, self.number_of_separation)

        print ("Smallest number of separation is " + str(self.number_of_separation))

    def print_links(self):
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
