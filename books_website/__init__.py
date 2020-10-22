from flask import Flask
from books_website.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from books_website.main.routes import main
    from books_website.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
