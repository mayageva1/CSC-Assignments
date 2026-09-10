def FindMax(n):
    max = n[0]
    for i in range(1,len(n)):
        if n[i] > max:
            max = n[i]
    return max