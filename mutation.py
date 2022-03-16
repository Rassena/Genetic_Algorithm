import copy
import random

MUTATION_PROBABILITY = 3


def mutation(solutions: list):
    mutated_solutions = []
    for solution in solutions:
        rand = random.random() * 100
        solution = copy.deepcopy(solution)
        if rand < MUTATION_PROBABILITY:
            print("Mutation:")
            print(solution)
            to_swap = random.sample(range(len(solution)), 2)
            temp = solution[to_swap[1]]
            solution[to_swap[1]] = solution[to_swap[0]]
            solution[to_swap[0]] = temp
            print(solution)
        mutated_solutions.append(solution)
    return mutated_solutions


