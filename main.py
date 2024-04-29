import pandas as pd
import numpy as np
from random import random as rand
from random import randint
import math
import matplotlib.pyplot as matplotlib


def main():
  data = pd.read_csv('data.txt', sep=' ', header=None)
  data = np.array(data)
  x, y = data[:, 1], data[:, 2]
  classes = data[:, 0]

  print('Input x')
  vx = float(input())
  print('Input y')
  vy = float(input())

  unique_classes = np.unique(classes)
  classProbs = np.zeros(len(unique_classes))
  ############
  
  for o, c in enumerate(unique_classes):
      indices = np.where(classes == c)[0]
      subset_x = x[indices]
      subset_y = y[indices]

      meanx = np.mean(subset_x)
      variancex = np.var(subset_x)

      meany = np.mean(subset_y)
      variancey = np.var(subset_y)

      priorProb = len(indices) / len(classes)

      likelyhood_x = pgivenc(vx, variancex, meanx)
      likelyhood_y = pgivenc(vy, variancey, meany)

      # Assuming evidence probabilities are 1 for simplicity
      evidenceProb_x = 1
      evidenceProb_y = 1
    #Article I looked at had these, but nobody else I asked had evidence probabilities. I also couldn't find how to calculate them so I just left it as 1.

      classProbs[o] = (priorProb * likelyhood_x + priorProb * likelyhood_y) / 2


  for i, g in enumerate(classProbs):
    print("\n\nclass " + str(i) + " probability:\n")
    print(g)


def pgivenc(v,variance,mean):
  return (1/(2*math.pi*variance**2))*((math.e)**((-(v-mean)**2)/(2*(variance**2))))

if __name__ == "__main__":
  main()