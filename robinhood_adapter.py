python
from adapters.base_adapter import BaseBrokerAdapter

class RobinhoodAdapter(BaseBrokerAdapter):
    def place_order(self, symbol, action, qty):
        print(f"Robinhood → {action} {qty} adet {symbol} işlemi gönderildi.")
        # Gerçek API entegrasyonu burada yapılacak