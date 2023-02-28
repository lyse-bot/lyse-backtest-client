from typing import Optional

from strategy_brain.klines import Klines
from strategy_imports import *


class Strategy:
    def __init__(self):
        super().__init__()
        self.data = MandatoryData.set(
            pair="ETHUSDT",
            timeline=Timeline.MINUTE_15,
            indicators=[
                Indicator("CCI", "CCI", ["high", "low", "close"], timeperiod=50),
                Indicator("RSI", "RSI", ["close"], timeperiod=14),
            ],
            leverage=2,
            ratio=1,
            strategy_name="StevenCohen",
        )

    @staticmethod
    def run(klines: Klines) -> Optional[Position]:
        cci = klines.All.iloc[-1]["CCI"]
        rsi = klines.All.iloc[-1]["RSI"]

        if cci < -50 and rsi < 30:
            return Position.long([TakeProfit.set(2, 1)], StopLoss.set(1.8))
        elif cci > 50 and rsi > 70:
            return Position.short([TakeProfit.set(2, 1)], StopLoss.set(1.8))
        return None
