import pickle
from individual import INDIVIDUAL




f = open('robot.p', 'rb')
best = pickle.load(f)
f.close()
print(best)
best.Evaluate(hideSim=False)
print(best.fitness)