def calculate():

    while True:
        total = float(input("Enter the total bill amount: "))
        amount = float(input("Enter the amount paid by the customer: "))

        if amount < total:
            amount = total - amount
            print("The customer still owes: $",amount)
                
        if amount > total:
            change = amount - total
            print("Bill paid in full. Return change: $",change)
                
        if amount == total:
            print("Bill paid in full. No balance due.")
        else:
            print(str("Error: Please enter a valid numerical amount."))
calculate()