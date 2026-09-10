def FermatTestForPrime(q, k):
    for num in k:
        if pow(num, q - 1) -1 % q !=0:
            return False
    return True


print(FermatTestForPrime(221, [2,24]))
print(FermatTestForPrime(221, [38])) 
