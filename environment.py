import constants as c

class ENVIRONMENT:

    def __init__(self, i):

        self.ID = i

        # Size of photoaxis
        self.l = 0.5
        self.w = 0.5
        self.h = 0.5

        # Position
        self.x = 0
        self.y = 0
        self.z = 0

        # Configure Environment
        Place_Light_Source_To_The_Front(self)
        Place_Light_Source_To_The_Back(self)
        Place_Light_Source_To_The_Right(self)
        Place_Light_Source_To_The_Left(self)

        # print(self.x, self.y, self.z)


    def Send_To(self, sim):

        ##### Body ######
        sim.Send_Box(objectID = 9 ,
                     x = self.x , y = self.y , z = self.z ,
                     length = self.l , width = self.w , height = self.h ,
                     r = 1 , g = 1 , b = 1 )

        sim.Send_Light_Source( objectIndex = 9 )


###### General Equations To Edit Variables ######
def Place_Light_Source_To_The_Front( env ):

    if env.ID == 0:

        env.x = 0
        env.y = 10
        env.z = 1

def Place_Light_Source_To_The_Right( env ):

    if env.ID == 1:

        env.x = 10
        env.y = 0
        env.z = 1

def Place_Light_Source_To_The_Back( env ):

    if env.ID == 2:

        env.x = 0
        env.y = -10
        env.z = 1

def Place_Light_Source_To_The_Left( env ):

    if env.ID == 3:

        env.x = -10
        env.y = 0
        env.z = 1
