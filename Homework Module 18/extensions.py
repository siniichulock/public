import requests
import json
from config import keys

class APIExeption(Exception):
    pass

class CashConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote.lower() == base.lower():
            raise APIExeption("Введена одна и та же валюта")

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIExeption(f"Валюта {quote} мне не знакома")

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIExeption(f"Валюта {base} мне не знакома")

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption("Некорректный ввод суммы")



        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}")
        total_base = json.loads(r.content)[keys[quote]]
        total_price = total_base * float(amount)
        return total_price