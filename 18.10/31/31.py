class User:
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Student(User):
    def set_name(self, name):
        if len(name) > 0:
            self.name = name
        else:
            raise Exception('Student name error')

class Employee(User):
    def set_age(self, age):
        if age > 18 and age < 65:
            self.age = age
        else:
            raise Exception('Age out of range')
    def get_age(self):
        return self.age