import os

from flask import Flask
from werkzeug.exceptions import HTTPException
from src.api.helpers import error_response


# new
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register blueprints
    from src.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)

    from src.api.terms import terms_blueprint

    app.register_blueprint(terms_blueprint)

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        response = error_response()
        response["errors"].append(str(e))
        return response, code

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
