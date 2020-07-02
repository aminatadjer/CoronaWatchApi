
from django.conf import settings
from random import sample
from robot.models import Veille
import requests
from config import SUBJECT, YOUTUBE_API_KEY


def scrap_youtube_videos():
    print("[*] Refresh database with new videos...")

    max_results = 50
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={SUBJECT}&key={YOUTUBE_API_KEY}&type=video&maxResults={max_results}"
    )
    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        video = Veille.objects.create(
            url=f"{item.get('id').get('videoId')}",
            titre=item.get("snippet").get("title"),
            description=item.get("snippet").get("description"),
            date=item.get("snippet").get("publishedAt"),
            type="youtube"
        )
        video.save()
