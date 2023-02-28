import base64
import datetime
import time
from getpass import getpass

import requests

HOST = "http://127.0.0.1:8000"
STRATEGY_NAME = "StevenCohen"
STRATEGY_FILE = "strategy.py"
START_TIME = datetime.date(2023, 1, 28)
END_TIME = datetime.date.today()


def load_strategy() -> str:
    file = open(STRATEGY_FILE, "r")
    content = file.read()
    file.close()
    return content


def get_authorization():
    username = input("Username: ")
    password = getpass(prompt="Password: ", stream=None)
    return (base64.b64encode((username + ":" + password).encode())).decode()


def run():
    result = requests.post(
        HOST + "/backtest/run",
        headers={"Authorization": get_authorization()},
        json={
            "start_time": (time.mktime(START_TIME.timetuple())),
            "end_time": (time.mktime(END_TIME.timetuple())),
            "name": STRATEGY_NAME,
            "content": content,
        },
    )
    if result.status_code == 200:
        result = result.json()["result"]
        print(result)
    else:
        print(result.text)


if __name__ == "__main__":
    content = load_strategy()
    run()
