import numpy as np
import copy as cp
import matplotlib.pyplot as plt
import random



def MatrixCreate(rows, columns):

    return np.array(np.zeros(shape=(rows,columns)))


def MatrixRandomize(v, max='NULL', min='NULL'):

    c = cp.deepcopy(v)

    if max != 'NULL' and min != 'NULL':
        for x in np.nditer(c, op_flags=['readwrite']):
            x[...] = random.uniform(max, min)

    else:
        for x in np.nditer(c, op_flags=['readwrite']):
            x[...] = random.getrandbits(1)

    return c


def Fitness(v):

    avg = 0
    for x in np.nditer(v):
        avg = avg + x/v.size
    return avg


def MatrixPerturb(v, prob, max='NULL', min='NULL'):

    c = cp.deepcopy(v)

    if max != 'NULL' and min != 'NULL':
        for x in np.nditer(c, op_flags=['readwrite']):
            x[...] = random.uniform(max, min)

    else:
        for x in np.nditer(c, op_flags=['readwrite']):
            if prob > random.random():
                x[...] = random.getrandbits(1)

    return c

def PlotVectorAsLine(fits):
    plt.plot(fits)
    plt.show()

def PlotInGrayScale(matrix):
    plt.imshow(matrix, cmap='gray', aspect='auto', interpolation='nearest')
    plt.show()

########################################################################################################################

########################################################################################################################
if __name__ == '__main__':

    plt.show(block=True)
    parent = MatrixCreate(1, 50)
    Genes = MatrixCreate(50, 5000)

    # Create a Child and Save the superior version
    for i in range(5):
        parent = MatrixRandomize(parent)
        parentFitness = Fitness(parent)
        fits = []

        for currentGeneration in range(500):
            #print currentGeneration, parentFitness
            child = MatrixPerturb(parent, 0.05)
            childFitness = Fitness(child)

            if childFitness > parentFitness:
                parent = child
                parentFitness = childFitness

            fits.append(round(parentFitness, 2))

            for j in parent[0,:]:
                Genes[j,currentGeneration] = parent[0,j]
            #print(parent)
        #print(Genes)
        #PlotVectorAsLine(fits)
        plt.plot(fits)
    plt.show()
    PlotInGrayScale(Genes)
