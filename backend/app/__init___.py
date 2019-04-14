from flask import Flask, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_materialize import Material
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_wtf import
import logging
from logging.handlers import SMTPHandler

db = SQLAlchemy()
mail = Mail()
materialize = Material()
migrate = Migrate()
markdown = Markdown()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)²²
    materialize.init_app(app)
    migrate.init_app(app)
    markdown(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddr=app.config['ADMINS'], subject='Erreur Arcanique',
                credentials=auth, secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Lancement Arcanique')

    return app

from app import models, mailing
