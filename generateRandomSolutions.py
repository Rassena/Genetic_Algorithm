import random


def is_correct_solution(solution: [int]) -> bool:
    """
    check if that solution is possible (2 machines on same place in grid)

    :param solution: list of machine's position in grid
    :return:
    """

    return any(solution.count(element) > 1 for element in solution)


def generate_random_solutions(amount_of_machines: int, grid_height: int, grid_width: int,
                              amount_of_solutions: int) -> [[list]]:
    """
    Generate random correct solution

    :param amount_of_machines: amount of machines placed in grid
    :param grid_height: height of tested grid area
    :param grid_width: width of tested grid area
    :param amount_of_solutions: amount of random solutions to generate
    :return: list of machine position in solution
    """

    solutions = []
    solution_number = 0
    while solution_number < amount_of_solutions:
        solution = []
        for machine_number in range(amount_of_machines):
            solution.append((random.randint(0, grid_width), random.randint(0, grid_height)))
        if is_correct_solution(solution):
            solutions.append(solution)
            solution_number += 1

    return solutions
