import pandas
import json
import requests


class StockNews:
    def __init__(self, stock, alpha_key, news_key):
        self.alpha_api = "https://www.alphavantage.co/query"
        self.stock = stock  # nome da ação
        self.alpha_key = alpha_key
        self.news_api = "https://newsapi.org/v2/top-headlines"
        self.news_api_key = news_key

    def alpha_parameters(self: int) -> dict:  # parametros da api
        alpha_parameters = {

            "function": "TIME_SERIES_INTRADAY",
            "symbol": self.alpha_stock,
            "interval": "60min",
            "apikey": self.alpha_key

        }
        return alpha_parameters

    def request_alpha(self) -> json:
        alpha = requests.get(self.alpha_api, params=self.alpha_parameters())
        print(alpha.raise_for_status())
        return alpha.json()

    def news_parameters(self) -> dict:
        new_parameters = {

            "q": self.stock,
            "sortBy": "popularity",
            "apiKey": self.news_api_key

        }
        return new_parameters

    def request_new(self) -> json:
        new = requests.get(self.news_api, params=self.news_parameters())
        return new.json()

    def to_csv(self):
        data_alpha = pandas.DataFrame(self.request_alpha())
        with open('new.exe', 'w') as txt:
            txt.write(data_alpha.to_csv())
