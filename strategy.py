from typing import Optional
from strategy_imports import *
import pandas as pd


class Strategy:
    def __init__(self):
        super().__init__()
        self.data = MandatoryData.set(
            pair='BTCUSDT',
            timeline=Timeline.HOUR_1,
            indicators=[Indicator('RSI', 'RSI', timeperiod=14)],
            leverage=5,
            ratio=0.5,
            strategy_name='Bill Gates',
        )

    @staticmethod
    def run(klines: pd.DataFrame) -> Optional[Position]:
        rsi = klines.iloc[-1]['RSI']
        if rsi > 80:
            return Position.short(TakeProfit.set(3, 1), StopLoss.set(1.5))
        return None
