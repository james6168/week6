# Наследование и множественное наследование

# Повторение
# class Car:
#     def __init__(self):
#         self.__price = 3000
#
#     @property
#     def money(self):
#         return self.__price
#
#     @money.setter
#     def set_money(self, new_money):
#         self.__price = new_money
#
#
# car1 = Car()
# print(car1.money)
# car1.set_money = 100
# print(car1.money)

# ==============

# class Counter:
#     def __init__(self):
#         self.value = 0
#
#     def increment(self):
#         self.value += 1
#         print(self.value)
#
#     def decrement(self):
#         self.value -= 1
#
#
# counter = Counter()
# counter.increment()
#
#
# class DoubleCounter(Counter):
#
#     def increment(self):
#         super().increment()
#         super().increment()
#
#     def decrement(self):
#         self.value -= 2
#
#     def set_zero(self):
#         self.value = 0
#
#     pass
#
#
# dcounter = DoubleCounter()
# dcounter.decrement()
# print(dcounter.value)


class Doctor:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def heal(self):
        print(f"{self.name} лечит!")

    def add_exp(self, year):
        self.experience += year

    def get_info(self):
        return f"{self.name}, {self.age}, {self.experience}"


class C:
    pass


class B(C):
    pass


class Stom(Doctor, B):
    def __init__(self, spec):
        self.spec = spec


class Orthodent(Stom, Doctor):
    def __init__(self, name, age, experience, salary, spec):
        # super().__init__(self, name, age, experience)
        Doctor.__init__(self, name, age, experience)
        Stom.__init__(self, spec)
        self.salary = salary

    def get_info(self):
        all_info = Doctor.get_info(self) + f"{self.spec} {self.salary}"
        print(all_info)


b = Doctor("Nurlan", 18, 3)
b.get_info()
a = Orthodent("naz", 23, 4, "brecet", 100000)
a.get_info()


# class DaughterTuple(tuple):
#
#     def append(self, element_to_be_added):
#         new_tuple_list = list(self)
#         new_tuple_list.append(element_to_be_added)
#         return tuple(new_tuple_list)
#
#
#
# some_daughter_tuple = DaughterTuple((1, 5))
# print(some_daughter_tuple.append("Fuck you"))
print(Orthodent.__mro__)



