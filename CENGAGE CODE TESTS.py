def calculate_interest(balance, rate):
    return balance * rate / 12

def generate_payment_schedule(purchase_price):
    down_payment = purchase_price * 0.10
    balance = purchase_price - down_payment
    monthly_payment = balance * 0.05

    print("Payment Schedule")
    print("Month\tTotal Balance\tInterest\tPrincipal\tPayment\tRemaining Balance")

    month = 1
    while balance > 0:
        interest = calculate_interest(balance, 0.12)
        principal = monthly_payment - interest if monthly_payment > interest else balance
        remaining_balance = balance - principal

        print(f"{month}\t{balance:.2f}\t\t{interest:.2f}\t\t{principal:.2f}\t\t{monthly_payment:.2f}\t\t{remaining_balance:.2f}")

        balance = remaining_balance
        month += 1

purchase_price = float(input("Enter the purchase price: "))
generate_payment_schedule(purchase_price)