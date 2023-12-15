class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        salary10 = self.salary*1.1
        print(int(salary10))
user = Employee('GABE', 3600)
user.show()