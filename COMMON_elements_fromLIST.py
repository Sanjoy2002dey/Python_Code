s1=[10,20,30,40,50,60]
s2=[5,10,15,20,25,30,35,40,45,50,55,60]
s3=[15,30,45,60,75,90]
print(s1)
print(s2)
print(s3)


A=list(set(s1)&set(s2)&set(s3))
print("Common element is: ",A)
