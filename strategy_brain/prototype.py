from typing import Union

from pydantic import BaseModel

from strategy_brain.klines import Indicator
from strategy_brain.order import Position


class Strategy:
    def __init__(self):
        super().__init__()
        self.data: MandatoryData = MandatoryData()

    def run(self, klines) -> Position:
        pass


class MandatoryData(BaseModel):
    pair: str
    timeline: str
    indicators: Union[None, Indicator, list[Indicator]]
    leverage: int
    ratio: float
    strategy_name: str = ""

    @classmethod
    def set(
        cls,
        pair: str,
        timeline: str,
        indicators: Union[None, Indicator, list[Indicator]],
        leverage: int,
        ratio: Union[int, float],
        strategy_name: str = "",
    ):
        pass
