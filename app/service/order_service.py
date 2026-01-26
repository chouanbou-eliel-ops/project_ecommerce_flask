from app.models.order import Order
from app.extensions import db

def create_order(user_id, product_id, quantity, price, status, order_date , total_price):
    order = Order(user_id = user_id, total_price = total_price)
    db.session.add(order)
    db.session.commit()
    return order

def get_order(order_id):
    order = Order.query.get(order_id)
    return order

def delete_order(order_id):
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()
    return order

def update_order(order_id, total_price):
    order = Order.query.get(order_id)
    order.total_price = total_price
    db.session.commit()
    return order

def update_order_status(order_id, status):
    order = Order.query.get(order_id)
    order.status = status
    db.session.commit()
    return order

