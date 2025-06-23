from bot import BasicBot

def get_user_input():
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Buy or Sell: ").upper()
    order_type = input("Order type (MARKET or LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None
    if order_type == "LIMIT":
        price = input("Price: ")
    return symbol, side, order_type, quantity, price

def main():
    bot = BasicBot()
    symbol, side, order_type, quantity, price = get_user_input()
    result = bot.place_order(symbol, side, order_type, quantity, price)
    print("Order Result:\n", result)

if __name__ == "__main__":
    main()
