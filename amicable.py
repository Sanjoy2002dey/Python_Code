def fact(a):
    s=0
    for i in range(1,int(a/2)+1,1):
        if(a%i==0):
            s=s+i
    return s
def amicable(a,b):
    if(fact(a)==b) and (fact(b)==a):
        print("AMICABLE number")
    else:
        print("NOT AN AMICABLE number ")
x=int(input("Enter the first number"))
y=int(input("Enter the second number "))
amicable(x,y)
