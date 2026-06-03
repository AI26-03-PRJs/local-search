from env.utils import random_position
import random
import copy

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
        if not state:
            return self.add_sensor(state)
        operations = ['remove','move']
        if len(state) < self.world.max_sensors:
            operations.append('add')

        op = random.choice(operations)
        if op == 'move':
            return self.move_sensor(state)
        elif op == 'remove':
            return self.remove_sensor(state)
        else:
            return self.add_sensor(state)

    def add_sensor(self,state):
        new_state = copy.deepcopy(state)
        pos = random_position(self.world)
        while pos in new_state:
            pos = random_position(self.world)
        new_state.append(pos)
        return new_state

    def remove_sensor(self,state):
        new_state = copy.deepcopy(state)
        inx_pos = random.randint(0, len(new_state) - 1)
        new_state.pop(inx_pos)
        return new_state

    def move_sensor(self,state):
        new_state = copy.deepcopy(state)
        idx_pos = random.randint(0, len(new_state) - 1)
        pos = random_position(self.world)
        while pos in new_state:
            pos = random_position(self.world)
        new_state[idx_pos] = pos
        return new_state

    def initialize_state(self):
        n_sensors = random.randint(1, self.world.max_sensors)
        state = []
        while len(state) < n_sensors:
            pos = random_position(self.world)
            if pos not in state:
                state.append(pos)
        return state