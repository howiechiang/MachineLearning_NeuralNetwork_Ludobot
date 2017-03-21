import matplotlib.pyplot as plt
from pyrosim import PYROSIM
from robot import ROBOT
import random



for i in range(0,3):
    ########################################################################################################################
    # Pyrosim setup
    ########################################################################################################################
    sim = PYROSIM(playPaused=False, evalTime=300)
    robot = ROBOT(sim, random.random()*2-1)

    sim.Start()
    sim.Wait_To_Finish()

    sensorData_0 = sim.Get_Sensor_Data(sensorID=0)
    sensorData_1 = sim.Get_Sensor_Data(sensorID=1)
    sensorData_2 = sim.Get_Sensor_Data(sensorID=2)
    sensorData_3 = sim.Get_Sensor_Data(sensorID=3)
    sensorData_4 = sim.Get_Sensor_Data(sensorID=4)
    sensorData_5 = sim.Get_Sensor_Data(sensorID=5)

    # x = sim.Get_Sensor_Data(sensorID=5, s=0)
    # y = sim.Get_Sensor_Data(sensorID=5, s=1)
    # z = sim.Get_Sensor_Data(sensorID=5, s=2)
    #
    # print (x[-1])
    # print(y[-1])
    # print(z[-1])

########################################################################################################################
# Data Visualization
########################################################################################################################
# f = plt.figure()
# #pn = f.add_subplot(111)
# #pn.set_ylim(-1, +1)
# plt.plot(sensorData_2)
# plt.show()