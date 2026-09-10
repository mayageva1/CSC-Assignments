#Make the vertex class
class Vertex():
    def __init__(self, name, neighborList=None, isVisited=False):
        self.name = name
        self.neighborList = neighborList
        self.isVisited = isVisited
#Create the vertices
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
#Set up the edges connecting vertices 
A.neighborList=[B, D]
B.neighborList=[A, C]
C.neighborList=[B, D]
D.neighborList=[C, E]
E.neighborList=[A, D]
#Here the graph is represented as a dictionary
Graph = {"A":A, "B":B, "C":C, "D":D, "E":E}

def dfs(Graph, inputVertexName, count):
    #TODO
    #Mark the inputVertex as visited
    Graph[inputVertexName].isVisited = True
    #Update the count variable
    count += 1
    #Go through all neighbors of the inputVertex
    for v in Graph[inputVertexName].neighborList:
        #TODO
        #Check if v has been visited yet, if not call dfs on v
        if v.isVisited == False:
            count = dfs(Graph, v.name, count)
    return count 

def CheckForConnectedGraph(Graph, inputVertexName, numNodes):
    #TODO set the count variable to 0
    count = 0
    count = dfs(Graph, inputVertexName, count)
    #TODO: check if count matches the numNodes
    if count == numNodes:
        return True
    else:
        return False
    #Return true if graph is connected, otherwise return false

#An example function call 
numNodes = 5
print(CheckForConnectedGraph(Graph, "A", numNodes))
