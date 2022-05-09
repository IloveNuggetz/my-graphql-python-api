
from flask_cors import CORS
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import find_modules, import_string

db=None

def create_app():
    app = Flask(__name__)
    app.config.update({})
    CORS(app)

    register_db(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    for name in find_modules(__name__):
        mod = import_string(name)
        if(hasattr(mod, 'bp')):
            app.register_blueprint(mod.bp)

def register_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:user@localhost:3306/testflaskgraphql"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    global db
    db = SQLAlchemy(app)


app = create_app()


"""
@app.route('/')
def hello():
    response = None
    try:
        response = WikimediaService().getMostViewedPages("de", "wikiquote")
        pass
    except GameException as e:
        response = e.message

    return response
"""
