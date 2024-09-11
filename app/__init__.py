from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_options
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap



db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='prd'):
    app = Flask(__name__)

    current_config = config_options[config_name]
    app.config.from_object(current_config)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap = Bootstrap(app)
    
    from app.books import book_blueprint
    app.register_blueprint(book_blueprint)

    
    return app

    
