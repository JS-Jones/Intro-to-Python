import statistics
import random

def question1():
    sentences = []
    print("enter something")
    while True:
        x = input()
        if x == "":
            break
        else:
            sentences.append(x)
    
    for x in sentences:
        print(x.upper())

def question2():
    for x in range(3):
        name = input("What is my name? ")
        if name == "Josh":
            print("Yes! My name is Josh!")
            break
        elif name != "Josh" and x==2:
            print("You ran out of chances.")
        elif name:
            print("Your are wrong!")
            
def question3():
    correct = 445
    num = int(input("Guess a number between 1 and 1000: "))

    while True:
        if num < correct:
            print("Too low!")
            num = int(input("Guess again: "))
        elif num >correct:
            print("Too high!")
            num = int(input("Guess again: "))
        else:
            print("Wow you got it!")
            break
            
def question4():
    start = float(input("what is the starting odomerter? "))
    mpgtotal = []

    
    while True:
        x= input("what is the odometer reading and gallons used? ")
        if x == "":
            break
        else:
            legs = x.split(" ")
            odometer = float(legs[0])
            gallons = float(legs[1])

            distance = odometer - start
            mpg = distance/gallons

            mpgtotal.append(mpg)
            
    for i in mpgtotal:
        print(i)

    print(statistics.mean(mpgtotal))
        
def question5():
    correct = random.randint(1,1000)
    num = int(input("Guess a number between 1 and 1000: "))

    while True:
        if num < correct:
            print("Too low!")
            num = int(input("Guess again: "))
        elif num >correct:
            print("Too high!")
            num = int(input("Guess again: "))
        else:
            playagain = input("Wow you got it! Do you want to play again? ")
            if playagain == "yes":
                question5()
            else:
                break
        
        
    




                      
