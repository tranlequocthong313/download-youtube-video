from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from youtube_api import request

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    return render_template("index.html")


@views.route('/json')
def get_json():
    return jsonify(request('lose yourself'))