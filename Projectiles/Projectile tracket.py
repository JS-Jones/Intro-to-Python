from projectile import Projectile

def get_input():
    angle = float(input("what is the angle of launch? "))
    initv = float(input("what is the initial velocity? "))
    inith = float(input("What is the initial height? "))
    timestep = float(input("what is the time interval for measurments? "))
    return angle, initv, inith, timestep

def main():
    angle, initv, ypos, timestep = get_input()

    cball = Projectile(angle, initv, ypos)

    while cball.getY() >= 0:
        cball.update(timestep)

    print("The cannonball went meters ", cball.getX())

main()





