from individual import INDIVIDUAL
import copy
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


    def Evaluate( self, hideSim=True, startPaused=False ):

        for i in self.p:

            #self.p[i].Evaluate(hideSim, startPaused)
            self.p[i].Start_Evaluation(hideSim, startPaused)

        for i in self.p:

            self.p[i].Compute_Fitness()


    def Mutate( self ):

        for i in self.p:

            self.p[i].Mutate()


    def ReplaceWith( self, other ):

        for i in self.p:

            if ( self.p[i].fitness < other.p[i].fitness ):

                self.p[i] = copy.deepcopy(other.p[i])


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

        self.p[len(self.p)] = other.p[best]


    def Collect_Children_From(self, other):

        for i in range(len(self.p), self.popSize):

            winner = self.Winner_Of_Tournament_Selection(other)
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()
            # self.p[i].ID = i


    def Winner_Of_Tournament_Selection(self, other):

        p1 = random.randint(0, len(other.p) - 1)
        p2 = random.randint(0, len(other.p) - 1)

        while p1 == p2:

            p2 = random.randint(0, len(other.p) - 1)

        if other.p[p2].fitness > other.p[p1].fitness:

            return other.p[p2]
        else:
            return other.p[p1]