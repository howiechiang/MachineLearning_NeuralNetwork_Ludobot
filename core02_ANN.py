from core01_HillClimber import *
import constants
import sys
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import math
import copy as cp
import random


def PlotSynapseConnections(neuronPos, synapses):
    plt.plot(neuronPositions[0, :], neuronPositions[1, :], 'ko', markerfacecolor=[1, 1, 1], markersize=18)

    for i in range(0, len((neuronPos[0, :]))):
        j = i + 1

        while j <= len(neuronPos[0, :]) - 1:

            # Color of Synapse
            if synapses[i, j] > 0:
                assignedColor = 'w'
            elif synapses[i, j] < 0:
                assignedColor = 'k'
            else:
                assignedColor = [0.5, 0.5, 0.5]

            # Width of Synapse
            w = int(10 * abs(synapses[i, j])) + 1

            plt.plot([neuronPos[0, i], neuronPos[0, j]],  [neuronPos[1, i], neuronPos[1, j]], color=assignedColor,
                    linewidth=w, path_effects=[pe.Stroke(linewidth=w+2, foreground='k'), pe.Normal()])
            j += 1
    plt.show()

def UpdateNeuron(neuronValues, synapses, i):

    # Checks if the dimensions of variables neuronValues and synapses are appropriate
    if len(synapses[:,0]) != len(synapses[0,:]):

        sys.exit("Synapses column & row size are not equal")

    elif len(synapses[:,0]) != len(neuronValues[0,:]):

        sys.exit("Number of neurons and synapses are not equal")


    # Calculates the next generation of neuron values
    for neuronCount in range(0, len(neuronValues[i-1,:])):

        temp = 0

        for aspectCount in range(0, len(synapses[:,neuronCount])):

            temp += synapses[aspectCount, neuronCount] * neuronValues[i - 1, aspectCount]

        # Contains the next generation within an acceptable range
        while abs(temp) > 1:
            temp = temp * 0.9

        neuronValues[i, neuronCount] = clamp(temp, 0, 1)

    return neuronValues

# Also known as the signma function, max output the mechanism can output, or cap of neuron value
def clamp(n, minn, maxn, thresh='MISSING'):

    # If there is no threshold return a capped value
    if thresh == 'MISSING':
        return max(min(maxn, n), minn)

    # If there is a threshold, assume that output must be discrete
    else:
        if n >= thresh:
            return maxn
        else:
            return minn


if __name__ == '__main__':

    weight_NN = MatrixCreate(10, 10)
    neuronValues = MatrixCreate(50, 10)
    neuronPositions = MatrixCreate(2, 10)
    synapses = MatrixCreate(10, 10)

    # Random synapse weights
    for i in np.nditer(synapses, op_flags=['readwrite']):
        i[...] = np.random.uniform(-1, 1)

    # Positions of Neurons
    angle = 0.0
    numNeurons = len(neuronValues[0, :])
    angleUpdate = 2 * constants.pi/numNeurons

    for i in range(0, numNeurons):

        neuronPositions[0, i] = math.cos(angle)
        neuronPositions[1, i] = math.sin(angle)
        angle += angleUpdate

    # Assign random values to first generation of neuron Values
    for i in np.nditer(neuronValues[0,:], op_flags=['readwrite']):
        i[...] = np.random.uniform(-1, 1)

    for i in range(0, len(neuronValues[:,0]) - 1):
        neuronValues = UpdateNeuron(neuronValues, synapses, i + 1)

    print (len(neuronValues[:,0]), len(neuronValues[0,:]))

    # Plot Commands
    PlotSynapseConnections(neuronPositions, synapses)
    PlotInGrayScale(neuronValues)
