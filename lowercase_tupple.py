list=[('sanjoy','Rahul'),('rohit','Bravo')]
s=[]
for i in list:
    for j in i:
        if j.islower():
            s.append(j)
print(tuple(s))
