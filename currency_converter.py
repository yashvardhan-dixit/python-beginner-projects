import requests

API_KEY = "ba33a61405786b1959ba5e36"  # 🔑 Replace this with your real API key
BASE_URL = f"https://v6.exchangerate-api.com/v6/ba33a61405786b1959ba5e36/latest/"

def convert_currency(base, target, amount):
    try:
        url = BASE_URL + base.upper()
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or data['result'] != 'success':
            print("❌ Failed to fetch exchange rates.")
            return

        rate = data['conversion_rates'].get(target.upper())
        if rate is None:
            print(f"❌ Invalid target currency: {target.upper()}")
            return

        converted = amount * rate
        print(f"\n💱 {amount} {base.upper()} = {converted:.2f} {target.upper()}")
    except Exception as e:
        print("⚠️ Error occurred:", e)

while True:
    print("\n🌍 Real-Time Currency Converter")
    base = input("Enter base currency (e.g., USD): ")
    target = input("Enter target currency (e.g., INR): ")
    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        continue

    convert_currency(base, target, amount)

    again = input("\n🔁 Do you want to convert another? (yes/no): ")
    if again.lower() != 'yes':
        print("👋 Exiting Currency Converter. Stay smart with your money!")
        break
