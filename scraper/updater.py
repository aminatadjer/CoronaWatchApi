from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import youtubeScraper, twitterScrapping, googleSearchScrapping




def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtubeScraper.scrap_youtube_videos,'interval', minutes=2)
    scheduler.add_job(twitterScrapping.getTweets, 'interval', minutes=2, id='twitter_job')
    scheduler.add_job(googleSearchScrapping.scrap, 'interval', minutes=2, id='google_job')
    scheduler.start()

