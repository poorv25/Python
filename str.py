a=input("enter a string : ")
b="the length of our string is "
l=len(a)
print("the length of our string is "+str(l))
for i in range(l):
    print(a[i],": is at index :",i)
