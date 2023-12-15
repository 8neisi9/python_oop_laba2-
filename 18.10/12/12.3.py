class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.salary)
user = Employee('GABE', 3600)
user.show()