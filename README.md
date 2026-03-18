# Binance Futures Testnet Trading Bot

A lightweight, modular **CLI-based trading bot** built in Python to place orders on **Binance Futures Testnet (USDT-M)**.

---

## 📌 Features

* ✅ Place **MARKET** orders
* ✅ Place **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ Clean **CLI interface** using argparse
* ✅ Structured, modular codebase
* ✅ Logging of API requests, responses, and errors
* ✅ Input validation and robust error handling

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance API client
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
├── .env.example
├── logs/
│   └── app.log
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShivaReddy54/Binance-CLI.git
cd training-bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

#### 🪟 Windows:

```bash
venv\Scripts\activate
```

#### 🍎 Mac/Linux:

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Setup Environment Variables

Create `.env` file:

```bash
cp .env.example .env
```

Add your Binance Testnet credentials:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## ▶️ Usage

---

### ✅ Place MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

### ✅ Place LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
```

---

## 🧾 Sample Output

```
===== ORDER REQUEST =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.01

===== ORDER RESPONSE =====
Order ID      : 12345
Status        : FILLED
Executed Qty  : 0.01
Avg Price     : 60000

✅ Order placed successfully
```

---

## 🧪 Logging

All logs are stored in:

```
logs/app.log
```

### Logs include:

* 📤 API request details
* 📥 API response data
* ❌ Errors and exceptions

---

## ⚠️ Notes / Assumptions

* Only **USDT trading pairs** are supported (e.g., BTCUSDT)
* Uses **Binance Futures Testnet** (not live trading)
* Requires valid API credentials

---

## 🧹 Deactivate & Delete Virtual Environment

### Deactivate venv:

```bash
deactivate
```

---

### Delete venv:

#### 🪟 Windows:

```bash
rmdir /s /q venv
```

---

## 📦 Requirements

* Python 3.8+
* python-binance
* python-dotenv




