class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self):
        pass
    def getName(self):
        return self.__name
    def getSalary(self):
        return str(self.__salary) + '$'
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setSalary(self, salary):
        self.__salary = salary
    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            raise Exception('Incorrect')

user = Employee()
user.setName('GABE')
user.setSalary(3600)
user.setAge(25)

print(user.getName())
print(user.getSalary())
print(user.getAge())
