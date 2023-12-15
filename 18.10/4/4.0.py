class Employee:
    company = "Industries Co."
    status = None
    task = None

user = Employee
user.status = "Waiting"
user.task = "Programming"
user.salary = 3600
user.name = "GABE"
user.age = 25

edward = Employee
edward.status = "Working"
edward.task = "Programming"
edward.salary = 3600
edward.name = "edward"
edward.age = 33

print(f'Работник компании {user.company} решил выполнить своё задание "{user.task}", но сейчас он {user.status}. Ему {user.age} лет, его зовут {user.name} и он получает {user.salary} долларов в месяц')