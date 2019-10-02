import random
import math
import numpy as np


def my_function(state):
    return state[0] * state[0] + state[1] * state[1]


def distance(first, second):
    return math.sqrt(math.pow(first[0] - second[0], 2) + math.pow(first[1] - second[1], 2))


class GreedyA_min(object):

    def __init__(self, start, end, count_of_cases):
        self.start = start
        self.end = end
        self.prev_state = [0, 0]
        self.state = []
        self.time = 1
        self.count_of_cases = count_of_cases

    def IN(self, x):
        return self.start <= x <= self.end

    def init_first(self):
        self.state = [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)]

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

    def control(self):
        """
        Возвращает False если нужно заканчивать генетический алгоритм.
        Возвращает True если можно продолжать генетический алгоритм.

        """
        dif = distance(self.state, self.prev_state)
        if dif < 0.04:
            return False
        else:
            return True

    def Greedy_algorithm(self):
        self.init_first()
        while self.control() and self.time < 10000:
            cases = []
            for i in range(self.count_of_cases):
                cases.append(self.next(self.state))
            value = []
            for x in cases:
                value.append(my_function(x))
            sort_index = np.argsort(value)
            self.prev_state = self.state
            self.state = cases[sort_index[0]]
            self.time += 1
        return self.state


class GreedyA_max(object):

    def __init__(self, start, end, count_of_cases):
        self.start = start
        self.end = end
        self.prev_state = [0, 0]
        self.state = []
        self.time = 1
        self.count_of_cases = count_of_cases

    def IN(self, x):
        return self.start <= x <= self.end

    def init_first(self):
        self.state = [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)]

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

    def control(self):
        """
        Возвращает False если нужно заканчивать генетический алгоритм.
        Возвращает True если можно продолжать генетический алгоритм.

        """
        dif = distance(self.state, self.prev_state)
        if dif < 0.04:
            return False
        else:
            return True

    def Greedy_algorithm(self):
        self.init_first()
        while self.control() and self.time < 10000:
            cases = []
            for i in range(self.count_of_cases):
                cases.append(self.next(self.state))
            value = []
            for x in cases:
                value.append(my_function(x))
            sort_index = np.argsort(value)
            sort_index = np.flip(sort_index)
            self.prev_state = self.state
            self.state = cases[sort_index[0]]
            self.time += 1
        return self.state


class Stochastic_search_min(object):

    def __init__(self, start, end, count_of_cases):
        self.start = start
        self.end = end
        self.prev_state = [0, 0]
        self.state = []
        self.time = 1
        self.count_of_cases = count_of_cases

    def IN(self, x):
        return self.start <= x <= self.end

    def init_first(self):
        self.state = [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)]

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

    def control(self):
        """
        Возвращает False если нужно заканчивать генетический алгоритм.
        Возвращает True если можно продолжать генетический алгоритм.

        """
        dif = distance(self.state, self.prev_state)
        if dif < 0.04:
            return False
        else:
            return True

    def moving_to_top(self):
        self.init_first()
        while self.control() and self.time < 10000:
            cases = []
            while len(cases) < self.count_of_cases:
                a = self.next(self.state)
                if my_function(a) < my_function(self.state):
                    cases.append(a)
            self.prev_state = self.state
            self.state = cases[random.randrange(0, len(cases), 1)]
            self.time += 1
        return self.state


class Stochastic_search_max(object):

    def __init__(self, start, end, count_of_cases):
        self.start = start
        self.end = end
        self.prev_state = [0, 0]
        self.state = []
        self.time = 1
        self.count_of_cases = count_of_cases

    def IN(self, x):
        return self.start <= x <= self.end

    def init_first(self):
        self.state = [random.randrange(self.start, self.end, 1), random.randrange(self.start, self.end, 1)]

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

    def control(self):
        """
        Возвращает False если нужно заканчивать генетический алгоритм.
        Возвращает True если можно продолжать генетический алгоритм.

        """
        dif = distance(self.state, self.prev_state)
        if dif < 0.04:
            return False
        else:
            return True

    def moving_to_top(self):
        self.init_first()
        while self.control() and self.time < 10000:
            cases = []
            while len(cases) < self.count_of_cases:
                a = self.next(self.state)
                if my_function(a) > my_function(self.state):
                    cases.append(a)
            self.prev_state = self.state
            self.state = cases[random.randrange(0, len(cases), 1)]
            self.time += 1
        return self.state
