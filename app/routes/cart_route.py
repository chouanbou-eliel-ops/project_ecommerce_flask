from flask import Blueprint, render_template, redirect, url_for, session
#from pip._internal.network import session
from flask_login import login_required
from app.models.product import Product

cart = Blueprint('cart', __name__)

@cart.route('/view_cart_item/<int:id>')
def view_cart_item(id):
    return render_template('cart_item.html', cart=cart)

@cart.route('/cart')
#@login_required
def cart_view():
    cart_used = session.get('cart', {})
    products = cart_used.get('products', [])
    total =0
    for product_id, quantity in cart_used.items():
        product = Product.query.get_or_404(product_id)
        total += product.price * quantity
        product.quantity = quantity
        products.append ({'product': product,
                          "quantité": product.quantity,
        "subtotal": product.price * quantity
        })
    return render_template('cart/cart.html', cart=cart_used, products=products, total=total)

@cart.route('/add/<int:id>', methods=['GET', 'POST'])
#@login_required
def add_to_cart(id):
    cart = session.get('cart', {})
    """
        if request.method == 'GET':
        return render_template('cart.html', cart=cart)
    else:
    """
    if str(id) not in cart:
        cart[id] = Product(id)
    # Il faudrait revoir ceci

    session['cart'] = cart
    return redirect(url_for('cart.add_to_cart'))# revoir ou rediriger

@cart.route('/cart/remove/<int:id>', methods=['GET', 'POST'])
#@login_required
def remove_from_cart(id):
    cart = session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    session['cart'] = cart
    return redirect(url_for('cart.view_cart'))

@cart.route('/cart/clear')
#@login_required
def clear_cart():
    session['cart'] = {}
    #session.pop('cart', None)
    return redirect(url_for('cart.cart_view'))



