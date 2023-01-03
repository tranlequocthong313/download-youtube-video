from flask import session, render_template, request, redirect, flash, url_for, Blueprint, jsonify
from models.user import User
from extensions import db

blueprint = Blueprint('helper', __name__)


@blueprint.route('/drop_all', methods=['GET'])
def drop():
    db.drop_all()
    return redirect(url_for('main.home'))


@blueprint.route('/get_users', methods=['GET'])
def get_users():
    return render_template('users.html', users=User.query.all())
