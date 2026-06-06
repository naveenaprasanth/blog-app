from flask import Blueprint, render_template

from app.models import User, Post

admin = Blueprint("admin", __name__)

@admin.route("/admin")
def dashboard():

    users = User.query.all()
    posts = Post.query.all()

    return render_template(
        "admin.html",
        users=users,
        posts=posts
    )