from task_logic import check,add,update,view,rem,viewAll
from task import Task

exit=False
def run():
    while exit==False:
        print("-------------------------------")
        print("****Main Menu****")
        print("1.enter taskID")
        print("2.View All tasks")
        print("0.Exit")
        print("-------------------------------")
        c=int(input("Enter your choice: "))
        print("-------------------------------")
        choice(c)

def choice(c):
    if c==1:
       global n
       n=int(input("Enter taskID: "))
       task(n)
        # flag=0
        # if ch==True:
        #     while flag==0:
        #         print("***** Sub Menu *****")
        #         print("1.Update Task Information")
        #         print("2.View Task Information")
        #         print("3.Remove Task Information")
        #         print("0.Back to Main Menu")
        # else:
        #     #  print("TaskID not Found")
        #      name=input("Enter task name: ")
        #      des=input("Enter Description: ")
        #      prio=int(input("Enter Priority: "))
        #      a=Task(n,name,des,prio)
        #      add(a)
        #      flag=1
    
    elif c==2:
        res=viewAll()
        print(res)
    elif c==0:
        global exit

        exit = True
flag=0
def task(n):
    t=check(n)
    if t==True:
        print("Task found")
        while flag==0:
            print("-------------------------------")
            print("***** Sub Menu *****")
            print("1.Update Task Information")
            print("2.View Task Information")
            print("3.Remove Task Information")
            print("0.Back to Main Menu")
            print("-------------------------------")
            c1=int(input("Enter your choice: "))
            print("-------------------------------")
            choice1(c1)
    else:
        print(t)
        print("create new task")
        name=input("Enter task name: ")
        des=input("Enter Description: ")
        prio=int(input("Enter Priority: "))
        t=Task(name,des,prio)
        res=add(n,t)
        print(res)
        # flag=1

def choice1(c1):
    if c1==1:
        u_n=input("Enter name to update:")
        u_d=input("Enter description to update:")
        u_p=int(input("Enter priority ot update:"))
        t=Task(u_n,u_d,u_p)
        res=update(n,t)
        print(res)
    elif c1==2:
        res=view(n)
        print(res)
    elif c1==3:
        res=rem(n)
        print(res)
    elif c1==0:
        global flag
        flag = 1
