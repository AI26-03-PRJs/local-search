from search.local_search_base import LocalSearchBase

class HillClimbing(LocalSearchBase):
    def run(self, initial_state,iterations=500,neighbors=40):
        current_state = initial_state.copy()
        current_cost = self.evaluate(current_state)

        best_state = current_state
        best_cost = current_cost

        evaluations = [current_cost]
        states_history = [current_state]

        for i in range(iterations):
            best_neighbor = None
            best_neighbor_cost = float("inf")

            for j in range(neighbors):
                neighbor = self.get_neighbor(current_state)
                cost = self.evaluate(neighbor)
                if cost < best_neighbor_cost:
                    best_neighbor_cost = cost
                    best_neighbor = neighbor

            if best_neighbor_cost >= current_cost:
                break

            current_state = best_neighbor
            current_cost = best_neighbor_cost

            if current_cost < best_cost:
                best_cost = current_cost
                best_state = current_state.copy()

            evaluations.append(current_cost)
            states_history.append(current_state.copy())

        return (best_state, best_cost, evaluations, states_history)