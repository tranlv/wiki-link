from findlink.setting import session
from sqlalchemy import func

from findlink.database import Page,Link


class Searcher:

    def __init__(self, starting_page, ending_page):
        self.starting_page = starting_page
        self.ending_page = ending_page
        self.my_list = []

    def link_search(self, current_page, starting_page):

        while starting_page not in self.my_list:
            current_url_id = session.query(Page.id).filter(Page.url == current_page).first()

            min_separation = session.query(func.min(Link.number_of_separation)).filter(Link.to_page_id == current_url_id[0])
            from_page_id = session.query(Link.from_page_id).filter(Link.to_page_id == current_url_id[0], Link.number_of_separation == min_separation)
            url = session.query(Page.url).filter(Page.id == from_page_id[0]).first()
            if url[0] not in self.my_list:
                self.my_list.append( url[0])
            self.linkSearch(url[0],starting_page)

    def list_of_links(self):

        self.linkSearch(self.ending_page,self.starting_page)
        return self.my_list
