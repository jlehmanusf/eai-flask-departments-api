from flask.cli import FlaskGroup
import logging

from src import create_app

app = create_app()
app.logger.setLevel(logging.DEBUG)
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
