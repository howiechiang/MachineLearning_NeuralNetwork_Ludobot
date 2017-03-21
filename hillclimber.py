import matplotlib.pyplot as plt
from pyrosim import PYROSIM
from robot import ROBOT
from individual import INDIVIDUAL
import copy as cp
import pickle
import random


parent = INDIVIDUAL()

for i in range(0,100):

    child = cp.deepcopy(parent)
    child.Mutate()

    parent.Evaluate(hideSim=True)
    child.Evaluate(hideSim=True)

    print("[g: ", i, "] [PW: ", parent.genome," ][P: ", parent.fitness, "] [C:", child.fitness, "]")

    if (child.fitness > parent.fitness):
        parent = child
        f = open("robot.p", "wb")
        pickle.dump(parent, f)
        f.close()
parent.Evaluate(hideSim=False)


########################################################################################################################
# Data Visualization
########################################################################################################################
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
# plt.plot(sensorData_2)
# plt.show()