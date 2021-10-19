class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name of person {} and age is {}".format(self.name, self.age))

class Student(Person):
    def displayStudent(self):
        print("Name of Student {} and age is {}".format(self.name, self.age))

# Base Class object
std1 = Person("Rajesh Mehata", "25")
std1.display()
print()

# Derived Class object
std2 = Student("Bhushan Mandlik", "20")
std2.display()
std2.displayStudent()