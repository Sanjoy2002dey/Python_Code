def palin(a):
    a=str.upper(a)
    f=0
    n=len(a)
    for i in range(0,int(n/2),1):
        if(a[i]!=a[n-1-i]):
           f=1
           break
    if(f==0):
        print("Palindrome")
    else:
        print("Not a Palinndrome")
x=input("Enter a string: ")
palin(x)
        
