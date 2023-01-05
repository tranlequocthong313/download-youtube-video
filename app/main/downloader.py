from pytube import YouTube


class Downloader:
    def download(self, video):
        try:
            self._create_youtube_video(video).download(video.destination)
        except:
            raise Exception("An error has occured")

    def _create_youtube_video(self, video):
        link = "https://www.youtube.com/watch?v=" + video.id
        stream = YouTube(link).streams
        return (
            stream.get_highest_resolution()
            if video.quality == "highest"
            else stream.get_lowest_resolution()
        )
