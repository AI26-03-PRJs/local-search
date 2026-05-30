
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
        """
        TODO: Implement the neighbor generation function.
        
        Generate a new valid state by applying a local change to the current state.
        Ensure you include all the required operations mentioned in the project PDF
        to support a dynamic search space.
        
        Returns:
            neighbor_state (list of tuples): The newly generated valid state.
        """
    def initialize_state(self):
        """
        TODO: Generate a valid initial state.
        
        Create a starting configuration of sensors within the grid boundaries,
        respecting the maximum sensor limits and obstacle placements.
        
        Returns:
            initial_state (list of tuples): The starting coordinates of the sensors.
        """
        raise NotImplementedError("Students must implement this method.")