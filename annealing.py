import random
import math


def probability(dE, temp):
    return math.exp(-dE / temp)


def energy(state):
    return state[0]*state[0]+state[1]*state[1]


class annealing_min(object):

    def __init__(self, temp, start, end, start_x, start_y):
        self.start_temp = temp
        self.temp = temp
        self.start = start
        self.end = end
        self.interval_y = [start, end]
        self.interval_x = [start, end]
        self.final_temp = 0.001
        self.state = [start_x, start_y]
        self.time = 0

    def IN(self, x):
        return self.start <= x <= self.end

    def next(self):
        length = self.end - self.start
        re_length = length * self.temp / self.start_temp
        next_state = [0, 0]
        while True:
            next_state[0] = (random.random() - 0.5) * re_length / 2 + self.state[0]
            if self.IN(next_state[0]):
                break
        while True:
            next_state[1] = (random.random() - 0.5) * re_length / 2 + self.state[1]
            if self.IN(next_state[1]):
                break
        return next_state

    def change_temp(self):
        self.temp = self.start_temp / self.time

    def simulated_annealing(self):
        current_energy = energy(self.state)
        while self.temp > self.final_temp:
            self.time += 1
            state_candidant = self.next()
            candidant_energy = energy(state_candidant)
            ran = 0
            prob = 0
            if candidant_energy < current_energy:
                current_energy = candidant_energy
                self.state = state_candidant
            else:
                ran = random.random()
                prob = probability(candidant_energy - current_energy, self.temp)
                if ran < prob:
                    current_energy = candidant_energy
                    self.state = state_candidant

            self.change_temp()
        return self.state


class annealing_max(object):

    def __init__(self, temp, start, end, start_x, start_y):
        self.start_temp = temp
        self.temp = temp
        self.start = start
        self.end = end
        self.interval_y = [start, end]
        self.interval_x = [start, end]
        self.final_temp = 0.001
        self.state = [start_x, start_y]
        self.time = 0

    def IN(self, x):
        return self.start <= x <= self.end

    def next(self):
        length = self.end - self.start
        re_length = length * self.temp / self.start_temp
        next_state = [0, 0]
        while True:
            next_state[0] = (random.random() - 0.5) * re_length / 2 + self.state[0]
            if self.IN(next_state[0]):
                break
        while True:
            next_state[1] = (random.random() - 0.5) * re_length / 2 + self.state[1]
            if self.IN(next_state[1]):
                break
        return next_state

    def change_temp(self):
        self.temp = self.start_temp / self.time

    def simulated_annealing(self):
        current_energy = energy(self.state)
        while self.temp > self.final_temp:
            self.time += 1
            state_candidant = self.next()
            candidant_energy = energy(state_candidant)
            ran = 0
            prob = 0
            if candidant_energy > current_energy:
                current_energy = candidant_energy
                self.state = state_candidant
            else:
                ran = random.random()
                prob = probability(current_energy - candidant_energy, self.temp)
                if ran < prob:
                    current_energy = candidant_energy
                    self.state = state_candidant

            self.change_temp()
        return self.state
