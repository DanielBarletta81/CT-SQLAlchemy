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
 orders = db.relationship('Order', backref= 'customer')

class Order(db.Model):
    __table_name__ = "Orders"

id = db.Column(db.Integer, primary_key = True)
date= db.Column(db.Date(255), nullable = False)
customer_id = db.Column(db.Integer, 
db.ForeignKey('Customers.id') )

class Customer_Accounts(db.Model):
 __table_name__ = "Customers_Accounts"

 id = db.Column(db.Integer, primary_key = True)
 username= db.Column(db.String(255), nullable = False)
 email = db.Column(db.String(320))
 password = db.Column(db.String(15))
 customer = db.relationship('Customer', backref= 'customer_account')


 ###
 ### add order table here ###
 order_product = db.Table("Order_Product",
    db.Column('order_id', db.Integer, db.ForeignKey('orders_id'), primary_key = True),
    db.Column('product_id', db.Integer, db.ForeignKey('products_id'), primary_key = True))

class Product(db.Model):
    __table_name__ = "Products"

id = db.Column(db.Integer, primary_key = True)
name= db.Column(db.String(255), nullable = False)
price= db.Column(db.Integer, nullable = False)


with app.app_context():
    db.create_all()

if __name__ == ('__main__'):
    app.run(debug=True)