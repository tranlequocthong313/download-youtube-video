from googleapiclient.discovery import build
from dotenv import load_dotenv
from dump_data import DUMP_DATA
import os

load_dotenv()
SECRET_KEY = os.getenv("YOUTUBE_API_KEY")


class YoutubeAPI:
    def search_with(self, query: str) -> list:
        youtube = build('youtube', 'v3',
                        developerKey=SECRET_KEY)

        request = youtube.search().list(
            part='snippet',
            maxResults=100,
            q=query
        )

        response = None
        try:
            response = request.execute()
        except Exception:
            # Rendering dump data because youtube limited its api requesting per day
            response = DUMP_DATA

        return response['items']
