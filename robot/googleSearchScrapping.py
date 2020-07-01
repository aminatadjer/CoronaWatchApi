import feedparser
from pprint import pprint
from bs4 import BeautifulSoup

# get the 100 first links in DZ feed and in arabic language
from robot.models import GoogleSearchResult

url = "http://news.google.com/news?q=covid-19&hl=ar-DZ&sort=date&gl=DZ&num=100&output=rss"


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
            searchObj = GoogleSearchResult.objects.create(
                description=description, date=date, titre=titre, url=url)
            searchObj.save()
