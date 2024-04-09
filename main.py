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
classes = data[:, 0]
classArray = np.array(classes)
meanx = np.mean(x)
variancex = np.std(x)**2
print('Input x')
vx = input()
print('Input y')
vy = input()
meany = np.mean(y)
variancey = np.std(y)**2
classProbs = computeClassProbs(vx, vy, meanx, variancex, meany, variancey, classArray)
print(classProbs)

def computeClassProbs(vx, vy, meanx, variancex, meany, variancey, classArray):
  for o in range(len(classArray)):
    indices = [i for i, x in enumerate(classArray) if x == o]
    priorProb = len(indices)/len(classArray)
    likelyhood_x = pgivenc(vx,variancex,meanx)
    likelyhood_y = pgivenc(vy,variancey,meany)
    evidenceProb_x = 1#P(Xi)
    evidenceProb_y = 1#P(Xi)
    #This is wrong. Fix.
    classProbs[o] = (priorProb)
  return classProbs

#Fix this function. I think it requires both dimensions to work? x and y?
def pgivenc(v,variance,mean):
  return (1/(2*math.pi*variance**2))*((math.e)**((-(v-mean)**2)/(2*(variance**2))))