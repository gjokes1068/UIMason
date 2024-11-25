from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main_bp  # Import routes from a different module
    app.register_blueprint(main_bp)

    return app
