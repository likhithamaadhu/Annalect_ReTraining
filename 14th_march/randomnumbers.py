import random

def randomnum(a,b):
    l=[random.randint(a,b) for i in range(11)]
    return l
    

def run():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    r=randomnum(a,b)
    print("Random number list: ",r)

run()

