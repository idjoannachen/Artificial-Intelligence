#!/usr/bin/env python3

# Please feel free to modify any part of the code or add any functions, or modify the argument
# of the given functions. But please keep the name of the given functions

# Please feel free to import any mathematical libraries you need.

# You are required to finish the genetic_algorithm function, and you may need to complete crossover, mutate and select.

import matplotlib.pyplot as plt
import random
import numpy as np

def crossover(old_gen, probability_crossover):
    #TODO START
    new_population = []
    for i in range(int(len(old_gen) / 2)): # 100/2 = 50, range = 0,...,49 = i. Take a pair of gene.
        gen1 = old_gen[i*2]
        gen2 = old_gen[i*2 + 1]

        if random.random() > probability_crossover: # if random > prob_crossover, no change to gene. if <, crossover
            new_population.append(gen1)
            new_population.append(gen2)
            continue

        two_pt1 = 0
        two_pt2 = 0
        while two_pt1 == two_pt2:
            two_pt1 = random.randint(0, 29)
            two_pt2 = random.randint(0, 29)
            # first position should be less than second position
            if two_pt1 >= two_pt2:
                two_pt1, two_pt2 = two_pt2, two_pt1
        # two pt crossover
        new_gen1 = gen1[:two_pt1] + gen2[two_pt1:two_pt2] + gen1[two_pt2:]
        new_gen2 = gen2[:two_pt1] + gen1[two_pt1:two_pt2] + gen2[two_pt2:]

        new_population.append(new_gen1)
        new_population.append(new_gen2)

    #TODO END
    return new_population

def mutate(old_gen, probability_mutation):
    #TODO START
    new_population = []
    for j in range(len(old_gen)):
        old_gene_j = old_gen[j]
        new_gene_j = ""
        for i in range(len(old_gene_j)):
            old_gene1 = int(old_gene_j[i])
            if random.random() < probability_mutation:
                if i % 3 == 0:
                    new_gene1 = ((random.randint(1, 3) + old_gene1 - 1) % 4) + 1  # from 1-4
                else:
                    new_gene1 = (random.randint(1, 8) + old_gene1) % 10 # from 0-9
                new_gene_j += str(new_gene1)
            else:
                new_gene_j += old_gene_j[i]

        new_population.append(new_gene_j)

    #TODO END
    return new_population

def select(old_gen, fitness):
    #TODO START
    prob_list = []
    indices = np.argsort(fitness) # ascending

    denominator = sum(range(len(old_gen)))
    for rank in range(len(old_gen)):
        prob = rank/denominator
        prob_list.append(prob)

    new_population = []
    for i in range(len(old_gen)):
        one_hot_enc = np.random.multinomial(1, prob_list)
        tuple1 = np.nonzero(one_hot_enc)
        new_gene = old_gen[indices[tuple1[0][0]]]
        new_population.append(new_gene)

    #TODO END
    return new_population

def genetic_algorithm(population, food_map_file, max_generation, probability_crossover, probability_mutation):
    #TODO START
    stats = [] # stats of each generation of the whole population

    food_map, map_size = get_map(food_map_file)
    for i in range(max_generation):
        # calculate fitness and food map for each individual.
        fitnesses = []
        max_fitness = -1
        max_gene = ""
        max_food_map_trial = ""

        for individual in population:
            food_map_trial, individual_fitness = ant_simulator(food_map, map_size, individual)
            fitnesses.append(individual_fitness)
        stats.append([min(fitnesses), max(fitnesses), sum(fitnesses) / len(fitnesses)])
        print(len(stats), stats[-1])

        new_population = select(population, fitnesses) # subset population based on fitness
        new_population = crossover(new_population, probability_crossover)
        new_population = mutate(new_population, probability_mutation)
        population = new_population

    for individual in population:
        food_map_trial, individual_fitness = ant_simulator(food_map, map_size, individual)
        if max_fitness < individual_fitness:
            max_fitness = individual_fitness
            max_gene = individual
            max_food_map_trial = food_map_trial

    return max_fitness, max_gene, max_food_map_trial, stats, population
    #TODO END

def initialize_population(num_population):
    # 100 ants, each has their own gene. gene has total 10 states, each state has 3 digits
    #  (so one ant has a 30-digit gene). we want to initilize individual gene (30 digits)

    #TODO START
    population = [] # 100 ants

    # 10 states, each state includes 3 digits. so every three digits represent a state:
    # if it's digit #1, take 1-4
    # state digit #2, false
    # state digit #3, true
    # ...

    for i in range(num_population):
        each_gene = [""] * 10

        for k in range(10):  # from 0-9 (for each state)
            state = [""] * 3
            for j in range(3):  # 0,1,2 (take three digits)
                if j == 0:
                    state[j] = str(random.randint(1, 4))
                else:
                    state[j] = str(random.randint(0, 9))
            full_state = "".join(state)
            each_gene[k] = full_state
        full_gene = "".join(each_gene)

        population.append(full_gene) # each ant will be assigned individual gene
    #TODO END
    return population

