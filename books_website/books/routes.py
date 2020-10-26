from flask import Blueprint, render_template

from books_website.models import Book

books = Blueprint('books', __name__)


@books.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book.html", title=book.name, book=book)
