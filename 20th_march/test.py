from emp import Employee,EmployeeStatus
emp1=Employee(1,"raj",23,1)
emp2=Employee(2,"raghu",25,1)
emp3=Employee(3,"ram",22,2)
emp4=Employee(4,"latha",21,2)
emp5=Employee(5,"Reshma",22,3)

# d={emp1.empno:emp1,emp2.empno:emp2,emp3.empno:emp3,emp4.empno:emp4,emp5.empno:emp5}

es1=EmployeeStatus(0,"Not Found",emp1)
es2=EmployeeStatus(1,"Found",emp2)
es3=EmployeeStatus(0,"Not Found",emp3)
es4=EmployeeStatus(1,"Found",emp4)
es5=EmployeeStatus(0,"Not Found",emp5)

d={emp1.empno:es1,emp2.empno:es2,emp3.empno:es3,emp4.empno:es4,emp5.empno:es5}


# def viewDetails(n):
#     if d.get(n) is not None:
#         r=d[n]
#         if r.statusCode==1:
#             return r.empObj
#         else:
#             return None

def viewEmployees(n):
    l=[]
    for i in d.values():
        if i.empObj.deptId==n:
            l.append(i.empObj.name)
    return l
    
    
    

viewEmployees(1)