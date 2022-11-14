# Polymorphism
from random import randint


# class Triangle:
#     def __init__(self, sides_count: int = 2):
#         self.sides = {f"side_{i}": randint(1, 20) for i in range(sides_count)}
#         self.square = 0
#         self.attrs_list = 0
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def distract_square(self):
#         square = 1/2 * self.sides["side_0"] * self.sides["side_1"]
#         self.square = square
#         return self.square
#
#     def get_list_of_attrs(self) -> None:
#         print([(key, value) for key, value in self.__dict__.items()])
#
#
# class Rectangle:
#     def __init__(self, a: int, b: int) -> None:
#         self.side_a = a
#         self.side_b = b
#         self.square = 0
#
#     def get_attrs(self) -> dict:
#         print(self.__dict__)
#
#     def distract_square(self):
#         self.square = self.side_a * self.side_b
#         print(self.square)
#
#     def get_list_of_attrs(self) -> None:
#         print([(key, value) for key, value in self.__dict__.items()])
#
#
# triangle_1 = Triangle()
# triangle_2 = Triangle()
# rectangle_1 = Rectangle(12, 6)
# rectangle_2 = Rectangle(16, 4)
# lists = [triangle_2, triangle_1,
#          rectangle_1, rectangle_2]
#
# for i in lists:
#     i.get_attrs()
#     i.distract_square()
#     i.get_list_of_attrs()

# Задача 2
# class Student имеет атрибуты full_name: str, course: int, subjects: dict - пустой по умолчанию,
# total - 0 по умолчанию
# реализовать метод set_subjects(self, dict)
# subjects может меняться

# Например:
# subjects = {
# "algebra": 56,
# "python": 76
# }

# self.total должен поменяться на average = avg(self.subjects)
# 3. save_total(self) Записать в новый файл в виде:
# Tabyldieva Nazgul - 1 - total
# 4. set_course() - при каждом вызове должен увеличиться на 1, и дозаписать


class Student:

    def __init__(self, full_name: str, course: int):
        self.full_name = full_name
        self.course = course
        self.subjects = {}
        self.total = 0

    def set_subjects(self, subjects_to_set: dict):
        self.subjects = subjects_to_set

    def get_total(self):
        list_of_marks = sum(self.subjects.values()) / len(self.subjects)
        self.total = list_of_marks

    def save_total(self):
        with open(f"{self.full_name}.txt", "a") as student_data:
            student_data.write(f"\n{self.full_name} - {self.course} - {self.total}")

    def set_course(self):
        self.course += 1


tabyldieva_nazgul_1 = Student("Tabyldieva Nazgul", 1)
tabyldieva_nazgul_1.set_subjects({"python": 100, "english": 0})
tabyldieva_nazgul_1.get_total()
tabyldieva_nazgul_1.save_total()

tabyldieva_nazgul_2 = Student("Tabyldieva Nazgul", 2)
tabyldieva_nazgul_2.set_subjects({"java": 88, "german": 78})
tabyldieva_nazgul_2.get_total()
tabyldieva_nazgul_2.save_total()

