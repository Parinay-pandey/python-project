import math
#using import math function
a=list(map(int,input("Enter the number: ").split(",")))
#Taking user input in form of number and converting it into list using split function.
def perfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
#this function use to check where a number occurs in fibonacci series
def fibonacci(b):
    return perfectsquare(5*b*b+4) or perfectsquare(5*b*b-4)

for i in a:
    if fibonacci(i)==True:
#for i in fibonacci series it will be True , it will print is valid.
        print(i,"is valid")
    else:
        print(i,"is invalid")
#For i not in Fibonacci series , it will print Invalid.

