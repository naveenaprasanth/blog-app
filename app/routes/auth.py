from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import db, bcrypt

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):
            login_user(user)
            return redirect(url_for("main.home"))

    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():

    logout_user()

    return redirect(url_for("main.home"))