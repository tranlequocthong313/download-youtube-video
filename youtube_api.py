from googleapiclient.discovery import build

api_key = 'AIzaSyC1EQ_WwMD3iQWhvVPapeW7BWx6uwM1_Z4'


def request(query):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q=query
    )

    response = request.execute()
    return response
