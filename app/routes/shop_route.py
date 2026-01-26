from flask import Blueprint, render_template
from app.models.product import Product

shop = Blueprint('shop', __name__, template_folder='templates', static_folder='static')

@shop.route('/')
def product_details(id):
    products = Product.query.get_or_404(id)
    return render_template('product.html', product=product)
