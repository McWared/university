import math
from turtle import *

def heartA (k):
    return 15 * math.sin(k) ** 3

def heartB (k):
    return 12 * math.cos(k) - 5 * \
    math.cos(2 * k) - 2 * \
    math.cos(3 * k) - \
    math.cos(4 * k)

speed(0)

bgcolor("black")
for i in range(6000):
    goto(heartA(i) * 15, heartB(i) * 15)
    for j in range(5):
        color ('#f73487')
    goto(0,0)