def rev(a,s):
    if a==0:
        return s
    else:
        return(rev(a//10,s*10+a%10))
x=int(input("Enter the number: "))
print ("The reverse of",x,"is",rev(x,0))
