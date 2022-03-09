SOURCE = 'source'
DEST = 'dest'
COST = 'cost'
AMOUNT = 'amount'


def calculate_solutions_score(solutions: [[int]], costs: dict, flows: dict) -> [float]:
    """
    Calculate scores for every solution in list

    :param solutions:
    :param costs:
    :param flows:
    :return: list of solutions scores
    """

    scores = []
    for solution in solutions:
        scores.append(calculate_solution_score(solution, costs, flows))

    return scores


def get_best_solutions(solutions: [], scores: [], amount: int = 1) -> [([int], float)]:
    """
    Get list of best :amount: solutions with their score

    :param solutions:
    :param scores:
    :param amount:
    :return: list of tuples (solution, score)
    """
    best_solutions = []

    for _ in range(amount):
        best_score = max(scores)
        best_number = 0
        for solution_number in range(len(solutions)):
            if scores[solution_number] != -1 and scores[solution_number] < best_score:
                best_score = scores[solution_number]
                best_number = solution_number
                scores[solution_number]=-1
        best_solutions.append((solutions[best_number], best_score))

    return best_solutions

def calculate_solution_score(solution: [int], costs: dict, flows: dict) -> float:
    """
    Calculate solution score

    :param solution:
    :param costs:
    :param flows:
    :return: solution score
    """

    score = 0

    for flow in flows:
        # print(flow.get(SOURCE), flow.get(DEST), flow.get(AMOUNT))
        source = flow.get(SOURCE)
        destination = flow.get(DEST)
        for cost in costs:
            pass
            # print(cost.get(SOURCE), cost.get(DEST), cost.get(COST))
            if source == cost.get(SOURCE) and destination == cost.get(DEST):
                distance = abs(solution[source][0] - solution[destination][0]) + abs(
                    solution[source][1] - solution[destination][1])
                score += distance * cost.get(COST) * flow.get(AMOUNT)

    return score
