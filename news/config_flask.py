import os
from config import config


def config_flask(app):
    """Setup Flask environment variables

    Args:
        app : The flask object
    """
    app.config["SECRET_KEY"] = config.get("flask.secret_key")
    app.config["SESSION_TYPE"] = config.get("flask.session_type")
    os.environ["FLASK_DEBUG"] = str(
        config.get("flask.debug")
    )  # app.config["FLASK_DEBUG"]
