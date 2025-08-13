# Assume the user has 5000 PKR in their bank account.
# Ask the user for a withdrawal amount.
# Use nested if/else to check:
# If the amount is greater than balance, print "Insufficient funds"
# If the amount is less than or equal to balance, allow withdrawal and print new balance
# If the amount is not a multiple of 500, print "Enter an amount in multiples of 500"
# Ensure the balance updates after a successful withdrawal.

balance = 5000
withdrawal_amount = int(input("Enter a withdrawal amount: "))

if withdrawal_amount > balance:
    print("Insufficient funds")
else:
    if withdrawal_amount % 500 != 0:
        print("Enter an amount in multiples of 500")
    else:
        balance = balance - withdrawal_amount
        print("Withdrawal successful. Your new balance is" + balance + "PKR.")