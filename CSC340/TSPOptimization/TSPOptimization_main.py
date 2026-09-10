import sys
from GAMember import GAMember
import Utils
import copy
from TSPGA import TSPGA
def main():
    node_list, dist_matrix = Utils.read_TSPLIB_data("data/berlin52.txt")
    tspGA = TSPGA(pop_size=100, mutation_rate=0.02, crossover_rate=0.50, dist_matrix=dist_matrix, colony_id=0)
    max_training_iterations = 3000
    best_member, best_fitness = tspGA.do_GA_optimization(max_training_iterations)
    valid_tour = Utils.verify_proper_tour(best_member.tour)
    if valid_tour == 0:
        print('best member tour is valid, all nodes exist..')
    print(best_member)
    Utils.plot_TSP_tour(best_member.tour, node_list)
if __name__ == "__main__":
 sys.exit(int(main() or 0))