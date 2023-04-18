list=(2,3,-4,5,-3,7)
x=tuple(filter(lambda i:i>0,list))
y=tuple(filter(lambda i:i<0,list))
print("positive elements in the tuple are: ",x)
