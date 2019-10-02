from task3.annealing import *
from task3.genetic import *
from task3.moving_to_top import *


def main():
    temp = 10
    start_interval = -50
    end_interval = 50
    test_min = annealing_min(temp, start_interval, end_interval, random.randrange(start_interval, end_interval, 1),
                             random.randrange(start_interval, end_interval, 1))
    print("Coordinate min value function with annealing_min= " + str(test_min.simulated_annealing()))
    test_max = annealing_max(temp, start_interval, end_interval, random.randrange(start_interval, end_interval, 1),
                             random.randrange(start_interval, end_interval, 1))
    print("Coordinate max value function with annealing_max= " + str(test_max.simulated_annealing()))

    test_min = GA_min(start_interval, end_interval, 10, 0.7)
    print("Сandidates min value function with Genetic algorithm = " + str(test_min.Genetic_algorithm()))
    test_max = GA_max(start_interval, end_interval, 10, 0.7)
    print("Сandidates max value function with Genetic algorithm = " + str(test_max.Genetic_algorithm()))

    test_min = GreedyA_min(start_interval, end_interval, 10)
    print("Coordinate min value function with Greedy algorithm = " + str(test_min.Greedy_algorithm()))
    test_max = GreedyA_max(start_interval, end_interval, 10)
    print("Coordinate max value function with Greedy algorithm = " + str(test_max.Greedy_algorithm()))

    test_min = Stochastic_search_min(start_interval, end_interval, 10)
    print("Coordinate min value function with Stochastic search for moving to top = " + str(test_min.moving_to_top()))

    test_max = Stochastic_search_max(start_interval, end_interval, 10)
    print("Coordinate min value function with Stochastic search for moving to top = " + str(test_max.moving_to_top()))

if __name__ == '__main__':
    main()
