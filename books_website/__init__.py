from flask import Flask
from books_website.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from books_website.main.routes import main
    from books_website.users.routes import users
    from books_website.authors.routes import authors
    from books_website.books.routes import books
    from books_website.admin_panel.routes import admin_panel
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(authors)
    app.register_blueprint(books)
    app.register_blueprint(admin_panel)

    return app



