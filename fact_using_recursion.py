def factorial_recursion(n):
    if (n==1):
        return (1)
    else:
        return n*factorial_recursion(n-1)
number = int(input("enter the number "))
print("factorial using alternative method ",factorial_recursion(number))
