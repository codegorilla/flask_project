from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from markupsafe import escape
from app.forms import LoginForm

def register_routes (app):

  @app.route("/")
  def index ():
    return render_template("index.html")

  @app.route("/home")
  def home ():
    return render_template("index.html")

  @app.route("/login", methods=['GET', 'POST'])
  def login ():
    form = LoginForm()
    if  form.validate_on_submit():
      flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
      return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
  
  @app.route("/register")
  def register ():
    return render_template("register.html")


  # @app.route("/<name>")
  # def hello(name):
  #     return render_template("index.html", content=name)

  # @app.route("/hello")
  # def hello():
  #     name = request.args.get("name", "Flask")
  #     return f"Hello, {escape(name)}!"

  # @app.route("/<name>")
  # def goodbye(name):
  #     return f"Hello, {escape(name)}!"
