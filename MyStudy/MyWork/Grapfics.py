import matplotlib
from pylab import *
import numpy as np
import random

def GetPoints():
    point = ''
    arrange = []
    while True:
        point = input('Enter the point\n')
        if point == 'exit':
            break
        else:
            arrange.append(int(point))
    return arrange

def GetRandomPoints(count):
    point = ''
    arrange = []
    n = 0
    while n != count:
        point = random.randrange(0, 100, 1)
        arrange.append(int(point))
        n += 1
    return arrange

def AddPoints(arrange, count):
    print(f'You need add {count} point')
    point = ''
    n = 0
    while n != count:
        point = int(input('Enter the point\n'))
        arrange.append(point)
        n += 1
    return arrange

X = GetRandomPoints(10)
Y = GetRandomPoints(10)

if len(X) > len(Y):
    X = AddPoints(Y, len(X) - len(Y))
elif len(X) < len(Y):
    Y = AddPoints(X, len(Y) - len(X))

scatter(X, Y)
plot(X,Y)
show()
