from population import POPULATION
from pyrosim import PYROSIM
from robot import ROBOT
from minimalRobot import MINIMAL_ROBOT
from individual import INDIVIDUAL
import constants as c
from core01_HillClimber import *
from environments import ENVIRONMENTS

import matplotlib.pyplot as plt
import copy as cp
import sys
import pickle
import random
import os.path

########################################################################################################################
# Script
########################################################################################################################

fits = []
envs = ENVIRONMENTS()
pickledPop = "robot.p"

###### Make a population ######
parents = POPULATION( c.popSize )
parents.Initialize()

###### Load Precursor into Population ######
if os.path.isfile(pickledPop):

    f = open(pickledPop, "rb")
    parents.Copy_Best_From(pickle.load(f))
    parents.p[0].fitness = 0
    parents.p[0].ID = 0
    f.close()

###### Print out fitness of initial parent ######
parents.Evaluate( envs, hideSim=True, startPaused=False )
parents.Print()

###### Iterate over generations ######
for g in range(0, c.numGens):

    children = POPULATION( c.popSize )
    children.FillFrom( parents )
    children.Evaluate( envs, hideSim=True, startPaused=False )
    parents.ReplaceWith( children )

    fits.append(parents.p[0].fitness)
    print(g, end=' ')
    parents.Print()


###### Visualize strongest configuration ######
for e in envs.envs:

    parents.p[0].Start_Evaluation( envs.envs[e], hideSim=False, startPaused=True )
    parents.p[0].fitness = 0
    parents.p[0].Compute_Fitness( printFit=True )

###### This pickles the best configuration ######
f = open("robot.p", "wb")

parents.Print()

parents.p[0].ID = 0
pickle.dump(parents, f)
f.close()


###### Data Visualization ######
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
plt.plot(fits)
plt.show()
