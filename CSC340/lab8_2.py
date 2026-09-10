#Make the vertex class
class Vertex():
    def __init__(self, name, neighborList=None, isVisited=False):
        self.name = name
        self.neighborList = neighborList
        self.isVisited = isVisited
#Exercise 2
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
A.neighborList=[B, C, D]
B.neighborList=[A, C, D]
C.neighborList=[A, D]
D.neighborList=[A, B, C]
Graph = {"A":A, "B":B, "C":C, "D":D}
numNeighbors = 3
def TestForCompleteness(Graph, numNeighbors):
    #TODO
    #Return true if the graph is complete
    #Return false otherwise
    for v in Graph:
        if len(Graph[v].neighborList) != numNeighbors:
            return False
    return True

#Exercise 2 B
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
A.neighborList=[B, C, D]
B.neighborList=[A, C, D]
C.neighborList=[A, B, D]
D.neighborList=[A, B, C]
Graph = {"A":A, "B":B, "C":C, "D":D}
numNeighbors = 3
print(TestForCompleteness(Graph, numNeighbors))

#returns true meaning the graph is complete