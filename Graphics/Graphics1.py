import turtle

def one_rectangle(size1, size2):
    turtle.forward(size1)
    turtle.left(90)
    turtle.forward(size2)
    turtle.left(90)
    turtle.forward(size1)
    turtle.left(90)
    turtle.forward(size2)
    turtle.left(90)
    
def rectangle(size, depth):
    turtle.color("#04B45F")
    turtle.down()
    if depth == 0:
        pass
    else:
        one_rectangle(size, abs(size/2))
        turtle.forward(size)
        rectangle(size/2, depth-1)
        turtle.forward(-size)
        rectangle(-size/2, depth-1)

        
##        print(depth, size)
##        one_rectangle(size, abs(size/2))
##        rectangle(-size/2, depth-1)
##        print(depth, size)
##        turtle.up()
##        turtle.forward(size*2)
##        print("move forward ", size*2)
##        turtle.down()
##        rectangle(size/2, depth-1)
        
    
def init(size):
    turtle.reset()
    turtle.setup(600,600)
    turtle.setworldcoordinates (-size, -size, 2*size, size)
    turtle.speed(0)
    turtle.up()
    turtle.pensize(2)


def main():
    depth = int(input("What is your depth? "))
    size = int(input("what is your size? "))

    init(size)
    rectangle(size, depth)
    turtle.done()
    
main()
