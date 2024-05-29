from flask import Flask, make_response, request, render_template
from .utils import auth_required

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    @app.route("/")
    @auth_required
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    create_app()
