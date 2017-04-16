import constants as c


###### Variables for Body Size ######
pi = c.pi
R = 0.3         # Head
L1 = 0.2        # Bicep Length
R1 = 0.0625       # Bicep Radius
L2 = 0.25       # Forearm Length
R2 = 0.075        # Forearm Radius


H1 = 0.15        # Hand Length
H2 = 0.2          # Hand Height
H3 = .0625          # Hand Width

F1 = 0.075      # Finger 1 Length
F2 = 0.075      # Finger 2 Length
F3 = 0.0625       # Finger 3 Length


D = 0.05

###### Color Scheme for body ######
rColor = 184 / 255
gColor = 184 / 255
bColor = 148 / 255


###### Model Setup ######
class GEODUDE:

    def __init__( self, sim ):

        self.Send_Object(sim)
        self.Send_Joints(sim)
        self.Send_Sensors(sim)
        self.Send_Neurons(sim)
        # self.Send_Synapse(sim)

    def Send_Object( self, sim ):

        ###### Head ######
        sim.Send_Cylinder( objectID=0,
                           x=0, y=0, z=R,
                           length=0, radius=R,
                           r=rColor, g=gColor, b=bColor)

        ###### Left Arm ######
        # Bicep
        sim.Send_Cylinder( objectID=1,
                           x=(R + L1 / 2), y=0, z=R,
                           length=L1, radius=R1,
                           r1=1, r2=0, r3=0,
                           r=rColor, g=gColor, b=bColor)
        # Forearm
        sim.Send_Cylinder( objectID=2,
                           x=(R + L1 + L2 / 2), y=0, z=R,
                           length=L2, radius=R2,
                           r1=1, r2=0, r3=0,
                           r=rColor, g=gColor, b=bColor)
        # Hand
        sim.Send_Box( objectID=3,
                      x=(R + L1 + R1 + L2 + H1 / 2), y=0, z=R,
                      length=H1, height=H2, width=H3,
                      r=rColor, g=gColor, b=bColor)

        # Thumb
        sim.Send_Box( objectID=4,
                      x=(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1 / 2),
                      length=D, height=F1, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=5,
                      x=(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1 * 3 / 2),
                      length=D, height=F1, width=D,
                      r=rColor, g=gColor, b=bColor)

        # Finger - 1
        sim.Send_Box( objectID=6,
                      x=(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R + D * 3 / 2),
                      length=F1, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=7,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R + D * 3 / 2),
                      length=F2, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=8,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 +F3 / 2), y=0, z=(R + D * 3 / 2),
                      length=F3, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        # Finger - 2
        sim.Send_Box( objectID=9,
                      x=(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R + D * 1 / 2),
                      length=F1, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=10,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R + D * 1 / 2),
                      length=F2, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=11,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 +F3 / 2), y=0, z=(R + D * 1 / 2),
                      length=F3, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        # Finger - 3
        sim.Send_Box( objectID=12,
                      x=(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R - D * 1 / 2),
                      length=F1, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=13,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R - D * 1 / 2),
                      length=F2, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=14,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 +F3 / 2), y=0, z=(R - D * 1 / 2),
                      length=F3, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        # Finger - 4
        sim.Send_Box( objectID=15,
                      x=(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R - D * 3 / 2),
                      length=F1, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=16,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R - D * 3 / 2),
                      length=F2, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        sim.Send_Box( objectID=17,
                      x=(R + L1 + R1 + L2 + H1 + F1 + F2 +F3 / 2), y=0, z=(R - D * 3 / 2),
                      length=F3, height=D, width=D,
                      r=rColor, g=gColor, b=bColor)

        ###### Right Arm ######
        # Bicep
        sim.Send_Cylinder(objectID=18,
                          x=-(R + L1 / 2), y=0, z=R,
                          length=L1, radius=R1,
                          r1=1, r2=0, r3=0,
                          r=rColor, g=gColor, b=bColor)
        # Forearm
        sim.Send_Cylinder(objectID=19,
                          x=-(R + L1 + L2 / 2), y=0, z=R,
                          length=L2, radius=R2,
                          r1=1, r2=0, r3=0,
                          r=rColor, g=gColor, b=bColor)
        # Hand
        sim.Send_Box(objectID=20,
                     x=-(R + L1 + R1 + L2 + H1 / 2), y=0, z=R,
                     length=H1, height=H2, width=H3,
                     r=rColor, g=gColor, b=bColor)

        # Thumb
        sim.Send_Box(objectID=21,
                     x=-(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1 / 2),
                     length=D, height=F1, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=22,
                     x=-(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1 * 3 / 2),
                     length=D, height=F1, width=D,
                     r=rColor, g=gColor, b=bColor)

        # Finger - 1
        sim.Send_Box(objectID=23,
                     x=-(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R + D * 3 / 2),
                     length=F1, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=24,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R + D * 3 / 2),
                     length=F2, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=25,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 + F3 / 2), y=0, z=(R + D * 3 / 2),
                     length=F3, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        # Finger - 2
        sim.Send_Box(objectID=26,
                     x=-(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R + D * 1 / 2),
                     length=F1, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=27,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R + D * 1 / 2),
                     length=F2, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=28,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 + F3 / 2), y=0, z=(R + D * 1 / 2),
                     length=F3, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        # Finger - 3
        sim.Send_Box(objectID=29,
                     x=-(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R - D * 1 / 2),
                     length=F1, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=30,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R - D * 1 / 2),
                     length=F2, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=31,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 + F3 / 2), y=0, z=(R - D * 1 / 2),
                     length=F3, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        # Finger - 4
        sim.Send_Box(objectID=32,
                     x=-(R + L1 + R1 + L2 + H1 + F1 / 2), y=0, z=(R - D * 3 / 2),
                     length=F1, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=33,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 / 2), y=0, z=(R - D * 3 / 2),
                     length=F2, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)

        sim.Send_Box(objectID=34,
                     x=-(R + L1 + R1 + L2 + H1 + F1 + F2 + F3 / 2), y=0, z=(R - D * 3 / 2),
                     length=F3, height=D, width=D,
                     r=rColor, g=gColor, b=bColor)


    def Send_Joints( self, sim ):

        ###### Left Arm ######
        # Body <-> Bicep
        sim.Send_Joint( jointID=0,
                        firstObjectID=0, secondObjectID=1,
                        x=R, y=0, z=R,
                        n1=1, n2=1, n3=-1,
                        lo=-pi/2, hi=pi/2)

        # Bicep <-> Forearm
        sim.Send_Joint( jointID=1,
                        firstObjectID=1, secondObjectID=2,
                        x=(R + L1 + R1), y=0, z=R,
                        n1=0, n2=0, n3=-1,
                        lo=0, hi=pi/2)

        # Forearm <-> Hand
        sim.Send_Joint(jointID=2,
                       firstObjectID=2, secondObjectID=3,
                       x=(R + L1 + R1 + L2), y=0, z=R,
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        # Hand <-> Thumb1
        sim.Send_Joint(jointID=3,
                       firstObjectID=3, secondObjectID=4,
                       x=(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2),
                       n1=1, n2=0, n3=0,
                       lo=0, hi=pi / 2)

        # Thumb1 <-> Thumb2
        sim.Send_Joint(jointID=4,
                       firstObjectID=4, secondObjectID=5,
                       x=(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1),
                       n1=1, n2=0, n3=0,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger1
        sim.Send_Joint(jointID=5,
                       firstObjectID=3, secondObjectID=6,
                       x=(R + L1 + R1 + L2 + H1), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=6,
                       firstObjectID=6, secondObjectID=7,
                       x=(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=7,
                       firstObjectID=7, secondObjectID=8,
                       x=(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger2
        sim.Send_Joint(jointID=8,
                       firstObjectID=3, secondObjectID=9,
                       x=(R + L1 + R1 + L2 + H1), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=9,
                       firstObjectID=9, secondObjectID=10,
                       x=(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=10,
                       firstObjectID=10, secondObjectID=11,
                       x=(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger3
        sim.Send_Joint(jointID=11,
                       firstObjectID=3, secondObjectID=12,
                       x=(R + L1 + R1 + L2 + H1), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=12,
                       firstObjectID=12, secondObjectID=13,
                       x=(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=13,
                       firstObjectID=13, secondObjectID=14,
                       x=(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger4
        sim.Send_Joint(jointID=14,
                       firstObjectID=3, secondObjectID=15,
                       x=(R + L1 + R1 + L2 + H1), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=15,
                       firstObjectID=15, secondObjectID=16,
                       x=(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=16,
                       firstObjectID=16, secondObjectID=17,
                       x=(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=-1,
                       lo=0, hi=pi / 2)

        ###### Left Arm ######
        # Body <-> Bicep
        sim.Send_Joint( jointID=17,
                        firstObjectID=0, secondObjectID=18,
                        x=-R, y=0, z=R,
                        n1=-1, n2=-1, n3=1,
                        lo=-pi/2, hi=pi/2)

        # Bicep <-> Forearm
        sim.Send_Joint( jointID=18,
                        firstObjectID=18, secondObjectID=19,
                        x=-(R + L1 + R1), y=0, z=R,
                        n1=0, n2=0, n3=1,
                        lo=0, hi=pi/2)

        # Forearm <-> Hand
        sim.Send_Joint(jointID=19,
                       firstObjectID=19, secondObjectID=20,
                       x=-(R + L1 + R1 + L2), y=0, z=R,
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        # Hand <-> Thumb1
        sim.Send_Joint(jointID=20,
                       firstObjectID=20, secondObjectID=21,
                       x=-(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2),
                       n1=1, n2=0, n3=0,
                       lo=0, hi=pi / 2)

        # Thumb1 <-> Thumb2
        sim.Send_Joint(jointID=21,
                       firstObjectID=21, secondObjectID=22,
                       x=-(R + L1 + R1 + L2 + D / 2), y=0, z=(R + H2 / 2 + F1),
                       n1=1, n2=0, n3=0,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger1
        sim.Send_Joint(jointID=22,
                       firstObjectID=20, secondObjectID=23,
                       x=-(R + L1 + R1 + L2 + H1), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=23,
                       firstObjectID=23, secondObjectID=24,
                       x=-(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=24,
                       firstObjectID=24, secondObjectID=25,
                       x=-(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R + D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger2
        sim.Send_Joint(jointID=25,
                       firstObjectID=20, secondObjectID=26,
                       x=-(R + L1 + R1 + L2 + H1), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=26,
                       firstObjectID=26, secondObjectID=27,
                       x=-(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=27,
                       firstObjectID=27, secondObjectID=28,
                       x=-(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R + D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger3
        sim.Send_Joint(jointID=28,
                       firstObjectID=20, secondObjectID=29,
                       x=-(R + L1 + R1 + L2 + H1), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=29,
                       firstObjectID=29, secondObjectID=30,
                       x=-(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=30,
                       firstObjectID=30, secondObjectID=31,
                       x=-(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R - D * 1 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        # Hand <-> Finger4
        sim.Send_Joint(jointID=31,
                       firstObjectID=20, secondObjectID=32,
                       x=-(R + L1 + R1 + L2 + H1), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=32,
                       firstObjectID=32, secondObjectID=33,
                       x=-(R + L1 + R1 + L2 + H1 + F1), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)

        sim.Send_Joint(jointID=33,
                       firstObjectID=33, secondObjectID=34,
                       x=-(R + L1 + R1 + L2 + H1 + F1 + F2), y=0, z=(R - D * 3 / 2),
                       n1=0, n2=0, n3=1,
                       lo=0, hi=pi / 2)


    # DEBUG ATM #
    def Send_Sensors( self, sim ):

        # DEBUG ONLY #
        sim.Send_Touch_Sensor( sensorID=0, objectID=0)

    def Send_Neurons( self, sim ):

        # DEBUG ONLY #
        sim.Send_Sensor_Neuron( neuronID=0, sensorID=0 )

        sim.Send_Motor_Neuron( neuronID=1, jointID=0, tau=c.tau )
        sim.Send_Motor_Neuron( neuronID=2, jointID=1, tau=c.tau )
        # sim.Send_Motor_Neuron(neuronID=3, jointID=2, tau=c.tau)
        # sim.Send_Motor_Neuron(neuronID=4, jointID=3, tau=c.tau)

    def Send_Synapse( self, sim ):

        # DEBUG ONLY #
        sim.Send_Synapse( sourceNeuronID=0, targetNeuronID=1, weight=1 )
        # sim.Send_Synapse( sourceNeuronID=0, targetNeuronID=2, weight=1 )