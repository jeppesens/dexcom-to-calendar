#! /usr/bin/python
from time import sleep
from datetime import datetime, timedelta

from config import Config
from utils.setup_logger import setup_logging
from put_bg_to_calendar import put_bg_to_calendar


if __name__ == '__main__':
    setup_logging()
    *map(lambda k: k.startswith('__') or getattr(Config, k), dir(Config.__class__)),
    while True:
        start = datetime.now()
        put_bg_to_calendar()
        sleep_until = start + timedelta(seconds=Config.TICK_SEC)
        sleep_for = (sleep_until - datetime.now()).total_seconds()
        if sleep_for > 0:
            sleep(sleep_for)
