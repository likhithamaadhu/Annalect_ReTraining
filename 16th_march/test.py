def viewDesired(n):
    list=[]
    for i in d:
        if d[i]==n:
            list.append(i)
    return list
    

d={"hello":4,"hi":1,"hai":1}
print(d)
n=int(input("Enter occurance number: "))
res=viewDesired(n)
print(res)