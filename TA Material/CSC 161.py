''' CSC 161 Exam Review
1) Go over quick Sort and Merge Sort

- How many iterations of binary search do you need to find an item in a list of 64 items
- Which is fastest merge sort, selection sort, linear search, binary search


2) Basic Fibonacci Sequence '''

def fib(n): # Recurrsive Method
    if (n==1): # Base Case --> Always
        return 1
    elif (n==0): # Base Case 2
        return 0
    return fib(n-1) + fib(n-2) # Calls itself

''' Fibonacci Review Work
    fib(3):
        return fib(2) + fib(1) --> 1 + 1 = 2
    
    fib(2):
        reuturn fib(1) + fib(0) --> 1 + 0 = 1

    fib(1): return 1

    fib (0): reutrn 0


3) Reivew Material Questions
- What does 10.0/2 = ?

- What is 10%5
- What is 5%2

- What will the below code print?
'''
def Q1(num):
    x = num
    if x == 5:
        print("The Answer is 5")
    elif x == 1:
        print("The Answer is 1")
        
    if x > 3:
        print(x)
        Q1(x-1)

x = 10
Q1(x)






'''
- Write a for loops that generates this output:
    5
    4
    3
    2
    1
    0







    [dog, cat]
- What list method can I use to add an item to the end of list? --> append()
    - add an item to a certain index of the list --> insert(1, "Hamster")
    - remove a specific item using the item name --> remove("cat")
    - remove a specific list item based on its index --> pop(1)
    - Replace dog with hamster --> list[0] = "Hamster"






- Difference between a list [] and a dictionary {dog: 2
                                                cat: 2}?
                            


- Someone explain to me how to create the basic structure of a Class. 




- Create a class called Student that takes in GPA and Name. Create a getGPA and
setGPA method. How to print custom things


    def __repr__(self):
        print(self.name + " " + str(self.gpa))


- for loops inside another for loop?

- Random.random vs Random.randint (5, 10)

- Know algorithm design: intractable, halting problem, etc




        
