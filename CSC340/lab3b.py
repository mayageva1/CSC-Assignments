#Generate all prime numbers up to n
##Using the sieve of Eratosthenes algorithm
import math
def GetAllPrimesUsingSieveOfE(n):
    #generate a list of n numbers
    numberList = list(range(2, n))
    #Generate a second list to keep track of whether the number is prime or not
    isPrime = [True] * (n - 2)
    #Go through and set the list isPrime to be true if the element is prime
    for i in range(len(numberList)):
            if (math.factorial(numberList[i]-1) +1) % numberList[i] != 0:
                isPrime[i] = False
    primeNumberList = []
    for i in range(len(numberList)):
        if isPrime[i]:
            primeNumberList.append(numberList[i])
    return primeNumberList

print(GetAllPrimesUsingSieveOfE(30))