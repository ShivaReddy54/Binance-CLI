def validate_symbol(symbol: str):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs supported (e.g., BTCUSDT)")


def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(order_type: str, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")