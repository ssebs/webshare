###
# __init__.py - main flask file
###
from flask import Flask, request, render_template
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder="../frontend/build/static", template_folder="../frontend/build")  # noqa
    CORS(app)

    # Need to import here to avoid circular import issues
    from .utils import test
    from .routes.files import files_routes
    app.register_blueprint(files_routes)

    @app.route("/api/")
    @app.route("/api/test")
    def api_test():
        return "Testing API."

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def frontend(path):
        return render_template("index.html")

    app.app_context().push()

    return app
# create_app


if __name__ == "__main__":
    app = create_app()
    app.run()