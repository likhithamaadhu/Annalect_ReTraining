def add(a,b):
    r=a+b
    return r

def show():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=add(a,b)
    print(("The addition of {} and {} is {}").format(a,b,c))

show()