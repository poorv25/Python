n=int(input("Enter value"))
m=n*10
count=1
for i in range(1,11):
      print(n,"*",i,"=",n*i)
print("\n")      
for i in range(n,m+1,n):
    print("{}*{}={}".format(n,count,i))
    count=count+1
