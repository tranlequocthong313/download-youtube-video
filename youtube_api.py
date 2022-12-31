from googleapiclient.discovery import build


class YoutubeAPI:
    api_key = 'AIzaSyC1EQ_WwMD3iQWhvVPapeW7BWx6uwM1_Z4'

    def search_with(self, query: str) -> list:
        youtube = build('youtube', 'v3', developerKey=self.api_key)

        request = youtube.search().list(
            part='snippet',
            maxResults=100,
            q=query
        )

        response = request.execute()
        return response['items']
