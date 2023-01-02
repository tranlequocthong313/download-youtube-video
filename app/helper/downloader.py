from pytube import YouTube


class Downloader:
    def download(self, videoId, quality, destination):
        try:
            link = 'https://www.youtube.com/watch?v=' + videoId
            youtubeObject = YouTube(link).streams

            if quality == 'highest':
                youtubeObject = youtubeObject.get_highest_resolution()
            else:
                youtubeObject = youtubeObject.get_lowest_resolution()

            youtubeObject.download(destination)

            return "Download is completed successfully"
        except:
            raise Exception("An error has occured")
