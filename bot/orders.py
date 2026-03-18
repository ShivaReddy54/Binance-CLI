import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info("Placing order: %s %s %s %s %s", symbol, side, order_type, quantity, price)

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info("API Response: %s", response)
        return response

    except Exception as e:
        logging.error("Order failed: %s", str(e))
        raise