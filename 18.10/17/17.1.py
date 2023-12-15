class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self):
        pass

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        self.__age = age


user = Employee()
user.setName('GABE')
user.setSalary(3600)
user.setAge(25)

print(user.getName())
print(user.getSalary())
print(user.getAge())
