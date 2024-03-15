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
        if self.lifes == self.__lifesLimit:
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

obj = Cat()

def cat_life(obj: object):
    obj.catch(); print(obj); obj.eat(); print(obj); obj.sleep(50); print(obj)

cat_life(obj)

"""17. Телевізор. Розробити клас, що моделює телевізор. Телевізор може вмикатися/вимикатися,
переключати канали. Написати програму, що демонструє «використання» телевізору (власник
інтерактивно керує пристроєм)."""

class TV:

    def __init__(self, endChannel, startChannel = 1) -> None:
        self.__power = False
        self.__startChannel = startChannel
        self.__endChannel = endChannel
        self.__currentChannel = startChannel

    def __str__(self) -> str:
        return f"Current channel: {self.currentChannel}"
    
    @property
    def currentChannel(self):
        return self.__currentChannel
    
    @property
    def startChannel(self):
        return self.__startChannel
    
    @property
    def endChannel(self):
        return self.__endChannel

    @property
    def power(self):
        return self.__power

    def switch(self):
        self.__power = not self.__power

    def changeUP(self):
        if self.currentChannel == self.__endChannel:
            self.__currentChannel = self.__startChannel
        else:
            self.__currentChannel +=1

    def changeDOWN(self):
        if self.currentChannel == self.__startChannel:
            self.__currentChannel = self.__endChannel
        else:
            self.__currentChannel -=1
    
    @currentChannel.setter
    def currentChannel(self, number):
        self.__currentChannel = number

p = TV(10)

def intereactive(obj: object):
    
    obj.switch()
    while obj.power != False:
        inp = int(input("1 - channelUP, 2 - channelDOWN, 3 - selectChannel, 4 - switch: "))
        if inp == 1: obj.changeUP()
        elif inp == 2: obj.changeDOWN()
        elif inp == 3:
            number = int(input(f'Select your channel ({obj.startChannel} - {obj.endChannel}): '))
            obj.currentChannel = number
        elif inp == 4: obj.switch()

        print(obj)

intereactive(p)