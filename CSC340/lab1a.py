#XOR function
def XOR(a, b):
    if (not a and b) or (a and not b):
        return True
    return False

#Define all possible values of A and B
A = [True ,False]
B = [True, False]
#For each possible value of A and B, print the XOR gate output
for i in range(0, len(A)):
    for j in range(0, len(B)):
        output = XOR(A[i], B[j])
        print("A=", A[i], "B=", B[j], "XOR(A,B)=", output)
