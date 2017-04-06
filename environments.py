from environment import ENVIRONMENT
import constants as c

class ENVIRONMENTS:

    def __init__(self):

        self.envs = {}

        for i in range(0, c.numEnvs):

            self.envs[i] = ENVIRONMENT(i)
