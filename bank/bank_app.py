import sys
from account import Account
from exceptions import InsufficientFunds

# instantiate a bank account object
bara = Account("bara", 500, 3)
withdraw_amount = 60

try:
    bara.make_withdrawal(withdraw_amount)
    # print(f"You have made a withdrawal {withdraw_amount}")
except InsufficientFunds:
    print("You have insufficient funds, please try again", file=sys.stderr)
else:
    print(f"You have made a withdrawal {withdraw_amount}")
finally:
    print(f"Your current balance is {bara.get_balance()}")

