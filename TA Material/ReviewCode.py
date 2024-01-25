''' CSC 161 Review:

Split seperates a string while sep combines them

Files:
file = input("Please enter the file name: ")
    infile = open(file, "r")
    filelist = infile.readlines()

Random:
import random
random.random() - gives a val between 0 and 1
random.randint(x,y) - gives an int between x and y (both included)

Classes:
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

Exceptions:
def get_input(): 
    while True:
        try: <----
            n = int(input("Please enter a positive integer: "))
            if n < 0:
                print("The integer must be positive.")
            else:
                 return n 
        except(ValueError): <-----
            print("Bad input!")
-Basically an if (try) and else (except) statement


Object Oriented Design:
- Make sure of classes such as GraphWin, only know the interface of the code (an outline of it)
1. Look for object candidates - look for nouns that can't simply be expressed as numbers or strings
2. Identify instance variables
3. Think about interfaces
4. Refine the nontrivial methods
5. Design iteratively
6. Try out alternatives
7. Keep it simple
- Encapsulation - helps with code reuse
- Polymorphism - what an object does depends on the class of the object
- Inheritance - allows a class to borrow behavior from another class - have all the methods from the superclass


Algorithm Design:
- constraints of code is the speed at which writen and how it runs
- Searching:
    - Linear Search - check the first item and see if it matches, if not, move on to the next
    - Sorted Search/Binary Search - guess a number in the middle in a sorted list and see if you're lower or higher
- Empirically (actuallly time of how long it takes)
- Analytically (how many steps are taken by each algorithm)
- Linear search takes n/2 while binary search takes log(n)
- Recursive - calling the same function inside the function, its important to have a base case to avoid infinite loops
- Sorting:
    - Selection Sort - find the smallest element in the list and put it at the front and then sort the list starting from the second element
    - Merge Sort - splits the list in halves, sorts each half, merge the halfs together
        - Make sure there is a BASE CASE --> works for a list of 1 value
        - Merge sort takes n*log(n)
    - Quick Sort - pick an element as the pivot and arrent the rest in relation to the pivot
        - can take anywhere from nlogn to n^2
    - Tim Sort - fastest and what python uses
        
Hard Problems:
- No efficient Solutions - hardness refers to number of steps to take in relation to the size of the input
- 2^n takes a lot more time than n^2
- Intractable - can solve a problem, but it takes way too much time
- Halting Problem - can't develop a program that detetcs infinite loop, results in total contradiction
- P vs NP: P is the set of problems that are efficiently solvable while NP is that we come up with a solution slowly
- If P = NP, then NP hard problems do have efficient solutions (we just don't know them), but if they don't equal, then they do not hava an efficient solution.
- Usually P != NP



