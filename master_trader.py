python
from models import Subscriber
from database import db_session
from adapters.adapter_map import adapter_map

def execute_master_trade(symbol, action, master_qty):
    users = Subscriber.query.all()
    for user in users:
        qty = int(master_qty * (user.match_ratio / 100))
        if action == "BUY" and not user.allow_buy:
            continue
        if action == "SELL" and not user.allow_sell:
            continue
        if qty * 10> user.max_daily_limit:
            continue
        adapter_class = adapter_map.get(user.broker)
        if adapter_class:
            adapter = adapter_class(user.api_key)
            adapter.place_order(symbol, action, qty)