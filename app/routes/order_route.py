from flask import request, Blueprint

from app.service.order_service import create_order

order_bp = Blueprint('orders', __name__)

@order_bp.route('/order', methods=['GET', 'POST'])
def order():

    user_id = request.form['user_id']
    order_id = request.form['order_id']
    """
        order = Order.query.filter_by(user_id=user_id).filter_by(order_id=order_id).first()
    if order:
        return render_template('order.html', order=order)
    else:
    """
    total_price = request.form['total_price']
    create_order(user_id, order_id, total_price)
    return "commande crée avec succes"

