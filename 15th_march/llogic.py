import random
from collections import Counter
l=[]
def fill():
    for i in range(10):
        l.append(random.randint(1,100))

def view():
    return l

def change(a,b):
    if a not in l:
        return "existing number not present"
    elif b in l:
        return "new number already present"
    else:
        index=l.index(a)
        l[index]=b
        return "Replaced"

def rem(a):
    if a in l:
        l.remove(a)
        return "Removed"
    else:
        return "Num not present"
    
def asc():
    l.sort()
    return l

def des():
    l.sort(reverse=True)
    return l

def occur():
    d=Counter(l)
    return d
    



    