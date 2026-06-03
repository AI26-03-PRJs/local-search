from search.local_search_base import LocalSearchBase
class TabuSearch(LocalSearchBase):
    def run(self, initial_state, tabu_length=10, iterations=500, max_neighbours=30):
        current_state = initial_state
        current_cost = self.evaluate(current_state)
        best_state = current_state.copy()
        best_cost = current_cost
        tabu_list = []
        evaluations = [best_cost]
        states_history = [best_state]
        for i in range(iterations):
            neighbors = []
            for j in range(max_neighbours):
                neighbors.append(self.get_neighbor(current_state))
            best_neighbor = None
            best_neighbor_cost = float('inf')
            for neighbor in neighbors:
                neighbor_cost = self.evaluate(neighbor)
                neighbor_key = tuple(sorted(neighbor))
                if neighbor_key not in tabu_list or neighbor_cost < best_cost:
                    if neighbor_cost < best_neighbor_cost:
                        best_neighbor = neighbor
                        best_neighbor_cost = neighbor_cost
            if best_neighbor is None:
                break
            current_state = best_neighbor
            current_cost = best_neighbor_cost
            current_key = tuple(sorted(current_state))
            tabu_list.append(current_key)
            if len(tabu_list) > tabu_length:
                tabu_list.pop(0)
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
            evaluations.append(best_cost)
            states_history.append(best_state)

        return best_state, best_cost, evaluations, states_history