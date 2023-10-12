from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import InputRequired, NumberRange


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1878, message="Please enter a year in the format YYYY."),
        ],
    )

    submit = SubmitField("Add Movie")


class StringListFiled(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            return []


class ExtendedMovieForm(MovieForm):
    cast = StringListFiled("Cast")
    series = StringListFiled("Series")
    tags = StringListFiled("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")
