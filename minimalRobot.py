import matplotlib.pyplot as plt
from pyrosim import PYROSIM
import constants as c

###### Variables ######
pi = c.pi

###### Model setup ######
class MINIMAL_ROBOT:

    def __init__( self, sim, wts ):

        ####### Components ######
        sim.Send_Cylinder(objectID=0, x=0, y=0, z=0.6, length=1.0, radius=0.1)
        sim.Send_Cylinder(objectID=1, x=0, y=0.5, z=1.1, length=1.0, radius=0.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)

        ###### Joints ######
        sim.Send_Joint(jointID=0, firstObjectID=0, secondObjectID=1, x=0, y=0, z=1.1, n1=-1, n2=0, n3=0, lo=-pi / 2,
                       hi=pi / 2)

        ###### Sensors ######
        sim.Send_Touch_Sensor(sensorID=0, objectID=0)
        sim.Send_Touch_Sensor(sensorID=1, objectID=1)
        sim.Send_Proprioceptive_Sensor(sensorID=2, jointID=0)
        sim.Send_Ray_Sensor(sensorID=3, objectID=1, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)
        sim.Send_Ray_Sensor(sensorID=4, objectID=1, x=0, y=1.1 / 2, z=1.1, r1=0, r2=0, r3=-1)
        sim.Send_Position_Sensor(sensorID=5, objectID=1)

        ###### This is broken for some reason but it should replace Sensor Neuron Activation
        # for sn in range(0,4):
        #     sim.Send_Sensor_Neuron(neuronID=sn, sensorID=sn)


        ###### Sensor Neurons ######
        sim.Send_Sensor_Neuron(neuronID=0, sensorID=0 )
        sim.Send_Sensor_Neuron(neuronID=1, sensorID=1 )
        sim.Send_Sensor_Neuron(neuronID=2, sensorID=2 )
        sim.Send_Sensor_Neuron(neuronID=3, sensorID=3 )
        sim.Send_Sensor_Neuron(neuronID=4, sensorID=4 )

        ###### Motor Neurons ######
        sim.Send_Motor_Neuron(neuronID=5, jointID=0 )

        ###### Synapses ######
        for s in range(0,4):
            sim.Send_Synapse(sourceNeuronID=s, targetNeuronID=5, weight=wts[s])
            # sim.Send_Synapse(sourceNeuronID=0, targetNeuronID=5, weight=wt)
            # sim.Send_Synapse(sourceNeuronID=1, targe~~tNeuronID=5, weight=-wt)