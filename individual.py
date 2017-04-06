from robot import ROBOT
from pyrosim import PYROSIM
import constants as c
from core01_HillClimber import *

import random
import math
import pickle
import numpy as np


###### Individual ######
class INDIVIDUAL:

    def __init__( self, i ):

        self.ID = i
        self.genome = MatrixCreate(5, 8)
        self.genome = MatrixRandomize(self.genome, 1, -1)
        self.fitness = 0


    def Evaluate( self, hideSim=True, startPaused=False ):

        sim = PYROSIM( playPaused=startPaused, playBlind=hideSim, evalTime=c.evaluationTime )
        robot = ROBOT( sim, self.genome )
        sim.Start()

        sim.Wait_To_Finish()

        x = sim.Get_Sensor_Data(sensorID=4, s=0)
        y = sim.Get_Sensor_Data(sensorID=4, s=1)
        z = sim.Get_Sensor_Data(sensorID=4, s=2)

        # self.sensorData_0 = sim.Get_Sensor_Data(sensorID=0)
        # self.sensorData_1 = sim.Get_Sensor_Data(sensorID=1)
        # self.sensorData_2 = sim.Get_Sensor_Data(sensorID=2)
        # self.sensorData_3 = sim.Get_Sensor_Data(sensorID=3)
        # self.sensorData_4 = sim.Get_Sensor_Data(sensorID=4)

        # print(sim.Get_Sensor_Data(sensorID=4))

        self.fitness = y[-1]
        del sim

    def Mutate( self ):

        # This will choose a random gene to mutate. but this is based on a Gauss distribution. This has been edited to
        # accept 2 dimensional genes
        x = random.randint(0, len(self.genome) - 1 )
        y = random.randint(0, len(self.genome[0]) - 1 )
        self.genome[x, y] = random.gauss(self.genome[x, y], math.fabs(self.genome[x, y]))

        # # This will mutate ALL genes
        # for i in range(0, len(self.genome)):
        #     self.genome[i] = random.gauss(self.genome[i], math.fabs(self.genome[i]))

    def Print( self ):

        print( '[', self.ID, self.fitness, ']', end=" " )
        #print(self.fitness, end=" "),
        #print(self.genome)

    def Start_Evaluation( self , environment , hideSim=True , startPaused=False ):

        self.sim = PYROSIM( playPaused=startPaused, playBlind=hideSim,
                            evalTime=c.evaluationTime )
        robot = ROBOT(self.sim, self.genome)
        environment.Send_To( self.sim )


        self.sim.Start()

    def Compute_Fitness( self, printFit=False ):

        self.sim.Wait_To_Finish()

        # x = self.sim.Get_Sensor_Data( sensorID=4, s=0 )     # s is the flag for the desired coordinate
        # y = self.sim.Get_Sensor_Data( sensorID=4, s=1 )
        # z = self.sim.Get_Sensor_Data( sensorID=4, s=2 )

        # the returned value is the inverse squared of the distance to light source
        distLight = self.sim.Get_Sensor_Data( sensorID=4, s=0 )

        if printFit:
            print(distLight[-1])

        self.fitness += math.log1p( distLight[-1] )
        del self.sim