from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config([])

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Customer(db.Model):
 __table_name__ = "Customers"

 id = db.Column(db.Integer, primary_key = True)
 name= db.Column(db.String(255), nullable = False)
 email = db.Column(db.String(320))
 phone = db.Column(db.String(15))

class Order(db.Model):
    __table_name__ = "Orders"

id = db.Column(db.Integer, primary_key = True)
date= db.Column(db.Date(255), nullable = False)
customer_id = db.Column(db.Integer, 
db.ForeignKey('Customers.id') )