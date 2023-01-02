from flask import session, render_template, request, redirect, flash, url_for, Blueprint
from helper.youtube_api import YoutubeAPI
from helper.downloader import Downloader

blueprint = Blueprint('main', __name__)

username_key = 'username'
email_key = 'email'
ytbAPI = YoutubeAPI()


@blueprint.route('/')
def home():
    username = None
    if username_key in session:
        username = session[username_key]
    return render_template('index.html', username=username)


@blueprint.route('/search_with_keyword', methods=['POST'])
def search_with_keyword():
    key_word = request.form['keyword']
    videos = ytbAPI.search_with_keyword(key_word)
    return redirect_by_videos_length(videos)


def redirect_by_videos_length(videos):
    if len(videos) == 0:
        flash('Video couldn\'t be found!')
        return redirect(url_for('main.home'))
    return render_template('index.html', videos=videos, username=session[username_key])


@blueprint.route('/search_with_link', methods=['POST'])
def search_with_link():
    try:
        # Cutting the youtube link https://www.youtube.com/watch?v=O3qfQikPN1s to get the ID
        videoId = request.form['link'].split('watch?v=')[1]
        videos = ytbAPI.search_with_videoId(videoId)
        return redirect_by_videos_length(videos)
    except:
        flash('Something went wrong, please check the link!')
        return redirect(url_for('main.home'))


@blueprint.route('/download')
def download():
    try:
        d = Downloader()
        args = request.args
        d.download(args.get('id'), args.get('quality'), args.get('dest'))
        flash('Video has been downloaded!')
        return redirect(url_for('main.home'))
    except Exception:
        flash('Video hasn\'t been downloaded!')
        return redirect(url_for('main.home'))
