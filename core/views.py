from flask import Blueprint, render_template, request, jsonify, redirect
from youtube_api import YoutubeAPI
from download_video import Downloader

views = Blueprint(__name__, 'views')
ytbAPI = YoutubeAPI()


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/search_with_keyword', methods=['POST'])
def search_with_keyword():
    key_word = request.form['keyword']
    videos = ytbAPI.search_with_keyword(key_word)
    return redirect_by_videos_length(videos)


def redirect_by_videos_length(videos):
    if len(videos) == 0:
        return render_template('not-found.html')
    return render_template('index.html', videos=videos)


@views.route('/search_with_link', methods=['POST'])
def search_with_link():
    try:
        link = request.form['link']
        videoId = link.split('watch?v=')[1]
        videos = ytbAPI.search_with_videoId(videoId)
        return redirect_by_videos_length(videos)
    except:
        return render_template('failed.html')


@views.route('/download')
def download():
    try:
        d = Downloader()
        args = request.args
        videoId = args.get('id')
        quality = args.get('quality')
        destination = args.get('dest')
        d.download(videoId, quality, destination)
        return render_template('/succeed.html')
    except Exception:
        return render_template('failed.html')
