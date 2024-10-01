from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_cros import CORS


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://friends.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)

app.run(debug=True)