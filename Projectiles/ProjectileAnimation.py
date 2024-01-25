from projectile import Projectile
from graphics import *

class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle,velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()


def main():
    win = GraphWin("Projectile Animation", 640, 480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    for x in range(0, 210, 50): #set up grid
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)

    while True:
        angle = float(input("Enter an angle, or -1 to quit: "))
        if(angle == -1):
            break
        vel = float(input("Enter velocity: "))
        height = float(input("Enter height: "))
        shot = ShotTracker(win, angle, vel, height)
        while (0 <= shot.getY() and -10 < shot.getX() and shot.getX() <= 210):
            shot.update(1/50)
            update(50)
    win.close()

main()
