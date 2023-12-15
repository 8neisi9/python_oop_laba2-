class Student:
    place = "school"
    name = None
    surname = None

    def show(self, first_name, last_name):
        initials = first_name[0].upper() + last_name[0].upper()
        return initials

pifa = Student()
pifa.name = 'pifa'
pifa.surname = 'petrov'

print(pifa.show(pifa.name, pifa.surname))