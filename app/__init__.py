from flask import Flask
from config import Config
from extensions import db
from main.routes import blueprint as main_blueprint
from user.routes import blueprint as user_blueprint
from auth.routes import blueprint as auth_blueprint
from helper.routes import blueprint as helper_blueprint


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(helper_blueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
