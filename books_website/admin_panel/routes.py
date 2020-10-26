from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

admin_panel = Blueprint('admin_panel', __name__)


@login_required
@admin_panel.route('/new/book')
def new_book():
    if current_user.is_authenticated and current_user.account_type == "admin":
        return render_template('new_book.html')
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





