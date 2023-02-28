import time
import datetime

import requests

HOST = "http://127.0.0.1:8000"
ENDPOINT = "/backtest/run"
STRATEGY_NAME = "StevenCohen"
STRATEGY_FILE = "strategy.py"
START_TIME = datetime.date(2023, 1, 28)
END_TIME = datetime.date.today()


def load_strategy() -> str:
    file = open(STRATEGY_FILE, "r")
    content = file.read()
    file.close()
    return content


def run():
    result = requests.post(HOST + ENDPOINT, json={
        "start_time": (time.mktime(START_TIME.timetuple())),
        "end_time": (time.mktime(END_TIME.timetuple())),
        "name": STRATEGY_NAME,
        "content": content
    })
    print(result.json()['result'])


if __name__ == "__main__":
    content = load_strategy()
    run()
