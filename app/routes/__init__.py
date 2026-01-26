
from app.routes.auth_route import auth
from app.routes.main import main
from app.routes.cart_route import cart
from app.routes.order_route import order_bp
from app.routes.shop_route import shop

def register_routes (app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(order_bp)
    app.register_blueprint(cart)
    app.register_blueprint(shop)