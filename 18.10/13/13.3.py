class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def show(self):
        print(self.__name, self.__salary, self.__age)


user = Employee('GABE', 3600, 25)
user.show()