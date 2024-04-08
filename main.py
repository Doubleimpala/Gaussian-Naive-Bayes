import pandas as pd
import numpy as np
from random import random as rand
from random import randint
import math
import matplotlib.pyplot as matplotlib


data = pd.read_csv('data.txt',sep = ' ', header=None)
#print(data)
data = np.array(data)
x, y = data[:, 1], data[:, 2]

meanx = 
variancex = 
vx = input()
vy = input()
meany = 
variancey = 

pvgivenc_x = pgivenc(vx,variancex,meanx)
pvgivenc_y = pgivenc(vy,variancey,meany)


def pgivenc(v,variance,mean):
  return (1/(2*math.pi*variance**2))*exp((-(v-mean)**2)/(2*(variance**2)))