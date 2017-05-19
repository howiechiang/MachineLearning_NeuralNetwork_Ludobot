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
import time

########################################################################################################################
# Script
########################################################################################################################

###### Variables ######
pickledPop = "robot.p"
loadPrecursor = False
#cSurv = int(c.popSize * c.perElitist)
cSurv = int(c.perElitist * c.popSize)

###### required variables ######
fits = []
envs = ENVIRONMENTS()

###### Make a population ######
parents = POPULATION( c.popSize )
parents.Initialize()

###### Load Precursor into Population ######
if os.path.isfile(pickledPop) and loadPrecursor:

    f = open(pickledPop, "rb")
    parents.Copy_Best_From(pickle.load(f), cSurv)
    f.close()

###### Print out fitness of initial parent ######
parents.Evaluate( envs, hideSim=True, startPaused=False , printFit=False )
parents.Print()

###### Iterate over generations ######
for g in range(0, c.numGens):

    # Initialize Children and fill population
    children = POPULATION( c.popSize )

    children.Copy_Best_From(parents, cSurv)

    # Rapture chance
    if random.random() < c.perRapture:

        print('Rapture')
        children.Rapture()
        children.Evaluate(envs, hideSim=True, startPaused=False, printFit=False)
        parents = cp.deepcopy(children)

    else:

        # Simple collection evaluation
        children.Collect_Children_From(parents, c.perCrossOver)

        # Evaluate Children and replace parents
        children.Evaluate( envs, hideSim=True, startPaused=False , printFit=False )
        parents.ReplaceWith( children )

    # Debugging
    fits.append(parents.p[0].fitness)
    print(g, end=' ')
    parents.Print()


###### Visualize strongest configuration ######
for e in envs.envs:

    parents.p[0].Start_Evaluation( envs.envs[e], hideSim=False, startPaused=True )
    parents.p[0].sim.Wait_To_Finish()


# for i in parents.p:
#
#     parents.p[i].Start_Evaluation( envs.envs[0], hideSim=False, startPaused=False)
#     #parents.p[i].sim.Wait_To_Finish()


###### This pickles the best configuration ######
# print('The parents will be pickled...')
# for i in parents.p:
#     parents.p[i].ID = 0
#
# f = open("robot.p", "wb")
# pickle.dump(parents, f)
# f.close()


###### Data Visualization ######
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
plt.plot(fits)
plt.show()
