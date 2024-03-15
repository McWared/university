"""14. Кіт характеризується життєвою енергією та віком. Кіт може спати, ловити мишу, їсти, тощо (залежить
від фантазії автора класу). Під час цих процесів змінюється життєва енергія та вік кота. Якщо кіт стає
дуже старий або дуже виснажений чи навпаки отримує забагато життєвої енергії, то він уходить в
астрал. Розробити клас, що моделює котів, та написати програму, яка моделює життя деякого кота.
15. Модифікувати клас котів так, щоб кіт мав дев’ять життів і тільки після втрати останнього йшов в
астрал."""

class Cat:

    __catchEnergy = 10
    __eatEnergy = 15
    __sleepEnergy = 5

    __catchTime = 0.5
    __eatTime = 1

    __energyLimit = 200
    __ageLimit = 100
    __lifesLimit = 0

    def __init__(self) -> None:
        self.__energy = 100
        self.__age = 0
        self.__astral = False
        self.__lifes = 9

    def __str__(self) -> str:
        return f'Energy = {self.energy}, age = {self.age}, lifes = {self.lifes}, astral = {self.astral}'

    @property
    def energy(self):
        return self.__energy
    
    @property
    def age(self):
        return self.__age
    
    @property
    def astral(self):
        return self.__astral
    
    @property
    def lifes(self):
        return self.__lifes
    
    def lifeCheck(self):
        if self.energy >= self.__energyLimit or self.energy == 0:
            self.__lifes -= 1
            self.__energy = 100
            self.__age = 0
        if self.age >= self.__ageLimit:
            self.__lifes -= 1
            self.__energy = 100
            self.__age = 0

    def astralCheck(self):
        if self.lifes == 0:
            self.__astral = True
        if self.astral:
            self.__energy = 0
            print ('Cat is in astral')

    def sleep(self, time: int): #time - hours
        self.__energy += time * self.__sleepEnergy
        self.__age += time

        self.lifeCheck()
        self.astralCheck()

    def catch(self):
        self.__energy -= self.__catchEnergy
        self.__age += self.__catchTime

        self.lifeCheck()
        self.astralCheck()
        
    def eat(self):
        self.__energy += self.__eatEnergy
        self.__age += self.__eatTime

        self.lifeCheck()
        self.astralCheck()

p = Cat()
print(p)
p.eat()
print(p)
p.catch()
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)
p.sleep(200)
print(p)

