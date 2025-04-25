#single-level
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle):  # Single level inheritance
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def __str__(self):
        return super().__str__() + f", Fuel Type: {self.fuel_type}"


# Main program
if __name__ == "__main__":
    print("=== Single Level Inheritance ===")
    my_car = Car("Toyota", "Camry", "Petrol")
    print(my_car)

#multi-level
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):  # First level of inheritance
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.department = department

    def __str__(self):
        return super().__str__() + f", Emp ID: {self.emp_id}, Department: {self.department}"


class Manager(Employee):  # Second level of inheritance (multilevel)
    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department)
        self.team_size = team_size

    def __str__(self):
        return super().__str__() + f", Team Size: {self.team_size}"


# Main program
if __name__ == "__main__":
    print("\n=== Multilevel Inheritance ===")
    mgr = Manager("Alice", 35, "M102", "IT", 8)
    print(mgr)
