import numpy as np
from Node import Node
import math
import matplotlib.pyplot as plt
def read_TSPLIB_data(file_name):
    node_list = []
    fobj = open(file_name,"r") 
    lines = [line for line in fobj.readlines() if line.strip()]
    num_nodes = len(lines) - 7
    fobj.close()
    dist_matrix = np.zeros((num_nodes, num_nodes))
    fobj = open(file_name,"r")
    count = 0
    for line in fobj:
        if count > 5: # first 5 lines are info
            if line[0:3] =='EOF':
                break
            parts = line.split(" ")
            node = Node(int(parts[0]), float(parts[1]), float(parts[2]))
            node_list.append(node)
        count = count + 1
 
    # compute dist_matrix
    for i in range(len(node_list)):
        for j in range(len(node_list)):
            dist_matrix[i,j] = math.sqrt((node_list[i].x - node_list[j].x)**2 +
                (node_list[i].y - node_list[j].y)**2)
    return node_list, dist_matrix
def verify_proper_tour(tour):
    all_nodes = np.ones(len(tour)-1)
    for i in range(len(tour)):
        all_nodes[tour[i]] = 0
    return np.sum(all_nodes) # should be zero if proper tour
def plot_TSP_tour(tour, node_data):
    x = []
    y = []
    for i in tour:
        x.append(node_data[i].x)
        y.append(node_data[i].y)
 
    plt.plot(x, y, 'co')
    a_scale = float(max(x))/float(100)
    # draw the tour for the TSP problem
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, 
    color ='g', length_includes_head=True)
    for i in range(0,len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width =    a_scale, color = 'g', length_includes_head = True)
 #Set axis too slightly larger than the set of x and y
    plt.xlim(-30, max(x)*1.1)
    plt.ylim(-30, max(y)*1.1)
    plt.show()