from pydantic import BaseModel

from retrieve_data.call_klines import call_klines
from binance import Client
import talib as ta
import pandas as pd


def get_klines(pair, start, end, timeline):
    return call_klines(pair, timeline, start=start, end=end)


class Timeline:
    MINUTE_1 = Client.KLINE_INTERVAL_1MINUTE
    MINUTE_3 = Client.KLINE_INTERVAL_3MINUTE
    MINUTE_5 = Client.KLINE_INTERVAL_5MINUTE
    MINUTE_15 = Client.KLINE_INTERVAL_15MINUTE
    MINUTE_30 = Client.KLINE_INTERVAL_30MINUTE
    HOUR_1 = Client.KLINE_INTERVAL_1HOUR
    HOUR_2 = Client.KLINE_INTERVAL_2HOUR
    HOUR_4 = Client.KLINE_INTERVAL_4HOUR
    HOUR_6 = Client.KLINE_INTERVAL_6HOUR
    HOUR_8 = Client.KLINE_INTERVAL_8HOUR
    HOUR_12 = Client.KLINE_INTERVAL_12HOUR
    DAY_1 = Client.KLINE_INTERVAL_1DAY
    DAY_3 = Client.KLINE_INTERVAL_3DAY
    WEEK_1 = Client.KLINE_INTERVAL_1WEEK


class Indicator:
    def __init__(self, name: str, function: str, **kwargs):
        self.function = getattr(ta, function)
        self.name = name
        self.options = kwargs

    def get_values(self, chart: pd.DataFrame):
        return self.function(chart["close"], **self.options)
