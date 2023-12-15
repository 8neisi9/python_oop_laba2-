class Employee:
    company = "Industries Co."
    status = None
    task = None
    def test_show(self):
        print(self.name)


user = Employee()
user.salary = 3600
user.name = "GABE"

user.test_show()