
import csv
from datetime import datetime
import yfinance as yf

portfolio = {}

print("=" * 55)
print("     STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 55)
print("Enter stock ticker symbols from your dataset.")
print("Type DONE when you have entered all stocks.")

# Take portfolio details from the user
while True:
    ticker = input(
        "\nEnter stock ticker (or DONE): "
    ).strip().upper()

    if ticker == "DONE":
        break

    if not ticker:
        print("Please enter a ticker symbol.")
        continue

    try:
        buy_price = float(input("Enter buy price per share: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

        print("Stock added successfully!")

    except ValueError:
        print("Enter a valid numeric price and quantity.")

if not portfolio:
    print("\nNo stocks entered. Program finished.")

else:
    results = []
    total_invested = 0
    total_market_value = 0

    print("\nFetching online stock prices...")
    print("Please wait.\n")

    for ticker, details in portfolio.items():
        try:
            stock = yf.Ticker(ticker)
            current_price = None

            # Try to get the latest available online quote
            try:
                price = stock.fast_info["last_price"]
                if price is not None and float(price) > 0:
                    current_price = float(price)
            except Exception:
                pass

            # If quote is unavailable, use latest closing price
            if current_price is None:
                history = stock.history(period="5d")

                if not history.empty:
                    current_price = float(
                        history["Close"].dropna().iloc[-1]
                    )

            if current_price is None or current_price <= 0:
                print(f"Could not get price for {ticker}. Skipped.")
                continue

            buy_price = details["buy_price"]
            quantity = details["quantity"]

            invested = buy_price * quantity
            market_value = current_price * quantity
            gain_loss = market_value - invested
            percentage = (gain_loss / invested) * 100

            total_invested += invested
            total_market_value += market_value

            print(f"Stock: {ticker}")
            print(f"Buy price:       {buy_price:.2f}")
            print(f"Current price:   {current_price:.2f}")
            print(f"Quantity:        {quantity}")
            print(f"Market value:    {market_value:.2f}")
            print(f"Gain/Loss:       {gain_loss:.2f}")
            print(f"Return:          {percentage:.2f}%")
            print("-" * 40)

            results.append({
                "Date_Time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Ticker": ticker,
                "Quantity": quantity,
                "Buy_Price": buy_price,
                "Current_Price": round(current_price, 2),
                "Invested_Amount": round(invested, 2),
                "Market_Value": round(market_value, 2),
                "Gain_Loss": round(gain_loss, 2),
                "Gain_Loss_Percentage": round(percentage, 2)
            })

        except Exception as error:
            print(f"Error fetching {ticker}: {error}")

    if results:
        total_gain_loss = total_market_value - total_invested
        total_percentage = (
            total_gain_loss / total_invested
        ) * 100

        print("\n" + "=" * 55)
        print("          PORTFOLIO SUMMARY")
        print("=" * 55)
        print(f"Total invested:  {total_invested:.2f}")
        print(f"Current value:   {total_market_value:.2f}")
        print(f"Total gain/loss: {total_gain_loss:.2f}")
        print(f"Overall return:  {total_percentage:.2f}%")
        print("=" * 55)

        filename = "portfolio_summary.csv"

        with open(
            filename, "w", newline="", encoding="utf-8"
        ) as file:
            fieldnames = list(results[0].keys())
            writer = csv.DictWriter(
                file, fieldnames=fieldnames
            )
            writer.writeheader()
            writer.writerows(results)

        print(f"\nCSV file saved: {filename}")
        print("The file contains your portfolio results.")

    else:
        print("\nNo stock prices could be retrieved.")
        print("Check your internet connection and ticker symbols.")
