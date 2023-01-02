from flask import session, render_template, request, redirect, flash, url_for, Blueprint
from models.user import User
from extensions import db

blueprint = Blueprint('user_profile', __name__)

username_key = 'username'
email_key = 'email'


@blueprint.route('/user-profile')
def profile():
    if username_key in session:
        email = None
        if email_key in session:
            email = session[email_key]
        return render_template('profile.html', email=email)
    else:
        return redirect(url_for('main.home'))


@blueprint.route('/update-information', methods=['POST'])
def update_information():
    try:
        email = request.form['email']
        session['email'] = email
        found_user = User.query.filter_by(
            name=session[username_key]).first()
        found_user.email = email
        db.session.commit()
        flash('Email has been updated!')
    except:
        flash('Email has already been used!')
    finally:
        return redirect(url_for('user_profile.profile'))
