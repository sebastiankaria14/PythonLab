class Student:
    def __init__(self, name="Unknown", roll=0, course="Undeclared"):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print(f" Name: {self.name}")
        print(f" Roll No: {self.roll}")
        print(f" Course: {self.course}")
        print("-" * 30)

# Object using DEFAULT constructor
print(" Creating object with default constructor:\n")
student1 = Student()
student1.display()

# Object using PARAMETERIZED constructor
print(" Creating object with parameterized constructor:\n")
student2 = Student("Parth", 101, "Computer Science")
student2.display()