def ant_simulator(food_map, map_size, ant_genes):
    """
    parameters:
        food_map: a list of list of strings, representing the map of the environment with food
            "1": there is a food at the position
            "0": there is no food at the position
            (0, 0) position: the top left corner of the map
            (x, y) position: x is the row, and y is the column
        map_size: a list of int, the dimension of the map. It is in the format of [row, column]
        ant_genes: a string with length 30. It encodes the ant's genes, for more information, please refer to the handout.
    
    return:
        trial: a list of list of strings, representing the trials
            1: there is food at that position, and the spot was not visited by the ant
            0: there is no food at that position, and the spot was not visited by the ant
            empty: the spot has been visited by the ant
        fitness: fitness of ant

    It takes in the food_map and its dimension of the map and the ant's gene information, and return the trial in the map
    """

    step_time = 200

    trial = [] # copies food map,can change entry
    for i in food_map:
        line = []
        for j in i:
            line.append(j)
        trial.append(line)

    position_x, position_y = 0, 0
    orientation = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # face down, left, up, right
    fitness = 0
    state = 0
    orientation_state = 3
    gene_list = [ant_genes[i: i + 3] for i in range(0, len(ant_genes), 3)] # split 30 digits into 10 states

    for i in range(step_time): # run 200 times and how many food get ate
        if trial[position_x][position_y] == "1": # if food, fitness+1, set current position as no food
            fitness += 1
        trial[position_x][position_y] = " "

        sensor_x = (position_x + orientation[orientation_state][0]) % map_size[0] # excess map size -> take mod
        sensor_y = (position_y + orientation[orientation_state][1]) % map_size[1]
        sensor_result = trial[sensor_x][sensor_y] # if current orientation has food

        # switch state
        if sensor_result == "1":
            state = int(gene_list[state][2]) # digit 0 - 9
        else:
            state = int(gene_list[state][1]) # digit 0, 1, 2

        action = gene_list[state][0]

        if action == "1":  # move forward
            position_x = (position_x + orientation[orientation_state][0]) % map_size[0]
            position_y = (position_y + orientation[orientation_state][1]) % map_size[1]
        elif action == "2":  # turn right
            orientation_state = (orientation_state + 1) % 4 # clockwise rotate - mod 4 bc there are 4 orientations
        elif action == "3":  # turn left
            orientation_state = (orientation_state - 1) % 4 # counter clockwise rotate
        elif action == "4":  # do nothing
            pass
        else:
            raise Exception("invalid action number!")

    return trial, fitness # food map state & fitness (# of food is ate)


def get_map(file_name):
    """
    parameters:
        file_name: a string, the name of the file which stored the map. The first line of the map is the dimension (row, column), the rest is the map
            1: there is a food at the position
            0: there is no food at the position
    
    return:
        food_map: a list of list of strings, representing the map of the environment with food
            "1": there is a food at the position
            "0": there is no food at the position
            (0, 0) position: the top left corner of the map
            (x, y) position: x is the row, and y is the column
        map_size: a list of int, the dimension of the map. It is in the format of [row, column]
    
    It takes in the file_name of the map, and return the food_map and the dimension map_size
    """
    food_map = []
    map_file = open(file_name, "r")
    first_line = True
    map_size = []

    for line in map_file:
        line = line.strip()
        if first_line:
            first_line = False
            map_size = line.split()
            continue
        if line:
            food_map.append(line.split())
    
    map_file.close()
    return food_map, [int(i) for i in map_size]

def display_trials(trials, target_file):
    """
    parameters:
        trials: a list of list of strings, representing the trials
            1: there is food at that position, and the spot was not visited by the ant
            0: there is no food at that position, and the spot was not visited by the ant
            empty: the spot has been visited by the ant
        taret_file: a string, the name the target_file to be saved

    It takes in the trials, and target_file, and saved the trials in the target_file. You can open the target_file to take a look at the ant's trial.
    """
    trial_file = open(target_file, "w")
    for line in trials:
        trial_file.write(" ".join(line))
        trial_file.write("\n")
    trial_file.close()

if __name__ == "__main__":
    #TODO START
    # You will need to modify the parameters below.
    # The parameters are for references, please feel free add more or delete the ones you do not intend to use in your genetic algorithm

    population = initialize_population(100)
    food_map_file = "muir.txt"
    max_generation = 200
    probability_crossover = 0.1
    probability_mutation = 0.02
    max_fitness, max_gene, max_food_map_trial, stats, population = genetic_algorithm(population, food_map_file, max_generation,
                                                                                  probability_crossover, probability_mutation)

    display_trials(max_food_map_trial, "max_food_map_trial.txt")

    plt.figure(1)
    xs = [i for i in range(len(stats))]
    ys = [i[1] for i in stats]
    plt.plot(xs, ys, marker = "*")
    plt.xlabel("Generation")
    plt.xlim(0, 200)
    plt.ylim(0, max(ys))
    plt.ylabel("Max Fitness")
    plt.savefig("Generation vs. Max Fitness.png")

    plt.figure(2)
    fitness_santafe = []
    fitness_muir = []

    food_map_santafe, map_size_santafe = get_map("santafe.txt")
    food_map_muir, map_size_muir = get_map("muir.txt")

    for individual in population:
        trial, fitness_s = ant_simulator(food_map_santafe, map_size_santafe, individual)
        trial, fitness_m = ant_simulator(food_map_muir, map_size_muir, individual)
        fitness_santafe.append(fitness_s)
        fitness_muir.append(fitness_m)

    xs_muir = [i for i in range(len(fitness_muir))]
    xs_santafe = [i for i in range(len(fitness_santafe))]
    plt.plot(xs_muir, fitness_muir, marker="*", color="red", label="Muir")
    plt.plot(xs_santafe, fitness_santafe, marker="*", color="blue", label="Santa Fe")
    plt.xlabel("Individuals in the final generation ")
    plt.xlim((0, 100))
    plt.ylim((0, max(max(fitness_muir), max(fitness_santafe)) ))
    plt.ylabel("Fitness")
    plt.legend()
    plt.savefig("Performance Comparison.png")

    #TODO END

    # # Example of how to use get_map, ant_simulator and display trials function
    # food_map, map_size = get_map("muir.txt")
    # ant_genes = "335149249494173115455311387263"
    # trial, fitness = ant_simulator(food_map, map_size, ant_genes)
    # display_trials(trial, "trial.txt")