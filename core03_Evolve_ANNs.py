from core01_HillClimber import *
from core02_ANN import *
import constants
import sys
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import math


def VectorCreate(width):

    return np.zeros(width, dtype='f')

def MeanDistance(v1, v2):

    if len(v1) != len(v2):
        sys.exit("Vectors are not of the same size")

    else:

        temp = 0
        for i in range(0, len(v1) - 1):
            temp += abs((v1[i] - v2[i])**2)

        return temp/len(v1)

def SynapseFitness(synapse, desiredNeuronValues):

    neuronValues = MatrixCreate(10, 10)
    neuronValues[0, :] = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    for i in range(1, len(neuronValues[:, 0])):
        neuronValues = UpdateNeuron(neuronValues, synapse, i)

    #PlotInGrayScale(neuronValues)
    actualNeuronValues = neuronValues[9, :]
    diff = MeanDistance(actualNeuronValues, desiredNeuronValues)

    return 1 - diff

def SynapseFitness2(synapse, desiredNeuronValues):

    neuronValues = MatrixCreate(10, 10)
    neuronValues[0, :] = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    for i in range(1, len(neuronValues[:, 0])):
        neuronValues = UpdateNeuron(neuronValues, synapse, i)

    #PlotInGrayScale(neuronValues)
    actualNeuronValues = neuronValues[9, :]

    diff = 0
    for i in range(1, 9):
        for j in range(0, 9):
            diff = diff + abs(neuronValues[i, j] - neuronValues[i, j + 1])
            diff = diff + abs(neuronValues[i + 1, j] - neuronValues[i, j])

        diff = diff / (2 * 8 * 9)

    return 1 - diff


if __name__ == '__main__':

    # Initialize Matrices
    numNeurons = 10
    numUpdates = 10

    parentSynapse = MatrixCreate(numNeurons, numNeurons)
    desiredNeuronValues = VectorCreate(numNeurons)

    # Set initial values for all matrices
    parentSynapse = MatrixRandomize(parentSynapse, -1, 1)
    desiredNeuronValues = np.array([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1])

    # Create a Child and Save the superior version
    parentFitness = SynapseFitness(parentSynapse, desiredNeuronValues)
    fits = []

    # Iterate over multiple generations
    for currentGeneration in range(3000):
        #print currentGeneration, parentFitness
        childSynapse = MatrixPerturb(parentSynapse, 0.08, 1, -1)
        childFitness = SynapseFitness(childSynapse, desiredNeuronValues)

        if childFitness > parentFitness:
            parentSynapse = childSynapse
            parentFitness = childFitness

        fits.append(parentFitness)

    # Recreate neuronValues of Ideal Synapse so it can be visualized.
    neuronValues = MatrixCreate(10, 10)
    neuronValues[0, :] = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    for i in range(1, len(neuronValues[:, 0])):
        neuronValues = UpdateNeuron(neuronValues, parentSynapse, i)

    # Plotting & Visuals
    PlotInGrayScale(neuronValues)
    plt.plot(fits)
    plt.show()
