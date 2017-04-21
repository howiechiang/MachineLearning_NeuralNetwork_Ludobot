from geodude import GEODUDE
from pyrosim import PYROSIM
import constants as c






sim = PYROSIM( playPaused=True, playBlind=False, evalTime=10000)
geodude1 = GEODUDE(sim)
sim.Start()
sim.Wait_To_Finish()

# touch = sim.Get_Sensor_Data(sensorID=0)
# print(touch)