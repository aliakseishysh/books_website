from flask import Blueprint, render_template, abort, flash
from flask_login import login_required, current_user

from books_website import db
from books_website.admin_panel.forms import NewBookForm, NewAuthorForm, DelBookForm
from books_website.models import Book, Author

admin_panel = Blueprint('admin_panel', __name__)


@login_required
@admin_panel.route('/new/book', methods=['GET', 'POST'])
def new_book():
    if current_user.is_authenticated and current_user.account_type == "admin":
        form = NewBookForm()
        if form.validate_on_submit():
            book = Book(name=form.name.data, description=form.description.data, book_file=form.book_file.data, author_id=form.author_id.data)
            db.session.add(book)
            db.session.commit()
            return render_template('account.html')
        return render_template('new_book.html', title='Новая книга', form=form)
    else:
        abort(405)


@login_required
@admin_panel.route('/new/author', methods=['GET', 'POST'])
def new_author():
    if current_user.is_authenticated and current_user.account_type == "admin":
        form = NewAuthorForm()
        if form.validate_on_submit():
            author = Author(name=form.name.data)
            db.session.add(author)
            db.session.commit()
            return render_template('account.html')
        return render_template('new_author.html', title='Новый автор', form=form)
    else:
        abort(405)


@login_required
@admin_panel.route('/authors/ids')
def authors_ids():
    if current_user.is_authenticated and current_user.account_type == "admin":
        authors = Author.query.all()
        return render_template('authors_ids.html', title='Ids авторов', authors=authors)
    else:
        abort(405)


@login_required
@admin_panel.route('/books/ids')
def books_ids():
    if current_user.is_authenticated and current_user.account_type == "admin":
        books = Book.query.all()
        return render_template('books_ids.html', title='Ids книг', books=books)
    else:
        abort(405)


@login_required
@admin_panel.route('/del/book', methods=['GET', 'POST'])
def del_book():
    if current_user.is_authenticated and current_user.account_type == "admin":
        form = DelBookForm()
        if form.validate_on_submit():
            book_id = form.book_id.data
            book = Book.query.get(book_id)
            db.session.delete(book)
            db.session.commit()
            return render_template('account.html')
        return render_template('del_book.html', title='Удалить книгу', form=form)
    else:
        abort(405)


@login_required
@admin_panel.route('/update/account', methods=['GET', 'POST'])
def update_account():
    if current_user.is_authenticated and current_user.account_type == "admin":
        return render_template('update_account.html')
    else:
        abort(405)





