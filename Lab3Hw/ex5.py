class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")
s = Student("John", 20, "A")
s.displayStudent()
