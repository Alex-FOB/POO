from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
#from models import 

@app.route('/')
def inicio():
    pass


if __name__ == '__main__':
    app.run(debug=True)