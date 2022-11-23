# dunder methods
# equal
# multiple
#division

class Point:

    # def __new__(cls, *args, **kwargs):
    #     cls.new_attr = kwargs.get("new_attr", 4)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("init")

    def __str__(self):
        return f"object x = {self.x}, y = {self.y}"

    def __add__(self, other):
        if isinstance(other, Point):
            result = self.x * self.y + other.x * other.y
            return result
        elif isinstance(other, str):
            result = str(self) + f" {other}"
            return result
        elif isinstance(other, int):
            result = (self.x + self.y) * other
            return result


obj_1 = Point(6, 3)
obj_2 = Point(9, 3)

print(obj_1 + obj_2)

# Д/з определить метод Division __div__ для чисел строк и объектов
