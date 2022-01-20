from flask import render_template
from app import app
from models.orderinfo import orders

@app.route('/orders')
def index():
    return render_template('index.html', customerOrders = orders)

@app.route('/orders/<number>')
def single_order(number):
    return render_template('singleorder.html', order_list = orders[int(number)])