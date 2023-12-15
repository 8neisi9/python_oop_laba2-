class Employee:
    company = "Industries Co."
    status = None
    task = None
user = Employee
user.status = "Waiting"
user.task = "Programming"
print(f'Работник компании {user.company} решил выполнить своё задание "{user.task}", но сейчас он {user.status}')