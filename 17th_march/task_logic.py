from task import Task
d={}
def check(n):
    if d.get(n) is not None:
        return True
    else:
        return "TaskID not Found"

def add(n,t):
    d[n]=t
    return "Task added"

def update(n,update_task):
    d[n]=update_task
    return "Task updated"

def view(n):
    try:
        return d[n]
    except:
        return "No such Task"

def rem(n):
    try:
        del d[n]
        return "Task deleted"
    except:
        return "No such Task"   
        
def viewAll():
    return d

