from pydantic import BaseModel
from typing import Union


class StopLoss(BaseModel):
    target: float

    @classmethod
    def set(cls, target: float):
        return cls(target=target)


class TakeProfit(BaseModel):
    target: float
    close_size: float

    @classmethod
    def set(cls, target: float, close_size: float):
        return cls(target=target, close_size=close_size)


class Position(BaseModel):
    side: str
    take_profit: Union[TakeProfit, list[TakeProfit]]
    stop_loss: StopLoss

    @classmethod
    def long(cls, take_profit: Union[TakeProfit, list[TakeProfit]], stop_loss: StopLoss):
       pass

    @classmethod
    def short(cls, take_profit: Union[TakeProfit, list[TakeProfit]], stop_loss: StopLoss):
        pass

    @classmethod
    def close(cls):
        pass
