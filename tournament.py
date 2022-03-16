import copy
import random

NEXT_STAGE_PERCENTAGE = 0.75


def tournament(solutions: list, scores: list, size=4):
    """
    :param solutions:
    :param scores:
    :param size:
    :return:
    """
    round_solutions = copy.deepcopy(solutions)
    round_scores = copy.deepcopy(scores)
    while len(round_solutions) > 1:
        new_round_solutions = []
        new_round_scores = []
        fights = round(len(round_solutions) * NEXT_STAGE_PERCENTAGE)
        if fights < size:
            fights = 1
        for i in range(fights):
            combat_solutions = []
            combat_scores = []
            for j in range(size):
                draw = random.sample(range(len(round_solutions)),1)[0]
                combat_solutions.append(round_solutions[draw])
                combat_scores.append(round_scores[draw])
            winner_solution, winner_score = battle(combat_solutions, combat_scores)
            new_round_solutions.append(winner_solution)
            new_round_scores.append(winner_score)
        round_solutions = copy.deepcopy(new_round_solutions)
        round_scores = copy.deepcopy(new_round_scores)
    return round_solutions[0], round_scores[0]


def battle(solutions: list, scores: list):
    """

    :param solutions:
    :param scores:
    :return:
    """

    best = 0
    best_position = 0
    for i in range(len(solutions)):
        if scores[i] > best:
            best = scores[i]
            best_position = i
    return solutions[best_position], scores[best_position]
