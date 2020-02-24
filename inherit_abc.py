from abc import *


class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Создан новый SchoolMember: {self.name}')

    @abstractmethod
    def tell(self):
        '''Вывести информацию'''
        print(f'Name: {self.name}; Age: {self.age}', end=' 8===o ')


class Teacher(SchoolMember):
    '''Представляет проподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f'Создан новый Teacher: {self.name}')

    def tell(self):
        SchoolMember.tell(self)
        print(f'Salary: {self.salary}')


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f'Создан новый Student: {self.name}')

    def tell(self):
        SchoolMember.tell(self)
        print(f'Marks: {self.marks}')


t = Teacher('Mr.Rick', 60, 10000000)
s = Student('Morty', 13, 123)

print(30*'*')
members = [t, s]
for m in members:
    m.tell()