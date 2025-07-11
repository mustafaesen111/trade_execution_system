python
from adapters.base_adapter import BaseBrokerAdapter

class FidelityAdapter(BaseBrokerAdapter):
    def place_order(self, symbol, action, qty):
        print(f"Fidelity → {action} {qty} adet {symbol} işlemi gönderildi.")
        # Burada Fidelity API bağlantısı kurulabilir (gerçek sistemde)