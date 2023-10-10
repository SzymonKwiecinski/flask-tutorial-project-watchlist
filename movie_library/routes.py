import uuid

from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    request,
    current_app,
    url_for,
)

from movie_library.models import Movie
from movie_library.forms import MovieForm
from dataclasses import asdict

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template("index.html", title="Movie Watchlist")


@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie(
            _id=uuid.uuid4().hex,
            title=form.title.data,
            director=form.director.data,
            year=form.year.data,
        )

        current_app.db.movie.insert_one(asdict(movie))

        return redirect(url_for(".index"))

    return render_template(
        "new_movie.html", title="Movies Watchlist - Add Movie", form=form
    )


@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))