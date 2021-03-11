class Person:
    number_created = 0

    def __init__(self, fname, lname, gender, birthdate):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.birthdate = birthdate
        Person.number_created += 1

    def get_full_name(self):
        print(self.fname, self.lname)
        return # why are the returns added at the end of each method

    def change_of_lname(self, new_name):
        self.lname = new_name
        return
    # might have the none returned because we are not storing this value?

    # could update the name using the hasattr
    # def update_fullname(self):
    #     if hasattr(self, "new_name"):
    #         full_name = self.fname , self.lname
    #         return full_name
    #     else:
    #         return self.full_name()


if __name__ == "__main__":
    p1 = Person("Nina", "Jolly", "Female", "04/05/1989")
    print(p1.get_full_name())
    p1.change_of_lname("Smith")
    print(p1.get_full_name())
    #print(p1.update_fullname())
