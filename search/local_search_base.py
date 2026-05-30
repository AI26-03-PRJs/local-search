from env.utils import random_position
import random

class LocalSearchBase:
    def __init__(self, world):
        self.world = world

    def evaluate(self, state):
        targets = self.world.get_targets()
        covered_targets = set()
        for (xs,ys) in state:
            for (xt, yt) in targets:
                if abs(xs-xt) + abs(ys-yt) <= self.world.sensor_range:
                    covered_targets.add((xt,yt))
        uncovered = len(targets) - len(covered_targets)
        cost = uncovered * 10 + len(state)
        return cost


    def get_neighbor(self, state):
        pass
    def initialize_state(self):
        n_sensors = random.randint(1, self.world.max_sensors)
        state = []
        while len(state) < n_sensors:
            pos = random_position(self.world)
            if pos not in state:
                state.append(pos)
        return state