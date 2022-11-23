# MRO - порядок разрешения методов

# staticmethod and classmethod, isinstance method

from datetime import datetime


class Person:
    it_major = ["pm", "devops", "tester", "developer", "analyst", "ux-ui designer"]

    spec = "Programmer"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_object(cls, name, year):
        now_date = datetime.now().year
        age = now_date - year
        return cls(name, age)

    @classmethod
    def get_object_with_cls(cls, list_object_person):
        for i in list_object_person:
            if isinstance(i, cls):
                print(i.name)
                print(i.age)


def get_person(self):
        print(f"{self.name} {self.age}")


nazgul = Person.create_object("nazgul", 1996)
print(nazgul.age)


# Задача

# класс Student в конструкторе он принимает  name, group, age,
# course, написать  classmethod который принимает
# type dict {name: "askdja", "group": "sadkas, "year": 1234, entrance_year: asdjad}
# и возвращает новый объект от класса Student и если

# class Student:
#     def __init__(self, name: str, age: int,
#                  group: int, course: int, entrance_year: int, is_bachelor=None, ):
#         self.name = name
#         self.age = age
#         self.group = group
#         self.course = course
#         self.is_bachelor =
#         self.is_magistry = False
#         self.is_ended_highschool = False
#         self.entrance_year = entrance_year
#
#     def create_dict_for_instance(self):
#         student_data_dict = {
#             "name": self.name,
#             "age": self.age,
#             "group": self.age,
#             "entrance_year": self.entrance_year
#         }
#         return student_data_dict
#
#     @classmethod
#     def create_new_student(cls, student_info: dict):
#         if datetime.now().year - student_info["entrance_year"] <= 4:


class Student:
    now_year = datetime.now().year

    def __init__(self, name: str, group: str, age: int, course: int) -> None:
        self.name = name
        self.age = age
        self.group = group
        self.course = course

    @classmethod
    def create_object(cls, dict_: dict):
        year = dict_.pop('year')
        year_add_vuz = dict_.pop('year_add_vuz')
        dict_.update({
            "age": cls.now_year - year,
            "course": cls.now_year - year_add_vuz
        })
        return cls(**dict_)

    def get_info(self):
        print(self.name, self.age, self.group, self.course)

    @staticmethod
    def get_vuz_add_year(obj, course):
        now_year = datetime.now().year
        return now_year - course


arsen = {
    "name": "Arsen",
    "group": "Python3",
    "year": 2005,
    "year_add_vuz": 2021
}

ars = Student.create_object(arsen)
ars.get_info()






