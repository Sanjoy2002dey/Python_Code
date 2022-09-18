def digiroot(a,s=0):
    x=a
    while(a!=0):
        s+=a%10
        a=a//10
    if(a==0 and s>9):
        a=s
        s=0
    print("The digital roots of ",x,"is",s)
        
x=int(input("Enter the number: "))
digiroot(x)
        
