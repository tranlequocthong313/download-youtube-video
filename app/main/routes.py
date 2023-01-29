from flask import session, render_template, request, redirect, flash, url_for, Blueprint, jsonify
from main.youtube_api import YoutubeAPI
from main.downloader import Downloader
from config import username_session_key
from auth.auth_service import AuthService
from main.video import Video
from user.user_service import UserService
import redis
import json

blueprint = Blueprint('main', __name__)
ytbAPI = YoutubeAPI()
auth = AuthService()
downloader = Downloader()
user = UserService()
client = redis.Redis(host='localhost', port=6379, db=0)


@blueprint.route('/')
@blueprint.route('/home')
def home():
    username = None
    if auth.is_login():
        username = session[username_session_key]
    return render_template('index.html', username=username)


@blueprint.route('/search_with_keyword', methods=['POST'])
def search_with_keyword():
    kw = request.form['keyword']
    key = f'search_with_keyword:::{kw}'
    cache = get_cache(key)
    if (cache):
        print('Hit cache:::')
        return redirect_by_videos_length(json.loads(cache))
    videos = ytbAPI.search_with_keyword(request.form['keyword'])
    client.set(key, json.dumps(videos))
    client.expire(key, 24 * 60 * 60)
    print('Miss cache:::')
    return redirect_by_videos_length(videos)


def redirect_by_videos_length(videos):
    if len(videos) == 0:
        flash('Video couldn\'t be found!')
        return redirect(url_for('main.home'))
    return render_template('index.html', videos=videos, username=session[username_session_key])

def get_cache(param):
    return client.get(param) 

@blueprint.route('/search_with_link', methods=['POST'])
def search_with_link():
    try:
        # Cutting the youtube link https://www.youtube.com/watch?v=O3qfQikPN1s to get the ID
        videoId = request.form['link'].split('watch?v=')[1]
        key = f'search_with_link:::{videoId}'
        cache = get_cache(key)
        if (cache):
            print('Hit cache:::')
            return redirect_by_videos_length(json.loads(cache))
        videos = ytbAPI.search_with_videoId(videoId)
        client.set(key, json.dumps(videos))
        client.expire(key, 24 * 60 * 60 * 3)
        print('Miss cache:::')
        return redirect_by_videos_length(videos)
    except:
        flash('Something went wrong, please check the link!')
        return redirect(url_for('main.home'))


@blueprint.route('/download')
def download():
    try:
        video = Video(request.args.get('id'), request.args.get(
            'quality'), request.args.get('dest'))
        downloader.download(video)
        if auth.is_login():
            user.add_new_downloaded_video(video)
        flash('Video has been downloaded!')
        return redirect(url_for('main.home'))
    except Exception:
        flash('Video hasn\'t been downloaded!')
        return redirect(url_for('main.home'))
