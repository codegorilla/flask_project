from flask import Flask
from config import Config
from app.extensions import db
from app.views import register_routes

def create_app (config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  # db.init_app(app)

  register_routes(app)

  return app
