from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import current_app



db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database()

    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        with current_app.app_context():
            db.create_all()
        print('Created Database!')


