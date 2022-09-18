s1=[10,20,30,40,50]
s2=[5,10,15,20,25,30,35,40,45,50]
s3=[20,40,60,80]
print(s1)
print(s2)
print(s3)
A=list(set(s1)& set(s2)& set(s3))
print("common elements: ",A)
