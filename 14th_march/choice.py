def choice(num):
    if num==1:
         s=input("Enter a string")
         r=words(s)
         print("No. of words in string : ",r)

    elif num==2:
        a=input("Enter a word: ")
        b=input("Enter a letter: ")
        r= search(a,b)
        print("{} present {} times in {}".format(b,r,a))
    elif num==0:
        exit()


def words(s):
    b=s.strip().split(" ")
    c=len(b)
    return c

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
    while True:
        print("1.Count words")
        print("2.count no.of ")
        print("0. Exit")
        print("--------------------------")
        n=int(input("Enter your choice:"))
        print("--------------------------")
        c=choice(n)


run()