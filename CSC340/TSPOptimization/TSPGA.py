from telnetlib import GA
from GAMember import GAMember
import copy
import random
import math
import random
import Utils
class TSPGA(object):  # Overall TSP Genetic Algorithm
    def __init__(self, pop_size=50, mutation_rate=0.02, crossover_rate=0.5,
                 dist_matrix=None, colony_id=0) -> None:
        self.population_size = pop_size
        self.population = []  # List of GAMembers
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.dist_matrix = dist_matrix
        self.best_member = None
        self.initialize_population()
        self.best_fitness = 100000
        self.colony_id = colony_id
        self.iteration = 0

    def initialize_population(self):
        self.population.clear()
        for i in range(self.population_size):
            mem = GAMember(self.dist_matrix)
            self.population.append(mem)

    def evaluate_population(self):
        for i in range(self.population_size):
            self.population[i].evaluate_member()

    def do_GA_optimization(self, max_training_iterations=2000):
        self.evaluate_population()
        self.population.sort()  # Sort population by fitness
        if self.population[0].fitness < self.best_fitness:
            self.best_fitness = self.population[0].fitness
            self.best_member = copy.deepcopy(self.population[0])
        same_count = 0
        last_best_fitness = 0

        for i in range(max_training_iterations):
            # Each loop is one generation
            self.select_population()
            self.crossover_population()
            self.evaluate_population()
            self.population.sort()

            if self.population[0].fitness < self.best_fitness:
                self.best_member = copy.deepcopy(self.population[0])
                self.best_fitness = self.population[0].fitness

            self.mutate_population()
            self.evaluate_population()
            self.population.sort()

            if self.population[0].fitness < self.best_fitness:
                self.best_member = copy.deepcopy(self.population[0])
                self.best_fitness = self.population[0].fitness

            # Uncomment the following lines to handle stagnation
            # if last_best_fitness == self.best_member.fitness:
            #     same_count += 1
            #     if same_count > 300:  # No improvement in 300 generations
            #         if len(self.population) < 200:
            #             m1 = GAMember(self.dist_matrix)
            #             self.population.append(m1)
            #             self.population_size = len(self.population)
            #         else:
            #             same_count = 0
            # last_best_fitness = self.best_member.fitness

            if i % 100 == 0:
                print('colony=', self.colony_id, ' iteration=', self.iteration,
                      ' best fitness = ', self.best_fitness)
            self.iteration += 1

        return self.best_member, self.best_fitness

    def select_population(self):
        # Drop 30% of the worst population and duplicate 30% of the best population
        start = 0
        for i in range(int(0.7 * self.population_size), self.population_size):
            self.population[i] = copy.deepcopy(self.population[start])
            start += 1

    def crossover_population(self):
        random.shuffle(self.population)  # Randomize population

        for ii in range(int(((self.crossover_rate / 2.0) * self.population_size))):
            p1 = ii  # First parent
            p2 = ii + int(0.5 * self.population_size)  # Second parent
            c1 = copy.deepcopy(self.population[p1])
            c2 = copy.deepcopy(self.population[p2])

            res3 = Utils.verify_proper_tour(self.population[p1].tour)
            res4 = Utils.verify_proper_tour(self.population[p2].tour)

            if res3 != 0:
                print('invalid tour for p1......')
            if res4 != 0:
                print('invalid tour for p2......')

            # Transfer genes to children
            gene_length = self.dist_matrix.shape[0]
            cut1 = int(math.ceil((gene_length + 1) / 4.0))
            cut2 = int(math.floor((gene_length + 1) * 3.0 / 4.0))

            d1, d2 = {}, {}

            for i in range(cut1, cut2):
                d1[c1.tour[i]] = -1
                d2[c2.tour[i]] = -1

            d1[0], d2[0] = -1, -1
            c1.tour[0] = c2.tour[0] = 0
            c1.tour[gene_length] = c2.tour[gene_length] = 0

            # Circular addition of tours
            start_pos = 1
            for i in range(1, cut1):
                for j in range(0, gene_length + 1):
                    if d1.get(self.population[p2].tour[start_pos]) != -1:
                        d1[self.population[p2].tour[start_pos]] = -1
                        c1.tour[i] = self.population[p2].tour[start_pos]
                        start_pos = (start_pos + 1) % (gene_length + 1)
                        break
                    else:
                        start_pos = (start_pos + 1) % (gene_length + 1)

            for i in range(cut2, gene_length):
                for j in range(0, gene_length + 1):
                    if d1.get(self.population[p2].tour[start_pos]) != -1:
                        d1[self.population[p2].tour[start_pos]] = -1
                        c1.tour[i] = self.population[p2].tour[start_pos]
                        start_pos = (start_pos + 1) % (gene_length + 1)
                        break
                    else:
                        start_pos = (start_pos + 1) % (gene_length + 1)

            self.population[p1] = c1
            self.population[p2] = c2

            res1 = Utils.verify_proper_tour(c1.tour)
            res2 = Utils.verify_proper_tour(c2.tour)

            if res1 != 0:
                print('invalid tour for child 1......')
            if res2 != 0:
                print('invalid tour for child 2......')

            self.population[p1].evaluate_member()
            self.population[p2].evaluate_member()

    def mutate_population(self):
        gene_length = self.dist_matrix.shape[0]
        count_to_mutate = int(self.population_size * (gene_length + 1) *
                              self.mutation_rate)

        for i in range(count_to_mutate):
            pos, popnum = 0, 0
            while pos == 0 or pos == gene_length:
                rnum = int(self.population_size * (gene_length + 1) * random.random())
                pos = rnum % (gene_length + 1)
                popnum = int(rnum / (gene_length + 1))

            doRandomExchange = True
            if random.random() < 0.7 and pos > 2:
                exchpos = pos - 1
                temp = self.population[popnum].tour[pos]
                self.population[popnum].tour[pos] = self.population[popnum].tour[exchpos]
                self.population[popnum].tour[exchpos] = temp
                doRandomExchange = False

            if doRandomExchange:
                exchpos = 0
                while exchpos in (0, gene_length + 1, gene_length):
                    exchpos = int(random.random() * (gene_length + 1))
                temp = self.population[popnum].tour[pos]
                self.population[popnum].tour[pos] = self.population[popnum].tour[exchpos]
                self.population[popnum].tour[exchpos] = temp
