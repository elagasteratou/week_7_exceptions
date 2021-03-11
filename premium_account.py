from account import Account


class PremiumAccount(Account):
    def __init__(self, name, initial, withdrawal_fee, interest):
        Account.__init__(self, name, initial, withdrawal_fee)
        self.interest = interest
        self.withdrawals = 0

    def make_withdrawal(self, amount):
        self._balance -= amount
        self.withdrawals += 1
        if self.withdrawals > 3:
            self._balance -= int(self.withdrawal_fee)

    def make_deposit_get_interest(self, amount):
        self._balance += amount
        if amount < 1000:
            self._balance += amount*self.interest
        else:
            self._balance += 1000*self.interest


if __name__ == "__main__":
    Michelle = PremiumAccount("Michelle", 10000, 3, 0.05)
    print(Michelle)
