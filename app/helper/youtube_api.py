from googleapiclient.discovery import build
from dotenv import load_dotenv
from helper.dump_data import DUMP_DATA
import os

load_dotenv()
SECRET_KEY = os.getenv("YOUTUBE_API_KEY")


class YoutubeAPI:
    def search_with_keyword(self, query):
        request = self.__build_youtube().search().list(
            part='snippet',
            maxResults=10,
            q=query
        )
        return self.__execute(request)

    def __build_youtube(self):
        return build('youtube', 'v3',
                     developerKey=SECRET_KEY)

    def __execute(self, request):
        response = None
        try:
            response = request.execute()
        except Exception:
            # Rendering dump data because youtube limited its api requesting per day
            response = DUMP_DATA

        return response['items']

    def search_with_videoId(self, videoId):
        request = self.__build_youtube().videos().list(
            part="snippet, contentDetails, statistics",
            id=videoId
        )
        return self.__execute(request)
