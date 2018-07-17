from flask import Flask
from web import routes
from scripts.database_utils import db_create_seed


def create_app() -> Flask:
    app = Flask(__name__, template_folder='web/templates',
                static_url_path='/static',
                static_folder='web/static')
    return app


def setup_routes(app: Flask) -> None:
    routes.register(app)


if __name__ == '__main__':
    # Create app
    app = create_app()
    # Set app routes
    setup_routes(app)
    # Create and seed database
    db_create_seed()
    # Run App
    app.run(debug=True, host='0.0.0.0')
