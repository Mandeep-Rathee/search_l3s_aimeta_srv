"""Flask app initialization via factory pattern."""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from search_l3s_aimeta.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    # to avoid a circular import
    from search_l3s_aimeta.api import api_bp
    
    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    return app
