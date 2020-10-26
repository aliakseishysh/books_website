from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

from books_website import db
from books_website.admin_panel.forms import NewBookForm
from books_website.models import Book

admin_panel = Blueprint('admin_panel', __name__)


@login_required
@admin_panel.route('/new/book')
def new_book():
    if current_user.is_authenticated and current_user.account_type == "admin":
        form = NewBookForm()
        if form.validate_on_submit():
            book = Book(name=form.name.data, description=form.description.data, author_id=form.author_id.data)
            db.session.add(book)
            db.session.commit()
            return render_template('account.html')
        return render_template('new_book.html', title='Новая книга', form=form)
    else:
        abort(405)


@login_required
@admin_panel.route('/del/book')
def del_book():
    if current_user.is_authenticated and current_user.account_type == "admin":
        return render_template('del_book.html')
    else:
        abort(405)


@login_required
@admin_panel.route('/update/account')
def update_account():
    if current_user.is_authenticated and current_user.account_type == "admin":
        return render_template('update_account.html')
    else:
        abort(405)





