import copy
import random

from generateRandomSolutions import is_correct_solution
from roulette import roulette

CROSSOVER_PROBABILITY = 40


def crossover(solutions: list, scores: list, grid_height: int, grid_width: int):
    """
    take random number of machines put it to other
    after that fix to be correct
    :param solutions:
    :param scores:
    :return:
    """
    new_population = []
    for approach in range(solutions):
        if random.randint(0, 1) == 1:
            parent_01 = solutions[approach]
            parent_02 = roulette(solutions, scores)
            child_01 = copy.deepcopy(parent_01)
            child_02 = copy.deepcopy(parent_02)
            gens = random.randint(0, len(parent_02))
            random.sample(0, len(parent_02) - 1, gens)
            for gen in gens:
                child_01[gen] = parent_02[gen]
            if not is_correct_solution(child_01):
                child_01 = fix_solution(child_01)
        new_population.append(child_01)
    else:
        new_population.append(parent_01)


def fix_solution(solution: list, grid_height: int, grid_width: int):
    fixed_solution = solution
    while not is_correct_solution(fixed_solution):
        for i in range(len(fixed_solution) - 1):
            for j in range(len(fixed_solution) - i):
                if fixed_solution[i] == fixed_solution[i + j + 1]:
                    fixed_solution[i + j + 1] = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
    return fixed_solution
