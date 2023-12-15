class Student:
    place = "school"
    name = None
    surname = None

    def show(self, string):
        if len(string) > 0:
            return string[0].upper() + string[1:]
        else:
            return string

pifa = Student()
pifa.name = 'pifa'
pifa.surname = 'petrov'

print(pifa.show(pifa.name))