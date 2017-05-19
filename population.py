from individual import INDIVIDUAL
from core01_HillClimber import *
import copy as cp
import random
import numpy as np
import constants as c

###### Population ######
class POPULATION:

    def __init__( self, popSize ):

        self.popSize = popSize

        self.p = {}

    ###### RECURSIVE INDIVIDUAL FUNCTIONS ######
    def Initialize( self ):

        for i in range( 0, self.popSize ):

            self.p[i] = INDIVIDUAL(i)

    def Evaluate( self, environments, hideSim=True, startPaused=False , printFit=False):

        for i in self.p:

            self.p[i].fitness = 0
            self.p[i].stability = 0
            self.p[i].uniqueness = 10000

            # for e in environments.envs:
            #
            #     self.p[i].Start_Evaluation(environments.envs[e], hideSim, startPaused)
            #     self.p[i].Compute_Fitness(printFit)
            #     self.p[i].Store_Sensor_Data()
            #     del self.p[i].sim

            self.p[i].Start_Evaluation(environments.envs[0], hideSim, startPaused)

        for i in self.p:

            self.p[i].Compute_Fitness(printFit)
            self.p[i].Store_Sensor_Data()
            del self.p[i].sim

            if printFit:

                print(self.p[i].fitness)
                print()

        # This is performed to compute uniqueness
        for i in self.p:

            self.Compute_Uniqueness(i)

    def Print( self ):

        for i in self.p:

            self.p[i].Print()

        print()     # This is needed so it end the printed command line

    def Mutate( self ):

        for i in self.p:

            self.p[i].Mutate()

    ###### POPULATION GENERATION ######
    # Replaces population, but retains a specified # of survivors
    def Rapture(self):

        # include a loop to sort p[] based on most to least fit.

        for i in range( len(self.p), self.popSize ):

            self.p[i] = INDIVIDUAL(i)

    def FillFrom( self, other ):

        self.Copy_Best_From( other )
        self.Collect_Children_From( other )

    def ReplaceWith( self, other ):

        for i in self.p:

            if ( self.p[i].fitness < other.p[i].fitness ) or ( self.p[i].uniqueness < other.p[i].uniqueness ):
            #if (self.p[i].uniqueness < other.p[i].uniqueness):

                self.p[i] = cp.deepcopy(other.p[i])

    ###### Finds the best of input populations and inserts into self ######
    def Copy_Best_From( self, other, cElite = 1):

        best = np.array(np.zeros(cElite))
        bestFitness = np.array(np.zeros(cElite))

        for i in other.p:

            for j in range(0, int(cElite)):

                # This is looped as such because np.insert and del does not work.....
                if other.p[i].fitness > bestFitness[j]:

                    for k in range(len(best) - 1, j, -1):

                        best[k] = best[k - 1]
                        bestFitness[k] = bestFitness[k - 1]

                    best[j] = i
                    bestFitness[j] = other.p[i].fitness
                    break

        for i in range(0, len(best)):

            ind = best[i]
            self.p[i] = cp.deepcopy(other.p[ind])

        #self.p[len(self.p)] = cp.deepcopy(other.p[best])

    def Collect_Children_From(self, other, crossOverChance=0):

        for i in range(len(self.p), self.popSize):

            # if random.random() < crossOverChance:
            #
            #     #self.p[i] = cp.deepcopy(self.Breed(other))
            #     #self.p[i].Mutate()
            #     self.p[i] = cp.deepcopy(other.p[i])
            #     print("CrossOver")
            #     return
            #
            # else:

            winner = self.Winner_Of_Tournament_Selection(other)
            self.p[i] = cp.deepcopy(winner)
            self.p[i].Mutate()

            # if i//2 == 0:
            #
            #     winner = self.Winner_Of_Tournament_Selection(other)
            #     self.p[i] = cp.deepcopy(winner)
            #     self.p[i].Mutate()
            #
            # else:
            #     ###### Breeds with the first person, which in the loop is the fittest ######
            #     self.p[i] = cp.deepcopy(self.Breed(other))
            #     self.p[i].Mutate()


    def Winner_Of_Tournament_Selection(self, other):

        p1 = len(self.p)
        p2 = random.randint(0, len(other.p) - 1)

        while p1 == p2:

            p2 = random.randint(0, len(other.p) - 1)

        if other.p[p2].fitness >= other.p[p1].fitness\
                or other.p[p2].uniqueness >= other.p[p1].uniqueness:

            return other.p[p2]

        else:

            return other.p[p1]

    def Compute_Uniqueness(self, i):

        # Uniqueness diminishes when it finds a similar robot...
        self.p[i].uniqueness = 1000000

        for j in range(0, c.popSize - 1):

            if ( j != i ):

                currentDistance = self.p[i].Compute_Distance_Between( self.p[j] )

                if ( currentDistance < self.p[i].uniqueness ):

                    self.p[i].uniqueness = currentDistance

    def Breed(self, other):

        p1 = random.randint(0, len(other.p) - 1)
        # p1 = 0
        p2 = random.randint(0, len(other.p) - 1)
        child = INDIVIDUAL(1)        # This only sets up the framework of the child

        geneImprint = MatrixCreate( len(other.p[p1].genome), len(other.p[p1].genome[0]) )
        geneImprint = MatrixRandomize(geneImprint)

        childGenome = other.p[p1].genome * geneImprint
        childGenome += other.p[p2].genome * np.logical_not(geneImprint)

        child.genome = childGenome

        return child

    def Perform_NEAT(self, i):

        self.p[i].Mutate_Neat()