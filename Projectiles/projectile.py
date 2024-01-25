import math

class Projectile:
    def __init__(self,angle,velocity,height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = math.cos(theta) * velocity
        self.yvel = math.sin(theta) * velocity

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def update(self, timestep):
        self.xpos = self.xpos + self.xvel*timestep
        yvel1 = self.yvel - 9.8*timestep
        averageyvel = (self.yvel +yvel1)/2
        self.ypos = self.ypos + averageyvel * timestep
        self.yvel = yvel1

