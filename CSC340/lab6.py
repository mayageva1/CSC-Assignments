import numpy as np
def BanditArmA(n):
    out = np.random.uniform(0,n)
    return out
def BanditArmB(n):
    if np.random.uniform(0,n)>n/2: return n/2
    return 0
def BanditArmC(n):
    h = 0
    v = 0
    for i in range(0, n):
        if np.random.uniform(0,1) >= 0.5: h += 1
        if np.random.uniform(0,1) >= 0.7: v += 1
    return h-v
    #n, p = 10, .5  # number of trials, probability of each trial
    #s = np.random.binomial(n, p, 1000)
    # result of flipping a coin 10 times, tested 1000 times.
numTrials = 100
#array for holding the winner of each round
bestResult = np.zeros(3)
#test the bandit arms a set number of times
for i in range(0, numTrials):
    #select the roll/flip parameter for the arms
    n=50
    #get the outcome from each arm
    A = BanditArmA(n)
    B = BanditArmB(n)
    C = BanditArmC(n)
    results = [A,B,C]
    #record which arm was most profitable this round
    best_index = 0
    for j in range(1, len(results)):
        if results[j] > results[best_index]:
            best_index = j
    
    # Increment the count for the best arm
    bestResult[best_index] += 1
most_profitable_arm_index = 0
for i in range(1, len(bestResult)):
    if bestResult[i] > bestResult[most_profitable_arm_index]:
        most_profitable_arm_index = i
arms = ["BanditArmA", "BanditArmB", "BanditArmC"]
print("The most profitable arm is: " + arms[most_profitable_arm_index])
#Arm A maximizes profits