import logging

from config import Config


def setup_logging() -> None:
    logger = logging.getLogger('root')
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(module)s:%(funcName)s():%(lineno)d | %(message)s')
    console_handler = logging.StreamHandler()

    logger.setLevel(Config.LOG_LEVEL)
    console_handler.setLevel(Config.LOG_LEVEL)

    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)
