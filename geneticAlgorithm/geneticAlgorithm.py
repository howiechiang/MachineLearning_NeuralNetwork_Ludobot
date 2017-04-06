from population import POPULATION
from pyrosim import PYROSIM
from robot import ROBOT
from minimalRobot import MINIMAL_ROBOT
from individual import INDIVIDUAL
import constants as c
from core01_HillClimber import *

import matplotlib.pyplot as plt
import copy as cp
import sys
import pickle
import random


fits = []

# for i in range(0,100):
#
#     child = cp.deepcopy(parent)
#     child.Mutate()
#
#     parent.Evaluate(hideSim=True)
#     child.Evaluate(hideSim=True)
#
#     print("[g: ", i, "] [PW: ", parent.genome," ][P: ", parent.fitness, "] [C:", child.fitness, "]")
#     fits.append(parent.fitness)
#
#     if (child.fitness > parent.fitness):
#         parent = child
#         f = open("robot.p", "wb")
#         pickle.dump(parent, f)
#         f.close()
# parent.Evaluate(hideSim=False, startPaused=True)




# Make a population
parents = POPULATION( 10 )
parents.Initialize()
parents.Evaluate( startPaused=False )
parents.Print()

for g in range(0, 200):

    children = POPULATION( 10 )
    children.FillFrom(parents)
    parents.ReplaceWith(children)
    parents.Evaluate()

    print(g, end=' ')
    children.Print()


#     # Make a copy and evaluate them
#     children = cp.deepcopy( parents )
#     children.Mutate()
#     children.Evaluate( hideSim=True, startPaused=False )
#
#     parents.ReplaceWith( children )
#     parents.Evaluate( startPaused=False )
#
#     print(g, end=' ')
#     parents.Print()
#
parents.Evaluate( hideSim=False, startPaused=True )

###### Data Visualization ######
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
# plt.plot(fits)
# plt.show()