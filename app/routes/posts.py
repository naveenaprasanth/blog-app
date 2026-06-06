from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from app.forms import PostForm
from app.models import Post
from app import db

posts = Blueprint("posts", __name__)


@posts.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():

    form = PostForm()

    if form.validate_on_submit():

        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("main.home"))

    return render_template("create_post.html", form=form)