'''This program creates a house using the graphics library, made by Joshua Jones'''
from graphics import *

def main():
    win = GraphWin("House", 500, 500)

    #Creates the house base
    maintext = Text(Point(250,450), "Click on lower left corner of the house frame.").draw(win)
    p1 = win.getMouse()
    maintext.setText("Click upper right corner of the house frame.")
    p2 = win.getMouse()
    Rectangle(p1,p2).draw(win)

    #create the house door
    width = (p2.x-p1.x) * .2
    maintext.setText("Click on the center of the top of the door.")
    p3 = win.getMouse()
    leftcorner =Point(p3.x-(width/2),p3.y)
    rightcorner = Point(p3.x+(width/2),p1.y)
    Rectangle((leftcorner),(rightcorner)).draw(win)

    #creates door knob
    height = p1.y - p3.y
    center = Point((p3.x+width/2)-10,(height/2)+p3.y)
    Circle(center,5).draw(win)

    #creates window
    maintext.setText("Click on the center of the window.")
    p4 = win.getMouse()
    windowwidth = width * .75
    wleftcorner = Point(p4.x-windowwidth/2,p4.y-windowwidth/2)
    wrightcorner = Point(p4.x+windowwidth/2,p4.y+windowwidth/2)
    Rectangle(wleftcorner,wrightcorner).draw(win)
    Line(Point((p4.x-windowwidth/2),(p4.y)), Point((p4.x+windowwidth/2),(p4.y))).draw(win)
    Line(Point((p4.x),(p4.y-windowwidth/2)), Point((p4.x),(p4.y+windowwidth/2))).draw(win)
    
    #creates Roof
    maintext.setText("Click on the peak of the roof.")
    UpperLeft = Point(p1.x,p2.y)
    UpperRight = p2
    p5 = win.getMouse()
    Polygon(UpperLeft,UpperRight,p5).draw(win)

    #Close win
    maintext.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
    
  

    

