########################################################################################################################
# Mad Constants Bro, Not Variables
########################################################################################################################
###### Some basic sense Constants ######
pi = 3.14256

###### Constants for Simulation ######
evaluationTime = 2000

###### Constants for Robot ######
L = 0.1
R = L/5
H = 0.1
numHidNeurons = 5

biasSensor = 0.01
biasMotor = 0.01
biasNeuron = 0.01

###### Evolution Constants ######
popSize = 10
numGens = 50
numEnvs = 4
tau = 0.5

###### Logistics of Children Generation ######
perElitist = .1          # elitist percentage
perCrossOver = .01        # percent chance to breed
perRapture = .05      # percent chance to reset population
sMutation = 0.3          # sigma of mutation
