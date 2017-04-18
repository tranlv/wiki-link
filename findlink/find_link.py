from database.data_handle import DataHandle
from database.database import Page
from findlink.searcher import Searcher
from settings import session


class FindLink:

    def __init__(self, starting_url, ending_url, limit=6):

        self.limit = limit
        self.starting_url = starting_url
        self.ending_url = ending_url
        self.found = False
        self.number_of_separation = 1

        DataHandle().update_page_if_not_exists(starting_url)
        DataHandle().update_page_if_not_exists(ending_url)

        # update link for starting_page
        starting_id = session.query(Page.id).filter(Page.url == starting_url).all()
        DataHandle.update_link(starting_id[0], starting_id[0], 0)

    def search(self):
        """ return the smallest number of links between 2 given urls
        """

        self.found = DataHandle().retrieve_data(self.ending_url, self.number_of_separation)

        while self.found is False:
            self.number_of_separation += 1
            if self.number_of_separation > self.limit:
                print ("Number of separation is exceeded number of limit. Stop searching!")
                return
            self.found = DataHandle().retrieve_data(self.ending_url, self.number_of_separation)

        print ("Smallest number of separation is " + str(self.number_of_separation))

    def print_links(self):
        """ return the links between 2 given urls
        """

        if self.number_of_separation > self.limit or self.found is False:
            print ("No solution within limit!")
            return
        my_search = Searcher(self.starting_url, self.ending_url)
        my_list = [self.ending_page] + my_search.list_of_links()
        my_list.reverse()

        for x in my_list:
            print x
