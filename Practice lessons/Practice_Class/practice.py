class Point:

    __delta = 10

    def __init__(self, x, y) -> None:
        self.__x = x+self.__delta
        self.__y = y+self.__delta

    def __repr__(self) -> str:
        return f'x = {self.__x - self.__delta}, y = {self.__y - self.__delta}'
        
    def __str__(self) -> str:
        return f"Point (x = {self.x}, y = {self.y})"

    @property  #Декоратор, щоб прибрати потребу ставити дужки при виклику
    def x(self):
        return self.__x-self.__delta
    
    @property
    def y(self):
        return self.__y-self.__delta
    
    @x.setter #Тепер можна прибрати 'set_' в назві методу; тепер можна "напряму" змінювати змінну, але насправді використовується цей метод
    def x(self, value):
        self.__x = value + self.__delta
        return value
    @y.setter
    def y(self, value):
        self.__y = value + self.__delta
        return value

p = Point(10, 15)
p.x = 100
print(p)
print(p.x, p.y)