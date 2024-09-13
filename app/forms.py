from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from . import app
from .models import Category


def get_categories():
    with app.app_context():
        """Получение всех возможных категорий"""
        categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    """Класс формы добавления новости на портале"""
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым"), Length(max=255,
                                                                                                           message='Введите заголовок длиной до 255 символов')])
    text = TextAreaField('Текст', validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')


class CategoryForm(FlaskForm):
    """Класс формы добавления категорий новостей"""
    title = StringField('Название',
                        validators=[DataRequired(message="Поле не должно быть пустым"), Length(max=255,
                                                                                               message='Введите название длиной до 255 символов')])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Некорректный email')])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(),
                                                              EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')
