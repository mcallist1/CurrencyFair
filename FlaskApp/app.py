import os
import sqlite3

import json
from flask import Flask, jsonify, request, render_template, g
import logging

logging.basicConfig(filename='/tmp/app.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'db.sqlite')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        logger.debug(DATABASE)
        db = g._database = sqlite3.connect(DATABASE)
        # db.execute('CREATE TABLE transactions (userId,currencyFrom,currencyTo,amountSell,amountBuy,rate,timePlaced,originatingCountry)')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/message', methods=['POST'])
def post_trade_message():
    request_data = request.get_json()
    new_message = {
        "userId": request_data['userId'],
        "currencyFrom": request_data['currencyFrom'],
        "currencyTo": request_data['currencyTo'],
        "amountSell": request_data['amountSell'],
        "amountBuy": request_data['amountBuy'],
        "rate": request_data['rate'],
        "timePlaced" : request_data['timePlaced'],
        "originatingCountry" : request_data['originatingCountry']
    }
    sql = ('INSERT INTO transactions(userId,currencyFrom,currencyTo,amountSell,amountBuy,rate,timePlaced,originatingCountry ) '
           'VALUES(:userId, :currencyFrom, :currencyTo, :amountSell, :amountBuy, :rate, :timePlaced, :originatingCountry)')

    conn = get_db();
    cursor = conn.cursor()
    cursor.execute(sql, new_message)
    conn.commit()

    return jsonify(new_message)

@app.route('/message')
def get_trade_messages():
    keys = ["userId","currencyFrom","currencyTo","amountSell","amountBuy","rate","timePlaced","originatingCountry"]
    conn = get_db()
    cursor = conn.cursor()
    trade_messages = []
    for row in cursor.execute('SELECT * FROM transactions'):
        trade_messages.append(dict(zip(keys, row)))
    return jsonify({'trade_messages': trade_messages})


@app.route('/graph')
def display_graph():
    return render_template('graph.html')

@app.route('/graph-data')
def graph_data():
    conn = get_db()
    cursor = conn.cursor()
    chart_data = []
    for row in cursor.execute("SELECT priceDate, price FROM history WHERE currency='GBP' order by priceDate DESC limit 200"):
        chart_data.append([row[0], float(row[1])])

    chart_data.reverse()
    return jsonify({'chart_data': chart_data})

if __name__ == '__main__':
    app.run(port=5000)
