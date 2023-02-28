from typing import List

import pandas as pd
import talib as ta
from binance import Client
from pydantic import BaseModel
from retrieve_data.call_klines import call_klines


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
    def __init__(self, name: str, function: str, data: List = ["open"], **kwargs):
        self.function = getattr(ta, function)
        self.name = name
        self.data = data
        self.options = kwargs


class Klines(BaseModel):
    Start: pd.Series
    Open: pd.Series
    High: pd.Series
    Low: pd.Series
    Close: pd.Series
    Volume: pd.Series
    End: pd.Series
    All: pd.DataFrame

    def indicator(self, indicator: str) -> pd.Series:
        if indicator not in self.All.columns:
            raise NameError("Given indicator name seems to not exist in klines.")
        return self.All.loc[:, indicator]
