import itertools
a=set()
n=2
y=int(input("Enter the no of the element: "))
for i in range (y):
    x=input("Enter the item: ")
    a.add(x)
print("The set is : ",a)
p=list(itertools.combinations(a,n))
print(p)
