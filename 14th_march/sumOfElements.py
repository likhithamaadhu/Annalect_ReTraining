def sum(l):
    s=0
    for i in l:
        s=s+i
    return s
    
def run():
    l=list(map(int,input("Enter list of elements").split()))
    r=sum(l)
    print("Sum : ",r)
run()
