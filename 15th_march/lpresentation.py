from llogic import fill,view,change,rem,asc,des,occur
exit = False
def run():
   
    while exit == False:
        # print("cgfvh",exit)
        print("------------------------")
        print("1.Fill up list with 10 random numbers")
        print("2.view all the list")
        print("3.change the number in list")
        print("4.Remove element in the list")
        print("5.Sort in Ascending order")
        print("6.Sort in Descending order")
        print("7.Occurances of numbers")
        print("0.Exit")
        print("------------------------")
        c=int(input("Enter your choice: "))
        print("------------------------")
        choice(c)

def choice(c):
    if c==1:
        fill()
        print("Done")
    elif c==2:
        res=view()
        print(res)
    elif c==3:
        a=int(input("Enter a existing number: "))
        b=int(input("Enter a number to replace: "))
        res=change(a,b)
        print(res)
    elif c== 4:
        a=int(input("Enter number to remove: "))
        res=rem(a)
        print(res)
    elif c==5:
        print("Ascending order:")
        res=asc()
        print(res)
    elif c==6:
        print("Descending order:")
        res=des()
        print(res)
    elif c==7:
        print("Occurances of the numbers:")
        res=occur()
        for i in res:
            print(i,"-->",res[i])
    elif c==0:
        global exit

        exit=True
        print("Exited!!")

