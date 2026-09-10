#Excercise 1

def FibonacciFunction(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return FibonacciFunction(n-1)+FibonacciFunction(n-2)
    
assert(FibonacciFunction(10)==55)
print("Passed test 1")

#Excercise 2 part a
#print(FibonacciFunction(40))
#The code actually takes a while to computer the Fibonacci of 40.
#This is because the code is recursive, so the function is getting called 40 times
#Which takes a lot of time and processing to compute

#Excercise 2 part c:
def FibonacciFunctionNR(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n+1):
            temp = a
            a = b
            b = b+temp
        return b
            
assert(FibonacciFunctionNR(10) == 55)
print("Passed test 2")    
#This code runs much faster because the function only runs twice
# The thing that is getting iterated is the for loop
# It is much less processing for a computer to run a for loop 40 times rather
# than an entire function 40 times        
            
#Excercise 2 Part E

##from sympy import *
##A= Symbol('A')
##B= Symbol('B')
##k= Symbol('k')
##F = (A**(k-1)*(1+A)-B**(k-1)*(1+B))
##F = expand(F)
##pprint(F)