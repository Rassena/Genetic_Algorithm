from random import random


def roulette(solutions: list, scores: list):
    """
    roulette selecting method for new generation

    :param solutions:
    :param scores:
    :return:
    """
    new_generation_solutions = list()
    new_generation_scores = list()
    sum_of_scores = 0
    solutions_thresholds = list()
    for i in range(len(solutions)):
        sum_of_scores += scores[i]
    for i in range(len(solutions)):
        previous = 0
        if (i!=0):
            previous = solutions_thresholds[i-1]
        solutions_thresholds.append(previous + scores[i] / sum_of_scores)
    for i in range(len(solutions)):
        draw = random()
        selected = 0
        for j in range(len(solutions_thresholds)):
            if draw > solutions_thresholds[i]:
                selected = i - 1
                break
        new_generation_solutions.append(solutions[selected])
        new_generation_scores.append(scores[selected])


    return new_generation_solutions,new_generation_scores
