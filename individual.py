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

        # genome[0] = Hidden <-> Sensor Neurons
        # genome[1] = Hidden <-> Motor Neurons
        # genome[2] = Hidden <-> Hidden Recurrent Neurons
        self.genome = [MatrixCreate(c.numHidNeurons, 5), MatrixCreate(c.numHidNeurons,8), MatrixCreate(c.numHidNeurons, c.numHidNeurons)]
        self.genome[0] = MatrixRandomize(self.genome[0], 1, -1)
        self.genome[1] = MatrixRandomize(self.genome[1], 1, -1)
        self.genome[2] = MatrixRandomize(self.genome[2], 1, -1)
        self.fitness = 0
        self.stability = 0
        self.uniqueness = 0
        self.touchSensorData = np.array([])

    def Evaluate( self, environment, hideSim=True, startPaused=False, printFalse=False ):

        self.Start_Evaluation(environment=environment, hideSim=hideSim, startPaused=startPaused)
        self.Compute_Fitness( printFit=printFalse)
        self.Store_Sensor_Data()
        del self.sim

    def Mutate( self , s = c.sMutation):

        # This will choose a random gene to mutate. but this is based on a Gauss distribution. This has been edited to
        # accept 2 dimensional genes

        for i in range(0,3):

            # Synapse Layer
            sLayer = random.randint(0, len(self.genome) - 1)
            x = random.randint(0, len(self.genome[sLayer]) - 1 )
            y = random.randint(0, len(self.genome[sLayer][x]) - 1 )

            # random.gauss(mean, sigma)
            self.genome[sLayer][x,y] = random.gauss(self.genome[sLayer][x,y], math.fabs(self.genome[sLayer][x,y] * s ))


            # # This will mutate ALL genes
            # for i in range(0, len(self.genome)):
            #     self.genome[i] = random.gauss(self.genome[i], math.fabs(self.genome[i]))

            # Clip the value of Gene
            self.genome[sLayer][x,y] = np.clip(self.genome[sLayer][x,y], -1, 1)
            #self.genome[x, y] = max(min(1, self.genome[x, y]), -1)


    def Print( self ):

        print( '[', self.ID, self.fitness, self.uniqueness, ']', end=" " )
        #print(self.fitness, end=" "),
        #print(self.genome)

    def Start_Evaluation( self, environment, hideSim=True, startPaused=False ):

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
        distLight = self.sim.Get_Sensor_Data(sensorID=4, s=0)
        distX = self.sim.Get_Sensor_Data(sensorID=5, s=0)
        distY = self.sim.Get_Sensor_Data(sensorID=5, s=1)

        # Touch Sensor Values.... Comes in vector
        for t in range (0, 4):

            self.stability += sum(self.sim.Get_Sensor_Data(sensorID=t)) * 0.25

        # DEBUGGING #
        if printFit:

            plt.plot(distLight ** 0.25)
            plt.show()

        # Fitness Computation
        self.fitness += distLight[-1] ** 0.25
        # self.fitness += np.clip(distLight[-1], 0, 0.1)


    def Store_Sensor_Data(self):

        touchSensorData = np.zeros(shape=(4, c.evaluationTime))

        for t in range(0, 4):

            touchSensorData[t,:] = self.sim.Get_Sensor_Data(sensorID=t, s=0)

        self.touchSensorData = touchSensorData

        # Stability Data
        columnSums = np.sum( touchSensorData, axis=0 )
        columnThresholds = np.clip( columnSums, 0, 1 )
        self.stability = np.sum( columnThresholds )

    def Compute_Distance_Between(self, other):

        try:

            self.touchSensorData

        except NameError:

            print("Sensor Data was not Stored")

        else:

            #euclideanDistance = np.linalg.norm(self.touchSensorData - other.touchSensorData)
            #euclideanDistance = self.fitness - other.fitness

            delta = np.sum(np.fabs(self.touchSensorData - other.touchSensorData))
            return delta

            # tOnGround = np.sum(self.touchSensorData)
            # tOnGround_Other = np.sum(other.touchSensorData)
            # euclideanDistance = np.fabs(tOnGround - tOnGround_Other)
            #
            # return euclideanDistance
    def Mutate_Neat(self):

        # synapse layer
        sLayer = random.randint(0, len(self.genome) - 1)

        # Shuffles the row of that Synapse layer
        self.genome[sLayer] = self.genome[sLayer] [np.random.permutation( len(self.genome[sLayer][0]) ), :]
