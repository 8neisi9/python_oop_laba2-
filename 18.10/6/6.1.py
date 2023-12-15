class Employee:
    company = "Industries Co."
    status = None
    task = None
    def test_show(self, name, salary):
        return name + ' ' + salary


user = Employee
user.salary = 3600
user.name = "GABE"

print(user.name, user.salary)