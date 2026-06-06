from flask import Blueprint, render_template
from app.models import Post

main = Blueprint("main", __name__)

@main.route("/")
def home():

    posts = Post.query.all()

    return render_template(
        "home.html",
        posts=posts
    )