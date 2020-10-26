from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewBookForm(FlaskForm):
    name = StringField('Название книги', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    book_file = StringField('Название файла', validators=[DataRequired()])
    author_id = StringField('Id автора', validators=[DataRequired()])
    submit = SubmitField('Добавить')


