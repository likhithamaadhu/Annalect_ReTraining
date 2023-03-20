def mostOccured(x):
    counter=0
    result=x[0]

    for i in x:
        curr_frequency = x.count(i)
        if curr_frequency>counter:
            counter=curr_frequency
            result=i
    return result

def run():
    x=list(map(int,input("Enter numbers: ").split()))
    r=mostOccured(x)
    print("Most occured is:",r)

run()