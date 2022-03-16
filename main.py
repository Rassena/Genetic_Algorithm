from ReadData import read_from_json_file, EASY_COST_PATH, EASY_FLOW_PATH, FLAT_FLOW_PATH, FLAT_COST_PATH, \
    HARD_FLOW_PATH, HARD_COST_PATH
from calculateScore import calculate_solutions_score, get_best_solutions
from generateRandomSolutions import generate_random_solutions
from mutation import mutation
from roulette import roulette
from tournament import tournament

if __name__ == '__main__':
    # [cost_path,flow_path, number_of_machines,grid_height,grid_width,solutions_to_generate,number_of_best_solutions]
    easy_problem = [EASY_COST_PATH, EASY_FLOW_PATH, 9, 3, 3, 100, 10]
    flat_problem = [FLAT_COST_PATH, FLAT_FLOW_PATH, 12, 1, 12, 100, 10]
    hard_problem = [HARD_COST_PATH, HARD_FLOW_PATH, 24, 5, 6, 100, 10]

    problems = [easy_problem, flat_problem, hard_problem]

    tournament_size = 4

    for problem in problems:
        number_of_machines = problem[2]
        grid_height = problem[3]
        grid_width = problem[4]
        solutions_to_generate = problem[5]
        number_of_best_solutions = problem[6]

        print("\n\tRandom starting solutions\n")
        # generate random solutions
        random_solutions = generate_random_solutions(number_of_machines, grid_height, grid_width, solutions_to_generate)
        print(random_solutions)

        # get costs and flows
        costs = read_from_json_file(EASY_COST_PATH)
        flows = read_from_json_file(EASY_FLOW_PATH)

        # calculate scores for solutions
        scores = calculate_solutions_score(random_solutions, costs, flows)
        print(scores)

        print("\n\tBest Solutions with scores\n")
        # get best solutions with scores
        best_solutions = get_best_solutions(random_solutions, scores, number_of_best_solutions)
        print(best_solutions)
        # print(best_solutions[0][1])

        print("\n\tRoulette Result\n")
        # roulette
        new_solutions, new_scores = roulette(random_solutions, scores)
        print(new_solutions)
        print(new_scores)

        print("\n\tTournament Result\n")
        tournament_solution, tournament_score = tournament(random_solutions, scores, tournament_size)
        print(tournament_solution)
        print(tournament_score)

        print("\n\tMutation Result\n")
        mutation_solution = mutation(random_solutions)
        mutation_scores = calculate_solutions_score(mutation_solution, costs, flows)
        print(mutation_solution)
        print(mutation_scores)
        print("\t===========================\n")
