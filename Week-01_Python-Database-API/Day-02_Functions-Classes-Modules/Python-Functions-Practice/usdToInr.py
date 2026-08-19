def convertUsdToInr(usd_amount, exchange_rate=95.99):
    if usd_amount < 0:
        raise ValueError("USD amount cannot be negative.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be positive.")

    inr_amount = usd_amount * exchange_rate
    return inr_amount

usd_amount = float(input("Enter the amount in USD: "))

inr_amount = convertUsdToInr(usd_amount)
print(f"{usd_amount} USD is equal to {inr_amount:.2f} INR.")
