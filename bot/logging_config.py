import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)