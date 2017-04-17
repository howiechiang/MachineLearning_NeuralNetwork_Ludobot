########################################################################################################################
# Mad Constants Bro, Not Variables
########################################################################################################################


###### Constants for Simulation ######
evaluationTime = 1000


###### Constants for Robot ######
L = 0.1
R = L/5


###### Some basic sense Constants ######
pi = 3.14256


###### Evolution Constants ######
popSize = 10
numGens = 50
numEnvs = 4
tau = 0.3


###### Logistics of Children Generation ######
perElitist = .1          # elitist percentage
perCrossOver = .01        # percent chance to breed
perRapture = .05      # percent chance to reset population
sMutation = 0.3          # sigma of mutation
