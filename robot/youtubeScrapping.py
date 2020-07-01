from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from random import sample
from robot.models import VideoYoutube
import requests


def remove_old_videos():
    print("[*] Remove old videos...")
    videos = VideoYoutube.objects.all()
    for video in videos:
        video.delete()


def scrap_youtube_videos():
    print("[*] Refresh database with new videos...")
    api_key = 'AIzaSyBbN9W5cMiRHuwj7--AnUZZVEJ8Kl3lrRk'
    query = "covid19"
    max_results = 50
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&type=video&maxResults={max_results}"
    )
    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        video = VideoYoutube(
            url=f"http://www.youtube.com/embed/{item.get('id').get('videoId')}",

            titre=item.get("snippet").get("title"),
            description=item.get("snippet").get("description"),

        )
        video.save()


def main():

    scrap_youtube_videos()


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(main, 'interval', hours=0.001)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler error.")
