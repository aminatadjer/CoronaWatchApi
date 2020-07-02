from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import youtubeScraper


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtubeScraper.scrap_youtube_videos,
                      'interval', hours=20)
    scheduler.start()
