class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")
