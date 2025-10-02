import requests

# Function to convert currency using API
def convert_currency(amount, from_currency, to_currency):
    try:
        # Using exchangerate.host convert endpoint (reliable and free)
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)
        response.raise_for_status()  # Check for network errors
        data = response.json()
        
        # Check if conversion was successful
        if data.get('result') is not None:
            converted_amount = data['result']
            print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}\n")
        else:
            print("Conversion failed. Please check the currency codes.")
    
    except requests.exceptions.RequestException as e:
        print(f"Network or API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    print("💱 Currency Converter 💱")
    print("Valid currency codes examples: USD, EUR, INR, GBP, JPY\n")
    
    while True:
        try:
            # Take amount input
            amount_input = input("Enter amount to convert: ")
            amount = float(amount_input)  # Convert to float
            
            # Take currency inputs
            from_currency = input("From currency (e.g., USD, EUR, INR): ").upper()
            to_currency = input("To currency (e.g., USD, EUR, INR): ").upper()
            
            # Perform conversion
            convert_currency(amount, from_currency, to_currency)
            
            # Ask if user wants to convert again
            cont = input("Do you want to convert another amount? (yes/no): ").lower()
            if cont != 'yes':
                print("Program exited. Thank you!")
                break
            
        except ValueError:
            print("Invalid input! Please enter a numeric amount.\n")

if __name__ == "__main__":
    main()
