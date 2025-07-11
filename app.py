python
from flask import Flask, render_template, request, redirect
from config import Config
from database import db_session
from models import Subscriber
from master_trader import execute_master_trade

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def dashboard():
    subscribers = Subscriber.query.all()
    return render_template('dashboard.html', users=subscribers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        sub = Subscriber(
            name=request.form['name'],
            broker=request.form['broker'],
            api_key=request.form['api_key'],
            match_ratio=int(request.form['match_ratio']),
            max_daily_limit=float(request.form['limit']),
            allow_buy='buy' in request.form,
            allow_sell='sell' in request.form
)
        db_session.add(sub)
        db_session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/trigger_trade', methods=['POST'])
def trigger_trade():
    symbol = request.form['symbol']
    action = request.form['action']
    qty = int(request.form['quantity'])
    execute_master_trade(symbol, action, qty)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)