import numpy as np
class GAMember():
    def __init__(self, dist_matrix) -> None:
        self.tour = [] # start and end nodes are same
        self.num_nodes = dist_matrix.shape[0] 
        self.fitness = 0
        self.dist_matrix = dist_matrix
        self.initialize_member()
        self.evaluate_member() # fitness of member
    def __str__(self):
        out = str(self.fitness) + ":"
        for node in self.tour:
            out = out + str(node) + "->"
        return out[0:len(out)-2]
 
    def __lt__(self, other):
        return self.fitness < other.fitness # to help in sorting members
    def initialize_member(self):
        random_perm = np.random.permutation(np.arange(1,self.num_nodes))
        self.tour = list(random_perm)
        self.tour.insert(0,0) # first node is 0
        self.tour.append(0) # last node in tour is 0
 
    def evaluate_member(self):
        prev_node = 0 
        cost = 0
        for i in range(1,len(self.tour)-1): # start node is 0
            cost = cost + self.dist_matrix[self.tour[prev_node], self.tour[i]]
            prev_node = i
        cost = cost + self.dist_matrix[self.tour[prev_node], 0] 
        self.fitness = cost
