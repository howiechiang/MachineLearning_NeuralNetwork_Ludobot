from population import POPULATION
from pyrosim import PYROSIM
from robot import ROBOT
from minimalRobot import MINIMAL_ROBOT
from individual import INDIVIDUAL
import constants as c
from core01_HillClimber import *
from environments import ENVIRONMENTS


import matplotlib.pyplot as plt
import copy as cp
import sys
import pickle
import random
import os.path
import time

genome = [MatrixCreate(c.numHidNeurons, 5), MatrixCreate(c.numHidNeurons, 8),
               MatrixCreate(c.numHidNeurons, c.numHidNeurons)]
genome[0] = MatrixRandomize(genome[0], 0, 0)
genome[1] = MatrixRandomize(genome[1], 0, 0)
genome[2] = MatrixRandomize(genome[2], 0, 0)

# Plain Robot without motor Neurons
sim = PYROSIM(playPaused=True, playBlind=False, evalTime=1000000)
robot = ROBOT(sim, genome)
sim.Start()