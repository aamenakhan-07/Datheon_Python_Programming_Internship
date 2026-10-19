
import csv
from datetime import datetime

# Sample market prices (not live stock prices)
market_prices = {
    "AAPL": 230.00,
    "MSFT": 510.00,
    "GOOGL": 250.00,
    "AMZN": 220.00,
    "TSLA": 440.00
}

portfolio = {}

print("=" * 45)
print("     STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 45)

while True:
    ticker = input(
        "\nEnter stock ticker (or DONE to finish): "
    ).strip().upper()

    if ticker == "DONE":
        break

    if ticker not in market_prices:
        print("Ticker not available in sample prices.")
        print("Available tickers:", ", ".join(market_prices))
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
        print("Please enter a valid numeric price and quantity.")

if not portfolio:
    print("\nNo stocks entered. Exiting program.")

else:
    total_invested = 0
    total_market_value = 0
    results = []

    print("\n" + "=" * 85)
    print("PORTFOLIO PERFORMANCE SUMMARY")
    print("=" * 85)

    print(
        f"{'Ticker':<10}{'Quantity':>10}"
        f"{'Buy Price':>13}{'Market Price':>15}"
        f"{'Market Value':>16}{'Gain/Loss':>15}"
    )

    for ticker, details in portfolio.items():
        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = market_prices[ticker]

        invested = buy_price * quantity
        market_value = current_price * quantity
        gain_loss = market_value - invested
        percentage = (gain_loss / invested) * 100

        total_invested += invested
        total_market_value += market_value

        print(
            f"{ticker:<10}{quantity:>10}"
            f"{buy_price:>13.2f}{current_price:>15.2f}"
            f"{market_value:>16.2f}{gain_loss:>15.2f}"
        )

        results.append({
            "Date_Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "Ticker": ticker,
            "Quantity": quantity,
            "Buy_Price": buy_price,
            "Current_Price": current_price,
            "Invested_Amount": invested,
            "Market_Value": market_value,
            "Gain_Loss": gain_loss,
            "Gain_Loss_Percentage": round(percentage, 2)
        })

    total_gain_loss = total_market_value - total_invested
    total_percentage = (
        total_gain_loss / total_invested
    ) * 100

    print("-" * 85)
    print(f"Total Invested:      {total_invested:.2f}")
    print(f"Current Value:       {total_market_value:.2f}")
    print(f"Total Gain/Loss:     {total_gain_loss:.2f}")
    print(f"Overall Return:      {total_percentage:.2f}%")
    print("=" * 85)

    # Save the portfolio summary to CSV
    filename = "portfolio_summary.csv"

    with open(filename, "w", newline="") as file:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nPortfolio summary saved to {filename}")
