def words(s):
    b=s.split(" ")
    c=len(b)
    return c
    

def run():
    a=input("Enter a string")
    r=words(a)
    print("No. of words in string : ",r)
    
run()