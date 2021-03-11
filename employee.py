from person import Person
import random


class Employee(Person):
    def __init__(self, fname, lname, gender, birthdate, sector, company):
        # TODO can we inherit less attributes than superclass has?
        Person.__init__(self, fname, lname, gender, birthdate)
        self.sector = sector
        self.company = company
        self.hours = 0
        # set employee number at instantiation once - can print same number multiple times
        self.employee_number = "Your employee number is: {}".format(random.randint(1, 500))

    def get_work_hours(self, hours):
        self.hours += hours

    def get_total_hours(self):
        print(self.hours)

    @property  # defining email like a method but can access it like an attribute
    def make_email(self):
        return '{}.{}@{}.co.uk'.format(self.fname, self.lname, self.company)

    def __str__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    # TODO what does the __repr__ do?
    def __repr__(self):
        return "Employee: ('{}', '{}')".format(self.fname, self.lname)

    def __getattr__(self, fname):
        return fname + " is here!"


if __name__ == "__main__":
    worker_1 = Employee("John", "Doe", "Male", "03/01/1985", "marketing", "Loud")
    print(worker_1.make_email)
    print(worker_1.get_total_hours())
    worker_1.get_work_hours(8)
    worker_1.get_work_hours(4)
    print(worker_1.get_total_hours())

