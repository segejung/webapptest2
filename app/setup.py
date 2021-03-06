#!/usr/bin/env python3

import logging
import pathlib
from os import path
import os
from controllers.home import controller as home_controller
from controllers.form import controller as form_controller
from controllers.html import controller as html_controller
from controllers.pdf import controller as pdf_controller
from controllers.api import controller as api_controller
from controllers.jobs import controller as jobs_controller
from controllers.download import controller as download_controller
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from db import db

env_name = os.environ.get('ENV', 'dev_local')  # default ENV is dev_local


def create_app(testing=False):
    app = Flask(__name__, template_folder='templates',
                static_folder='static', static_url_path='')
    app.config.from_object(__name__)
    app.logger.setLevel(logging.INFO)
    app.logger.info(f"Environment: {env_name}")
    # For Flash Messages
    app.secret_key = 'b7bb85a76fb487473409'
    load_config(app)

    CORS(app, resources={r'/*': {'origins': '*'}})

    # register controllers
    app.register_blueprint(home_controller)
    app.register_blueprint(api_controller)
    app.register_blueprint(pdf_controller)
    app.register_blueprint(html_controller)
    app.register_blueprint(form_controller)
    app.register_blueprint(jobs_controller)
    app.register_blueprint(download_controller)

    db.init_app(app)

    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database

    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        if not database_exists(engine.url):
            create_database(engine.url)

        # migrate database
        with app.app_context():
            db.create_all()
            db.session.commit()

    except Exception as e:
        app.logger.error(f'Database Init Exception: {e}')
        exit(1)

    return app


def load_config(app):
    current_abs_path = pathlib.Path(__file__).resolve().parents[0]
    config_file_path = f"{current_abs_path}/configs/{env_name}.py"

    if path.exists(config_file_path):
        app.logger.info(f"Loads config from {config_file_path}")
    else:
        app.logger.error(
            f"Config file for ENV {env_name} at path {config_file_path} does not exist. Exit.")
        exit(1)
    app.config.from_pyfile(config_file_path)
