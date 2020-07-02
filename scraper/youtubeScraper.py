
from django.conf import settings
from random import sample
from robot.models import VideoYoutube
import requests
from config import SUBJECT, API_KEY, MAX_RESULTS


def scrap_youtube_videos():
    print("Scrapping")
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={SUBJECT}&key={API_KEY}&type=video&maxResults={MAX_RESULTS}"
    )
    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        if not VideoYoutube.objects.filter(url=f"{item.get('id').get('videoId')}").exists():
            video = VideoYoutube(
                url=f"{item.get('id').get('videoId')}",
                titre=item.get("snippet").get("title"),
                description=item.get("snippet").get("description"),
                date=item.get("snippet").get("publishedAt")
            )
            video.save()
