from flask import session, render_template, request, redirect, flash, url_for, Blueprint
from auth.auth_service import AuthService
from user.user_service import UserService
from config import email_session_key, username_session_key

blueprint = Blueprint('user', __name__)
auth = AuthService()
user = UserService()


@blueprint.route('/user-profile')
def profile():
    if auth.is_login():
        return render_template('profile.html', user=user.find_user_by_name(session[username_session_key]))
    else:
        return redirect(url_for('main.home'))


@blueprint.route('/update-information', methods=['POST'])
def update_information():
    try:
        user.update_email(request.form[email_session_key])
        flash('Email has been updated!')
    except Exception:
        flash('Email has already been used!')
    finally:
        return redirect(url_for('user.profile'))
