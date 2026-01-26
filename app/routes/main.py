from flask import Blueprint, render_template
from app.models.product import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()# va dans la table et recupere tout les produits
    return render_template('index.html', products=products)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/products')
def products():
    products = Product.query.all()
    return render_template('products/product.html', products=products)

@main.route('/shop')
def shop():
    return render_template('shop.html')

@main.route('/users')
def users():
    return render_template('users.html')
