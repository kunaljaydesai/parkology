from flask import Flask
app = Flask(__name__)
app.secret_key = "parkology"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/parkology'

from models import db
db.init_app(app)

import parkapp.routes

