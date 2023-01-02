from flask import session, render_template, request, redirect, flash, url_for, Blueprint
from auth.auth_service import AuthService
from user.user_service import UserService
from config import email_session_key

blueprint = Blueprint('user', __name__)
auth = AuthService()
user = UserService()


@blueprint.route('/user-profile')
def profile():
    if auth.is_login():
        return get_to_profile_page()
    else:
        return redirect(url_for('main.home'))


def get_to_profile_page():
    email = None
    if user.has_set_email_already():
        email = session[email_session_key]
    return render_template('profile.html', email=email)


@blueprint.route('/update-information', methods=['POST'])
def update_information():
    try:
        user.update_email(request.form[email_session_key])
        flash('Email has been updated!')
    except Exception:
        flash('Email has already been used!')
    finally:
        return redirect(url_for('user_profile.profile'))
