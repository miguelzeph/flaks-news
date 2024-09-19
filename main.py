from flask import Flask
from flask_session import Session
from news.views import news

from news.config_flask import config_flask

app = Flask(
    __name__,
    template_folder="./news/templates",
    static_folder="./news/static"
)

app.register_blueprint(news)


config_flask(app) # Our personal config
Session(app) # Used to add Server-side Session to one or more Flask applications
