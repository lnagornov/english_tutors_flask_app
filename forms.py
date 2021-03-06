from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, HiddenField, SelectField
from wtforms.validators import InputRequired

from func import get_data_from_db


class BookingForm(FlaskForm):
    """Booking form for a class with a tutor."""

    tutor_id = HiddenField()
    class_day = HiddenField()
    time = HiddenField()
    name = StringField("Вас зовут", [InputRequired("Пожалуйста, введите ваше имя")])
    phone = StringField(
        "Ваш телефон", [InputRequired("Пожалуйста, введите ваш номер телефона")]
    )
    submit = SubmitField("Записаться на пробный урок")


class RequestForm(FlaskForm):
    """Request form for a tutor search."""

    goal = RadioField(
        "Какая цель занятий?",
        choices=[
            (key, " ".join(value))
            for key, value in get_data_from_db(option="goals").items()
        ],
        default="travel",
    )

    time_for_practice = RadioField(
        "Сколько времени есть?",
        choices=[
            (key, value)
            for key, value in get_data_from_db(option="time_for_practice").items()
        ],
        default="limit1_2",
    )

    name = StringField("Вас зовут", [InputRequired("Пожалуйста, введите ваше имя")])
    phone = StringField(
        "Ваш телефон", [InputRequired("Пожалуйста, введите ваш номер телефона")]
    )
    submit = SubmitField("Найдите мне преподавателя!")


class SortTutorsForm(FlaskForm):
    """Form for sorting list of tutors.
    Sorting options:
    1. random order;
    2. tutors with high rating first;
    3. tutors with high price first;
    4. tutors with low price first;
    """

    sort_by = SelectField(
        "Сортировка преподавателей",
        choices=[
            ("random", "В случайном порядке"),
            ("high_rating_first", "Сначала лучшие по рейтингу"),
            ("high_price_first", "Сначала дорогие"),
            ("low_price_first", "Сначала недорогие"),
        ],
        default="random",
    )
    submit = SubmitField("Сортировать")
