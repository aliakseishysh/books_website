from flask import Flask
from books_website.config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from books_website.main.routes import main
    from books_website.users.routes import users
    from books_website.authors.routes import authors
    from books_website.books.routes import books
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(authors)
    app.register_blueprint(books)

    return app



