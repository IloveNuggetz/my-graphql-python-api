
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:user@localhost:3306/testflaskgraphql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

controllers = []


def create_app():

    from .Controller.GraphQLController import GraphQLController
    controllers.append(GraphQLController())
    for controller in controllers:
        bp = controller.get_bp()
        app.register_blueprint(bp)
        pass


create_app()
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
