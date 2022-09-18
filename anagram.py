a=input("Enter the first strng: ")
a=str.upper(a)
b=input("Enter the second string: ")
b=str.upper(b)
if(sorted(a)==sorted(b)):
    print("Anagram string")
else:
    print("Not Anagram string")

