from pytube import YouTube


class Downloader:
    def download(self, videoId):
        link = 'https://www.youtube.com/watch?v=' + videoId
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
            return "Download is completed successfully"
        except:
            raise Exception("An error has occured")
