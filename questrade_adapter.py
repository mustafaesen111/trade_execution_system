python
from adapters.base_adapter import BaseBrokerAdapter

class QuestradeAdapter(BaseBrokerAdapter):
    def place_order(self, symbol, action, qty):
        print(f"Questrade → {action} {qty} adet {symbol} işlemi gönderildi.")
        # Questrade API entegrasyonu burada tanımlanabilir