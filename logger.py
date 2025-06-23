import logging

def setup_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("bot.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
