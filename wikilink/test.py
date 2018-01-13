from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
import re
from requests import get, HTTPError
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
import configparser

Base = declarative_base() #metadata
existed_url = set()

def get_database_url():
    config = configparser.ConfigParser()
    config.read('wiki-link.conf')
    return config.get('database', 'connection')


class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message
        
class DataHandle:
    def __init__(self):
        connection = get_database_url()
        engine = create_engine(connection, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()  # having conversation with database
        return

    def retrieve_data(self, starting_id, ending_id, number_of_separation):
        """ return true if one of the link with a given number of separation from
            starting url is ending url

        :param starting_id:
        :param ending_id:
        :param number_of_separation:
        :return: boolean
        """

        # query all the page id where from_page_id is the starting url
        # when separation is 0, the starting page retrieve itself
        to_page_id_list = self.session.query(Link.from_page_id).filter(
                                          Link.number_of_separation == number_of_separation,
                                          Link.from_page_id == starting_id).all()

        for url_id in to_page_id_list:

            # retrieve url from id
            url = self.session.query(Page.url).filter(Page.id == url_id).all()

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

                # only insert link starting with /wiki/ and update Page if not exist
                inserted_url = link.attrs['href']
                self.update_page_if_not_exists(inserted_url)

                # update links table with starting page if it not exists
                inserted_id = self.session.query(Page.id).filter(Page.url == inserted_url).first()
                self.update_link(starting_id, inserted_id[0], number_of_separation + 1)

                if inserted_id is ending_id:
                    return True
        return False

    def update_page_if_not_exists(self, url):
        """ insert into table Page if not exist

        :param url:
        :return: null
        """

        page_list = self.session.query(Page).filter(Page.url == url).all()
        if page_list.len() == 0:
            existed_url.add(url)
            page = Page(url=url)
            self.session.add(page)
            self.session.commit()


    def update_link(self, from_page_id, to_page_id, no_of_separation):
        """ insert into table Link if link has not existed

        :param from_page_id:
        :param to_page_id:
        :param no_of_separation:
        :return: null
        """

        link_between_2_pages = self.session.query(Link).filter(Link.from_page_id == from_page_id,
                                                          Link.to_page_id == to_page_id).all()
        if link_between_2_pages.len() == 0:
            link = Link(from_page_id=Link.from_page_id,
                        to_page_id=to_page_id,
                        number_of_separation = no_of_separation)
            self.session.add(link)
            self.session.commit()


