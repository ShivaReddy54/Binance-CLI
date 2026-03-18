import argparse
import logging

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        # Print request summary
        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price    : {args.price}")

        client = BinanceClient().get_client()

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Print response
        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Order Failed: {str(e)}")
        logging.error("CLI Error: %s", str(e))


if __name__ == "__main__":
    main()