import os

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User, Player
from .footcontrol import recover_email
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post():
    # login code goes here
    user_login = request.form.get("userid")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    if '@' in user_login:
        user = User.query.filter_by(email=user_login).first()
    else:
        user = User.query.filter_by(phone=int(user_login)).first()
        
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash("Verifique seus dados e tente de novo.")
        flash("alert-danger")
        return redirect(
            url_for("auth.login")
        )  # if the user doesn't exist or password is wrong, reload the page
    
    if user.admin == 1:
        user.groupadm = 1
    elif user.groupid > 0:
        player = Player.query.filter_by(gourpid=user.groupid, userid=user.id).first()
        if player:
            user.groupadm = player.groupadm
            
    login_user(user, remember=remember)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("main.profile"))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/recoverlogin")
def recoverlogin():

    return render_template("recoverlogin.html")

@auth.route("/recoverlogin", methods=["POST"])
def recoverlogin_post():

    email = request.form.get("email")
    
    if "@" not in email:
        flash("Entrar E-mail válido")
        flash("alert-danger")
        return redirect(url_for("auth.signup"))

    user = User.query.filter_by(
        email=email
    ).first()  

    if ( not user ):  
        flash("E-mail não existe no banco de dados.")
        flash("alert-danger")
    else:
        password = os.urandom(5).hex()
        if recover_email(user, password):
            user.password = generate_password_hash(password, method="pbkdf2:sha256")
            db.session.commit()
            flash("E-mail de recuperação enviado.")
            flash("alert-success")
        else:     
            flash("Falha ao enviar email de recuperação. Contatar administrador.")
            flash("alert-danger")

    return redirect(url_for("auth.login"))