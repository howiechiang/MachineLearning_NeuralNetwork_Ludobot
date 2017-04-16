import pickle
from individual import INDIVIDUAL
from environments import  ENVIRONMENTS

###### Load Picked Population ######
f = open('robot.p', 'rb')
best = pickle.load(f)
f.close()

####### Create Environments ######
envs = ENVIRONMENTS()

best.p[0].fitness = 0

for e in envs.envs:

    best.p[0].Start_Evaluation(envs.envs[e], hideSim=False, startPaused=True)
    best.p[0].Compute_Fitness(printFit=True)

print(best.p[0].fitness)