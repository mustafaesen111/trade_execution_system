python
class BaseBrokerAdapter:
    def __init__(self, api_key):
        self.api_key = api_key

    def place_order(self, symbol, action, qty):
        raise NotImplementedError("Bu method alt sınıfta tanımlanmalı.")