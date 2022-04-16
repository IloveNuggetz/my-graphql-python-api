from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://user:user@localhost:3306/testflaskgraphql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

CORS(app)

@app.route('/')
def hello():
    return 'My First API !!'
