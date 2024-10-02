import pymysql
import db
from flask import Flask, request
from controller.categories import add_categories
from controller.categories import all_categories
from controller.add_payments import add_payments
from controller.orders import add_orders
from controller.orders import get_orders
from controller.customerr import add_customerr
from controller.customerr import get_customerr
from controller.product import add_product
from controller.product import get_products
from controller.sales_metrics import total_revenue
from controller.sales_metrics import revenue_by_product
from controller.sales_metrics import revenue_city
from controller.sales_metrics import top_selling_products
from controller.order_metrics import total_orders
from controller.order_metrics import pending_orders
from controller.order_metrics import cancelled_orders
from controller.order_metrics import successful_orders
from controller.payment_metrics import pending_payments
from controller.payment_metrics import successful_payments
from controller.product_metrics import inventory_levels
from controller.product_metrics import out_of_stock_products
from controller.geography_metrics import top_cities_by_sales
from controller.geography_metrics import top_countries_by_sales


app = Flask(__name__)

# root API of the application
@app.route("/", methods=['GET'])
def hello():
    return "centralized routing"

app.add_url_rule("/categories", view_func=add_categories, methods=['POST'])
app.add_url_rule("/categories", view_func=all_categories, methods=['GET'])
app.add_url_rule("/products", view_func=add_product, methods=['POST'])
app.add_url_rule("/products", view_func=get_products, methods=['GET'])
app.add_url_rule("/customers", view_func=add_customerr, methods=['POST'])
app.add_url_rule("/customers", view_func=get_customerr, methods=['GET'])
app.add_url_rule("/orders", view_func=add_orders, methods=['POST'])
app.add_url_rule("/orders", view_func=get_orders, methods=['GET'])
app.add_url_rule("/payments", view_func=add_payments, methods=['GET'])
app.add_url_rule("/metrics/sales/total_rev", view_func=total_revenue, methods=['GET'])
app.add_url_rule("/metrics/sales/rev_product", view_func=revenue_by_product, methods=['GET'])
app.add_url_rule("/metrics/sales/rev_city", view_func=revenue_city, methods=['GET'])
app.add_url_rule("/metrics/sales/top_selling", view_func=top_selling_products, methods=['GET'])
app.add_url_rule("/metrics/orders/total_order", view_func=total_orders, methods=['GET'])
app.add_url_rule("/metrics/orders/pending_orders", view_func=pending_orders, methods=['GET'])
app.add_url_rule("/metrics/orders/cancelled_orders", view_func=cancelled_orders, methods=['GET'])
app.add_url_rule("/metrics/orders/successful_orders", view_func=successful_orders, methods=['GET'])
app.add_url_rule("/metrics/payments/pending", view_func=pending_payments, methods=['GET'])
app.add_url_rule("/metrics/payments/successful", view_func=successful_payments, methods=['GET'])
app.add_url_rule("/metrics/product/inventory_levels", view_func=inventory_levels, methods=['GET'])
app.add_url_rule("/metrics/product/out_of_stock", view_func=out_of_stock_products, methods=['GET'])
app.add_url_rule("/metrics/geography/city_sale", view_func=top_cities_by_sales, methods=['GET'])
app.add_url_rule("/metrics/product/country_sale", view_func=top_countries_by_sales, methods=['GET'])
  
if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )

