import math

class Point:

    __delta = 10

    def __init__(self, x, y) -> None:
        self.__x = x+self.__delta
        self.__y = y+self.__delta

    def __repr__(self) -> str:
        return f'x = {self.__x - self.__delta}, y = {self.__y - self.__delta}'
        
    def __str__(self) -> str:
        return f"Point (x = {self.x}, y = {self.y})"

    @staticmethod
    def get_pi():
        return math.pi

    @classmethod
    def get_delta(cls):
        return cls.__delta

    @property  #Декоратор, щоб прибрати потребу ставити дужки при виклику
    def x(self):
        return self.__x-self.__delta
    
    @property
    def y(self):
        return self.__y-self.__delta
    
    @x.setter #Тепер можна "напряму" (через =) змінювати змінну, але насправді використовується цей метод
    def x(self, value):
        self.__x = value + self.__delta
        return value
    
    @y.setter
    def y(self, value):
        self.__y = value + self.__delta
        return value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other): # "lt" = "less than", "le" = "less than or equal", "gt" = "greater than" ...
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x
    
    def __le__(self, other):
        # if self.x == other.x:
        #     return self.y <= other.y
        # return self.x <= other.x

        return self == other or self < other # Іде використання методів віще "__eq__" та "__le__" тому що працюємо з обʼєктами
    
p1 = Point(10, 15)
p2 = Point(10, 15)
print(p1)
print(p2)
print(p1 <= p2)
print(p1 >= p2)