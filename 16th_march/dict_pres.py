from dict_logic import add,view,viewAll,viewDesired
exit=False
def run():
    while exit==False:
        print("---------------------")
        print("1.Add a word")
        print("2.View only the words")
        print("3.View all words with its occurance")
        print("4.View all words By asking their occurance")
        print("0.Exit")
        print("---------------------")
        c=int(input("Enter your choice: "))
        print("---------------------")
        choice(c)

def choice(c):
    if c==1:
        w=input("Enter the word: ")
        res=add(w)
        print()
        print(res)
    elif c==2:
        res=view()
        print(res)
    elif c==3:
        res=viewAll()
        for key,value in res.items():
            print(key,"-->",value)
    elif c==4:
        n=int(input("Enter occurance number: "))
        res=viewDesired(n)
        if not res:
            print()
            print("Given value not present")
        else:    
            for i in res:
                print(i,"occured",n,"times")
            # for i in res:
            #     print(i,end=" ")
            # print("occured",n,"times")
    elif c==0:
        global exit

        exit=True