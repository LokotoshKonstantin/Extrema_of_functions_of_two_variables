import random
import math
import numpy as np


def my_function(state):
    return state[0]*state[0]+state[1]*state[1]


def distance(first, second):
    return math.sqrt(math.pow(first[0] - second[0], 2) + math.pow(first[1] - second[1], 2))


class GA_min(object):

    def __init__(self, start, end, count_specimen, coef_crossing):
        self.start = start
        self.end = end
        self.count_specimen = count_specimen
        self.population = []
        self.coef_crossing = coef_crossing
        self.time = 1

    def init_population(self):
        for i in range(self.count_specimen):
            self.population.append(
                [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)])

    def crossing(self):
        half = int(len(self.population) / 2)
        father = self.population[:half]
        mother = self.population[half:]
        np.random.shuffle(father)
        np.random.shuffle(mother)
        offspring = []
        result = []
        for i in range(half):
            if np.random.uniform(0, 1) <= self.coef_crossing:
                copint = np.random.randint(0, int(len(father[i]) / 2))
                son = father[i][:copint] + (mother[i][copint:])
                daughter = mother[i][:copint] + (father[i][copint:])
            else:
                son = father[i]
                daughter = mother[i]
            offspring.append([son, daughter])

        for x in offspring:
            result.append([(x[0][0] + x[1][0]) / 2, (x[0][1] + x[1][1]) / 2])
        self.population = result

    def IN(self, x):
        return self.start <= x <= self.end

    def next(self, state):
        length = self.end - self.start
        re_length = length / self.time
        next_state = [0, 0]
        while True:
            next_state[0] = (random.random() - 0.5) * re_length / 2 + state[0]
            if self.IN(next_state[0]):
                break
        while True:
            next_state[1] = (random.random() - 0.5) * re_length / 2 + state[1]
            if self.IN(next_state[1]):
                break
        return next_state

    def mutation(self):
        result = []
        for x in self.population:
            for i in range(self.count_specimen):
                result.append(self.next(x))
        self.population = result

    def selection(self):
        result = []
        value = []
        for x in self.population:
            value.append(my_function(x))
        sort_index = np.argsort(value)[:self.count_specimen]
        for x in sort_index:
            result.append(self.population[x])
        self.population = result

    def control(self):
        """
        Возвращает False если нужно заканчивать генетический алгоритм.
        Возвращает True если можно продолжать генетический алгоритм.

        """
        dif = 0
        for x in range(len(self.population) - 1):
            dif += distance(self.population[x], self.population[x + 1])
        if dif < 0.04:
            return False
        else:
            return True

    def Genetic_algorithm(self):
        self.init_population()
        while self.time < 10000 and self.control():
            self.crossing()
            self.mutation()
            self.selection()
            self.time += 1
        return self.population


class GA_max(object):

    def __init__(self, start, end, count_specimen, coef_crossing):
        self.start = start
        self.end = end
        self.count_specimen = count_specimen
        self.population = []
        self.coef_crossing = coef_crossing
        self.time = 1

    def init_population(self):
        for i in range(self.count_specimen):
            self.population.append(
                [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)])

    def crossing(self):
        half = int(len(self.population) / 2)
        father = self.population[:half]
        mother = self.population[half:]
        np.random.shuffle(father)
        np.random.shuffle(mother)
        offspring = []
        result = []
        for i in range(half):
            if np.random.uniform(0, 1) <= self.coef_crossing:
                copint = np.random.randint(0, int(len(father[i]) / 2))
                son = father[i][:copint] + (mother[i][copint:])
                daughter = mother[i][:copint] + (father[i][copint:])
            else:
                son = father[i]
                daughter = mother[i]
            offspring.append([son, daughter])

        for x in offspring:
            result.append([(x[0][0] + x[1][0]) / 2, (x[0][1] + x[1][1]) / 2])
        self.population = result

    def IN(self, x):
        return self.start <= x <= self.end

    def next(self, state):
        length = self.end - self.start
        re_length = length / self.time
        next_state = [0, 0]
        while True:
            next_state[0] = (random.random() - 0.5) * re_length / 2 + state[0]
            if self.IN(next_state[0]):
                break
        while True:
            next_state[1] = (random.random() - 0.5) * re_length / 2 + state[1]
            if self.IN(next_state[1]):
                break
        return next_state

    def mutation(self):
        result = []
        for x in self.population:
            for i in range(self.count_specimen):
                result.append(self.next(x))
        self.population = result

    def selection(self):
        result = []
        value = []
        for x in self.population:
            value.append(my_function(x))
        sort_index = np.argsort(value)
        sort_index = np.flip(sort_index)[:self.count_specimen]
        for x in sort_index:
            result.append(self.population[x])
        self.population = result

    def control(self):
        """
            Возвращает False если нужно заканчивать генетический алгоритм.
            Возвращает True если можно продолжать генетический алгоритм.

            """
        dif = 0
        for x in range(len(self.population) - 1):
            dif += distance(self.population[x], self.population[x + 1])
        if dif < 0.04:
            return False
        else:
            return True

    def Genetic_algorithm(self):
        self.init_population()
        while self.time < 10000 and self.control():
            self.crossing()
            self.mutation()
            self.selection()
            self.time += 1
        return self.population
