from flask import session, render_template, request, redirect, flash, url_for, Blueprint
from models.user import User
from extensions import db

blueprint = Blueprint('auth', __name__)

username_key = 'username'
email_key = 'email'


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        session[username_key] = request.form[username_key]

        found_user = User.query.filter_by(
            name=request.form[username_key]).first()
        if found_user:
            session[email_key] = found_user.email
        else:
            user = User(session[username_key], None)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for('main.home'))
    else:
        if username_key in session:
            return redirect(url_for('main.home'))
        return render_template('login.html')


@blueprint.route('/logout')
def logout():
    session.pop(username_key, None)
    session.pop(email_key, None)

    return redirect(url_for('auth.login'))
