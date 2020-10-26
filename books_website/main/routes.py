from flask import Blueprint, render_template
from books_website.models import Book


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
