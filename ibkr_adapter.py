python
from adapters.base_adapter import BaseBrokerAdapter

class IBKRAdapter(BaseBrokerAdapter):
    def place_order(self, symbol, action, qty):
        print(f"IBKR → {action} {qty} adet {symbol} işlemi gönderildi.")
        # Gerçek IBKR API bağlantısı burada tanımlanabilir