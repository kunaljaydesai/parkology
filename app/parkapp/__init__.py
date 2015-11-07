from flask import flask
app = Flask(__name__)
app.secret_key = "parkology"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/parkology'

import parkapp.routes

