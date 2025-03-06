import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Error fetching exchange rates")
        return None
    
    rates = data.get("rates", {})
    return rates.get(target_currency, None)

def currency_converter():
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input("Enter amount: "))
    
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Invalid currency code or unable to fetch exchange rate.")

if __name__ == "__main__":
    currency_converter()
