class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, class_name, year):
        super().__init__(fname, lname)
        self.class_name = class_name
        self.graduationyear = year

    def printname(self):
        super().printname()
        print(self.class_name)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


class Teacher(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject


p1 = Student("Jessica", "Larsson", "BI20", 2020)
p2 = Student("Kalle", "Andersson", "WEBB20", 2021)

p1.welcome()
p2.welcome()

t1 = Teacher("Mikael", "Olsson", "Python")

t1.printname()
