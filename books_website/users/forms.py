from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from books_website.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(message='Введите логин'),
                                                Length(min=1, max=20,
                                                       message='Убедитесь, что длина логина от 1 до 20 символов')])
    email = StringField('Email', validators=[DataRequired(message='Введите email'),
                                             Email(message='Проверьте правильность email')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Введите пароль')])
    confirm_password = PasswordField('Подтверждение пароля',
                                     validators=[DataRequired(message='Подтвердитее пароль'),
                                                EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Данный логин занят. Пожалуйста, выберите другой.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Данный email занят. Пожалуйста, выберите другой.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Введите email'),
                                             Email(message='Проверьте правильность email')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Введите пароль')])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')







