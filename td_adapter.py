python
from adapters.base_adapter import BaseBrokerAdapter

class TDAdapter(BaseBrokerAdapter):
    def place_order(self, symbol, action, qty):
        print(f"TD Direct Investing → {action} {qty} adet {symbol} işlemi gönderildi.")
        # TD API entegrasyonu burada tanımlanabilir
