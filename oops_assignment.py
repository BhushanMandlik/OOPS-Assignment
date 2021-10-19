class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name of person {} and age is {}".format(self.name, self.age))

class Student(Person):
    def __init__(self, student_name, age, section):
        super().__init__(student_name, age)
        self.section = section

    def displayStudent(self):
        print("Name of Student {}, age is {} and he/she from {} section".format(self.name, self.age, self.section))

# Base Class object
std1 = Person("Rajesh Mehata", "25")
std1.display()
print()

# Derived Class object
std2 = Student("Bhushan Mandlik", "21", "CSE")
std2.display()
std2.displayStudent()