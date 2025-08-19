from flask import Flask

def create_app(config_name = 'development'):
    app = Flask(__name__)

    if config_name == 'development':
        app.config.from_object('config.DevelopmentConfig')
    
    app.config["CONFIG_NAME"] = config_name

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
