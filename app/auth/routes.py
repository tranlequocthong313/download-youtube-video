from flask import session, render_template, request, redirect, url_for, Blueprint
from auth.auth_service import AuthService
from config import username_session_key, email_session_key

blueprint = Blueprint('auth', __name__)
auth = AuthService()


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return auth.login()
    else:
        return redirect_by_login_status()


def redirect_by_login_status():
    if auth.is_login():
        return redirect(url_for('main.home'))
    return render_template('login.html')


@blueprint.route('/logout')
def logout():
    session.pop(username_session_key, None)
    session.pop(email_session_key, None)
    return redirect(url_for('auth.login'))
