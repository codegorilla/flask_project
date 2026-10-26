from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from markupsafe import escape

from app import app

@app.route("/")
def index ():
  return render_template("index.html")

@app.route("/login")
def login ():
  return render_template("login.html")

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
