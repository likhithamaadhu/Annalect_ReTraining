def cal(n):
    r= n**0.5
    return r

def sqrt():
    a=int(input("Enter a number:"))
    result=cal(a)
    print(("The squareroot of {} is {}").format(a,result))

sqrt()