from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    SWAGGER_URL = '/docs'  
    API_URL = '/static/swagger.json'
    swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL,
        config={'app_name': "Flask CRUD API"}
    )
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

    from app.routes.caseCreator import blueprint
    app.register_blueprint(blueprint)

    return app
