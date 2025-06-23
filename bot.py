from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL  # Set testnet URL
        self.client.API_URL = BASE_URL

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                logger.error(f"Unsupported order type: {order_type}")
                return None
            logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            return None
