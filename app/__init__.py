from flask import Flask
from config import Config
from extensions import db
from main.routes import blueprint as main_blueprint
from profile.routes import blueprint as profile_blueprint
from auth.routes import blueprint as auth_blueprint


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(auth_blueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
    db.create_all()
