import numpy
#list of vertices
V = ['A','B','C','D','E','F']
#list of edges
E = ['AC','AD','BD','BD', 'BF', 'CA', 'CF', 'DA', 'DB', 'DF','EF','FB','FC','FD', 'FE']
def ListToAdjMatrix(V,E):
    #Iterate through the set and create a dictionary
    #The job of the dictionary is to convert letters into numbers
    #This will eventually be used to fill in the adjacency matrix
    index = 0 
    letterToNumberDict = {}
    for v in V:
        letterToNumberDict[v] = index
        index = index + 1

    #Print the key/value pairs of the dictionary to see
    #the correspondence between letters and numbers 
    #for key, value in letterToNumberDict.items() :
        #print (key, value)
    numVertex = len(V)
    #Create an empty matrix to represent the graph 
    graphMatrix = numpy.zeros((numVertex, numVertex))
    #Go through each edge pair and fill in the corresponding result 
    for e in range(0, len(E)):
        #TODO, fill in the graphMatrix based on two things
        #Use the edge list E (first) and the letterToNumberDict (second)
        vertex1 = E[e][0]
        vertex2 = E[e][1]
        index1 = letterToNumberDict[vertex1]
        index2 = letterToNumberDict[vertex2]
        graphMatrix[index1][index2] = 1
        graphMatrix[index2][index1] = 1
    return graphMatrix
graphMatrix = ListToAdjMatrix(V,E)
print(graphMatrix)


#For each node create a list that counts the number of vertices 
#that have a certain degree. For example in the previous graph 
#there are are three nodes that have degree 2 (A, B and C)
def makeDegreeListFromGraphMatrix(graphMatrix):
    #Create the list
    degreeList = []
    #Go through and count the frequency of each node 
    for i in range(0, graphMatrix.shape[0]):
       #TODO: Figure out the degree of the node and put this number 
       #in the degree list
       degree = int(numpy.sum(graphMatrix[i]))
       degreeList.append(degree)
    #TODO: After putting the degree of each node in the frequency list
    #sort the frequency list from smallest to largest
    degreeList.sort()
    return degreeList

print(makeDegreeListFromGraphMatrix(graphMatrix))

def CheckIsomorphism(VA, EA, VB, EB):
    #Convert VA and EA to matrix 
    adjMatrixA = ListToAdjMatrix(VA, EA) #TODO write this function
    #Convert the matrix to a degree list
    degreeListA = makeDegreeListFromGraphMatrix(adjMatrixA)
    #Convert VB and EB to matrix
    adjMatrixB = ListToAdjMatrix(VB, EB)
    #Convert the matrix B to a degree list
    degreeListB = makeDegreeListFromGraphMatrix(adjMatrixB)
    #TODO: Check if degree list A and degree list B are the same
    if degreeListA == degreeListB: 
        isoResult = True
    else:
        isoResult = False
    #isoResult should be true if the lists are the same and false
    #if the lists are different
    return isoResult

#List of vertices
VA = ['A', 'B', 'C', 'D', 'E', 'F']
#List of edges 
EA = ['AC','AD', 'BD', 'BF', 'CA', 'CF', 'DA', 'DB', 'DF','EF','FB','FC','FD', 'FE']
print(CheckIsomorphism(VA, EA, V, E))


#List of vertices
VB = ['H', 'B', 'J', 'D', 'K', 'F']
#List of edges 
EB = ['HJ','HD', 'BD', 'BF', 'JH', 'JF', 'DH', 'DB', 'DF','KF','FB','FJ','FD', 'FK']
print(CheckIsomorphism(VB, EB, V, E))