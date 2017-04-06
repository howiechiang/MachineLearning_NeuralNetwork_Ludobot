from individual import INDIVIDUAL
from core01_HillClimber import *
import copy as cp
import random

###### Population ######
class POPULATION:

    def __init__( self, popSize ):

        self.popSize = popSize

        self.p = {}


    def Print( self ):

        for i in self.p:

            self.p[i].Print()

        print()     # This is needed so it end the printed command line


    def Evaluate( self, environments, hideSim=True, startPaused=False ):

        for i in self.p:

            self.p[i].fitness = 0

            for e in environments.envs:

                self.p[i].Start_Evaluation(environments.envs[e], hideSim, startPaused)
                self.p[i].Compute_Fitness()


    def Mutate( self ):

        for i in self.p:

            self.p[i].Mutate()


    def ReplaceWith( self, other ):

        for i in self.p:

            if ( self.p[i].fitness < other.p[i].fitness ):

                self.p[i] = cp.deepcopy(other.p[i])


    def Initialize( self ):

        for i in range( 0, self.popSize ):

            self.p[i] = INDIVIDUAL(i)


    def FillFrom( self, other ):

        self.Copy_Best_From(other)
        self.Collect_Children_From(other)


    def Copy_Best_From(self, other):

        best = 0
        bestFitness = other.p[0].fitness

        for i in other.p:

            if other.p[i].fitness > bestFitness:
                best =  i
                bestFitness = other.p[i].fitness

        self.p[0] = cp.deepcopy(other.p[best])
        #self.p[len(self.p)] = cp.deepcopy(other.p[best])


    def Collect_Children_From(self, other):

        for i in range(len(self.p), self.popSize):

            if i//2 == 0:

                winner = self.Winner_Of_Tournament_Selection(other)
                self.p[i] = cp.deepcopy(winner)
                self.p[i].Mutate()

            else:
                ###### Breeds with the first person, which in the loop is the fittest ######
                self.p[i] = cp.deepcopy(self.Breed(other))
                self.p[i].Mutate()

    def Winner_Of_Tournament_Selection(self, other):

        p1 = random.randint(0, len(other.p) - 1)
        p2 = random.randint(0, len(other.p) - 1)

        while p1 == p2:

            p2 = random.randint(0, len(other.p) - 1)

        if other.p[p2].fitness > other.p[p1].fitness:

            return other.p[p2]
        else:
            return other.p[p1]


    # Replaces population, but retains a specified # of survivors
    def Noahs_Ark(self, survivors):

        # include a loop to sort p[] based on most to least fit.

        for i in range(survivors, len(self.p)):

            self.p[i] = INDIVIDUAL(i)

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