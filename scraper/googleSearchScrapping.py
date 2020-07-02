import feedparser
from pprint import pprint
from bs4 import BeautifulSoup

# get the 100 first links in DZ feed and in arabic language
from robot.models import Veille
from config import GOOGLE_URL




class ParseFeed():

    def __init__(self, url):
        self.feed_url = url

    def clean(self, html):
        '''
        Get the text from html and do some cleaning
        '''
        soup = BeautifulSoup(html)
        text = soup.get_text()
        text = text.replace('\xa0', ' ')
        return text

    def parse(self):
        '''
        Parse the URL, and print all the details of the news
        '''
        feeds = feedparser.parse(self.feed_url).entries
        for f in feeds:

            description = self.clean(f.get("description", ""))
            date = f.get("published", "")
            titre = f.get("title", "")
            url = f.get("link", "")
            if not Veille.objects.filter(url=url).exists():
                searchObj = Veille.objects.create(description=description, date=date, titre=titre, url=url, type="google")
                searchObj.save()


def scrap():
    feed = ParseFeed(GOOGLE_URL)
    feed.parse()