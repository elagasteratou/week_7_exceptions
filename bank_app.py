from account import Account
from premium_account import PremiumAccount
from loan_account import LoanAccount

# instantiate a bank account object
Lisa = Account("Lisa", 500, 3)

# test bank account - object dot attribute
Lisa.see_account_number()
Lisa.make_deposit(40)
Lisa.get_balance()
Lisa.make_withdrawal(100)
Lisa.get_balance()
print(Lisa)
Lisa.see_account_number()
print("-"*20)

# instantiate a premium bank account object
Michelle = PremiumAccount("Michelle", 10000, 3, 0.05)
print(Michelle)
Michelle.see_account_number()

# test over three withdrawals and be charge withdrawal fee
Michelle.make_withdrawal(500)
print(Michelle)
Michelle.make_withdrawal(500)
print(Michelle)
Michelle.make_withdrawal(500)
print(Michelle)
Michelle.make_withdrawal(500)
print(Michelle)

# test deposit with interest in premium account
Michelle.make_deposit(1000)
print(Michelle)
print("-"*20)

# test loan account methods
loan_1 = LoanAccount("Bara", -10000, 3, 0.25, "good")
loan_1.see_account_number()
#print(loan_1.get_total_amount())
print(loan_1.credit_rating)
loan_1.get_credit_rating()
print(loan_1.make_payment(500))
loan_1.get_balance()
loan_1.see_payment_schedule()
print("-"*20)

# test number of accounts created
print("Number of accounts created:", Account.number_created)
