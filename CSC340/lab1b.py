def ComplexCircuit(A,B):
    C = not B
    D = not(A and B)
    E = A or C
    F = not(A and B)
    G = XOR(D, E)
    H = not(G and E and F)
    J = XOR(D, G)
    K = J and H and E
    return C, D, E, F, G, H, J, K
def XOR(a, b):
    if (not a and b) or (a and not b):
        return True
    return False

A = [True, False]
B = [True, False]
for i in range(0, len(A)):
    for j in range(0, len(B)):
        print("Value of A=", A[i])
        print("Value of B=", B[j])
        C, D, E, F, G, H, J, K = ComplexCircuit(A[i], B[j])
        print("Value of C=", C)
        print("Value of D=", D)
        print("Value of E=", E)
        print("Value of F=", F)
        print("Value of G=", G)
        print("Value of H=", H)
        print("Value of J=", J)
        print("Value of K=", K)
        print("=============")
