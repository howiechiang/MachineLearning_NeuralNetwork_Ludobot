import random
import math
import pickle
from robot import ROBOT
from pyrosim import PYROSIM


class INDIVIDUAL:

    def __init__(self):

        self.genome = random.random() * 2 - 1
        self.fitness = 0

    def Evaluate(self, hideSim=True):

        sim = PYROSIM(playPaused=False, playBlind=hideSim, evalTime=1000)
        robot = ROBOT(sim, self.genome)

        sim.Start()
        sim.Wait_To_Finish()

        x = sim.Get_Sensor_Data(sensorID=5, s=0)
        y = sim.Get_Sensor_Data(sensorID=5, s=1)
        z = sim.Get_Sensor_Data(sensorID=5, s=2)

        self.fitness = y[-1]

    def Mutate(self):

        self.genome = random.gauss(self.genome, math.fabs(self.genome))
