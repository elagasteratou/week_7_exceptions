from account import Account
import calendar


class LoanAccount(Account):
    def __init__(self, name, initial, withdrawal_fee, interest, credit_rating):
        Account.__init__(self, name, initial, withdrawal_fee)
        self.interest = interest
        self.credit_rating = credit_rating

    def get_credit_rating(self):
            print(self.name, "has a", str(self.credit_rating), "credit rating")

    # commented out because initial attribute is not being recognised
    #def get_total_amount(self):
    #    print("You will pay a total of: {}".format((-1 * int(self.initial)) + (1 + self.interest)))

    def make_payment(self, amount):
        self._balance += amount
        return

    def see_payment_schedule(self):
        print("Loan payments should be made on: ")
        for m in range(1, 13):
            cal = calendar.monthcalendar(2021, m)  # get an list of the weeks in the given months
            weekone = cal[0]
            weektwo = cal[1]  # the first thursday will fall in one of these two weeks - loop to find out which it is
            if weekone[calendar.THURSDAY] != 0:
                payment_day = weekone[calendar.THURSDAY]
            else:
                payment_day = weektwo[calendar.THURSDAY]

            print("%10s %2d" % (calendar.month_name[m], payment_day))
        return


    #def __str__(self):
    #    return "Loan Account: \nName: {}, initial: {}, credit_rating: {}".format(self.name, self.initial, self.credit_rating)


    #def __repr__(self):
    #    return f"name={self.name}, initial={self.initial}, credit_rating={self.credit_rating}"

if __name__ == "__main__":
    loan_1 = LoanAccount("Bara", -10000, 3, 0.25, "good")
    #print(loan_1)
    # TODO why does attribute initial not exist
    #print(loan_1.initial)
    print(loan_1.name)
    print(loan_1.credit_rating)
    print(loan_1.interest)
    #loan_1.get_total_amount()
    print(loan_1.credit_rating)
    loan_1.get_credit_rating()
    print(loan_1.make_payment(500))
    loan_1.get_balance()
    loan_1.see_payment_schedule()
