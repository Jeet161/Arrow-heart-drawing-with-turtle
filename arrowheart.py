import math
from turtle import *
def hearta(k):
    return 13 * math.sin(k) ** 3
   
def heartb(k):
    return 10 * math.cos(k) - 7 * \
            math.cos(2*k) - 4* \
            math.cos(3*k) -\
            math.cos(4*k)  
            
speed(0)
bgcolor("black")
for i in range (5000):
    goto(hearta(i)*22, heartb(i)* 20)
    for j in range(1):
        color("violet")


 