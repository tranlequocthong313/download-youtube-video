from flask import Blueprint, render_template, request, jsonify, redirect
from youtube_api import YoutubeAPI
from download_video import Downloader

views = Blueprint(__name__, 'views')
ytbAPI = YoutubeAPI()


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/search')
def search():
    key_word = request.args.get('keyword')
    videos = ytbAPI.search_with_keyword(key_word)
    return redirect_by_videos_length(videos)


def redirect_by_videos_length(videos):
    if len(videos) == 0:
        return render_template('not-found.html')
    return render_template('index.html', videos=videos)


@views.route('/download/<videoId>/<quality>')
def download(videoId, quality):
    d = Downloader()
    try:
        d.download(videoId, quality)
        return render_template('/succeed.html')
    except Exception:
        return render_template('failed.html')


@views.route('/download')
def download_with_query():
    try:
        link = request.args.get('link')
        videoId = link.split('watch?v=')[1]
        videos = ytbAPI.search_with_videoId(videoId)
        return redirect_by_videos_length(videos)
    except:
        return render_template('failed.html')
