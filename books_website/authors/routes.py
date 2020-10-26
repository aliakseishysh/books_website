from flask import Blueprint, render_template

from books_website.models import Author

authors = Blueprint('authors', __name__)


@authors.route("/author/<int:author_id>")
def author(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template("author.html", title=author.name, author=author)
