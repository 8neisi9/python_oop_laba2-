class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_info(self):
        print("Имя: {}, Возраст: {}, Пол: {}".format(self.name, self.age, self.gender))
person1 = Person("Иван", 25, "Мужской")
person2 = Person("Анна", 30, "Женский")
person1.print_info()
person2.print_info()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(5, 10)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()
print("Площадь прямоугольника: ", area)
print("Периметр прямоугольника: ", perimeter)
