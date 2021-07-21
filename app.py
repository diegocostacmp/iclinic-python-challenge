from flask import Flask

from prescription.api.main import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0")
