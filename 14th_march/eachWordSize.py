def eachWordSize(s):
    l=[]
    for i in s:
        l.append(len(i))
    return l
def run():
    s=["I am Likhitha","Lucky","This is ReTraining"]
    r=eachWordSize(s)
    print(r)
    
run()

