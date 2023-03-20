def search(x,y):
    c=0
    for i in x:
        if i==y:
            c+=1
    if c==0:
        return -1
    else:
        return c
        


def run():
    a=input("Enter a word: ")
    b=input("Enter a letter: ")
    r= search(a,b)
    print("{} present {} times in {}".format(b,r,a))

run()