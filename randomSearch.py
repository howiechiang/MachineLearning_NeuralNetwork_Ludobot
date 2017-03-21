import matplotlib.pyplot as plt
from pyrosim import PYROSIM
from robot import ROBOT
from individual import INDIVIDUAL
import random



for i in range(0,2):
    ########################################################################################################################
    # Pyrosim setup
    ########################################################################################################################

    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)

########################################################################################################################
# Data Visualization
########################################################################################################################
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
# plt.plot(sensorData_2)
# plt.show()