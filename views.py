from flask import Blueprint, render_template, request, jsonify, redirect
from youtube_api import YoutubeAPI
from download_video import Downloader

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    key_word = request.args.get('q')
    ytbAPI = YoutubeAPI()
    videos = ytbAPI.search_with(key_word)
    videos = []
    if len(videos) == 0:
        return render_template('not-found.html')
    return render_template('index.html', videos=videos)


@views.route('/download/<videoId>')
def download(videoId):
    d = Downloader()
    d.download(videoId)
    return redirect('/')
