from person import Person
from datetime import date


class Customer(Person):
    def __init__(self, fname, lname, gender, birthdate, staff, covid_jab):
        Person.__init__(self, fname, lname, gender, birthdate)
        self.staff = staff
        self.loyalty_points = 0
        self.covid_jab = covid_jab

    def get_rewards(self, price):
        self.loyalty_points += price/10
        if self.staff == True:          # pycharm wants this statement simplified - how can we do this?
            self.loyalty_points += price/20
        print("You now have {} loyalty points to spend.".format(self.loyalty_points))

        today = date.today().strftime("%d/%m/%Y")
        if self.birthdate[:6] == today[:6]:
            print("{} will receive a complimentary birthday gift today!".format(self.fname))
        else:
            print("Sorry, wrong date. You will need to come back, on your birthday.")

    def book_jab(self):
        if self.covid_jab == True:
            print("You have already had your vaccination")
        else:
            self.covid_jab = True

    def book_trip(self):
        if self.covid_jab == True:
            print("You are permitted to book summer holiday trips abroad.")
        else:
            print("Overseas holiday vacations cannot be booked without a Covid vaccination.")

    def __str__(self):
        return "Customer \nName: {}, Surname: {}, Points: {}".format(self.fname, self.lname, self.loyalty_points)

    def __repr__(self):
        return f"fname={self.fname}, lname={self.lname}, gender={self.gender}, birthdate={self.birthdate}"


if __name__ == "__main__":
    Anna = Customer("Anna", "Smith", "Female", "09/03/1996", True, False)
    print(Anna.get_full_name())
    print(Anna.loyalty_points)
    Anna.get_rewards(250)
    print(Anna.loyalty_points)
    print(Anna.gender)
    print(Anna)
    Anna.book_trip()
    Anna.book_jab()
    Anna.book_trip()
    Anna.get_rewards(300)
