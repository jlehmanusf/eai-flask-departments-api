from flask import Blueprint
from flask_restx import Api, Resource
from src.api.helpers import successful_response, error_response
import os
import cx_Oracle

terms_blueprint = Blueprint("terms", __name__)
api = Api(terms_blueprint)


class Terms(Resource):
    def get(self):
        banner_password = os.environ.get("BANNER_PASSWORD")
        banner_username = os.environ.get("BANNER_USERNAME")
        banner_instance = os.environ.get("BANNER_INSTANCE")
        try:
            items = []
            connection = cx_Oracle.connect(
                user=banner_username, password=banner_password, dsn=banner_instance
            )
            cursor = connection.cursor()
            results = cursor.execute("select stvterm_code, stvterm_desc from stvterm")
            for row in results:
                items.append({"code": row[0], "description": row[1]})
            connection.close()
            response = successful_response()
            response["data"] = items
            return response
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            response = error_response()
            response["errors"].append(error.message)
            return response


api.add_resource(Terms, "/terms")
