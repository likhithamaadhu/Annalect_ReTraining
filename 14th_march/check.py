def check(num):
    if num > 0:
        return "Positive number"
    elif num == 0:
        return "Zero"
    else:
        return "Positive number"

def run():
    a=float(input("Enter a number :"))
    r= check(a)
    print("{} is {}".format(a,r))

run()