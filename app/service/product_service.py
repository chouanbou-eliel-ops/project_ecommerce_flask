from app.models.product import Product
from app.extensions import db

def get_all_products():
    products = Product.query.all()
    return products

def get_product_by_id(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return product

def get_product_by_username(username):
    product = Product.query.filter_by(username=username).first()
    return product

def get_product_by_email(email):
    product = Product.query.filter_by(email=email).first()
    return product

def create_product(name, price, description):
    product = Product(name=name, price=price, description=description)
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product_id, name, price, description):
    product = Product.query.filter_by(id=product_id).first()
    product.name = name
    product.price = price
    product.description = description
