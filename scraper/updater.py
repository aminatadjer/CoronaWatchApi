from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import youtubeScraper


def start():
    youtubeScraper.scrap_youtube_videos()
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtubeScraper.scrap_youtube_videos,
                      'interval', minutes=1)
    scheduler.start()
