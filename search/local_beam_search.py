from search.local_search_base import LocalSearchBase

class LocalBeamSearch(LocalSearchBase):
    def run(self, initial_state, **kwargs):
        k = kwargs.get('k', 5)
        neighbors = kwargs.get('neighbors', 40)
        max_iterations = kwargs.get('max_iterations', 500)
        patience = kwargs.get('patience', 20)

        beam = [initial_state]
        while len(beam) < k:
            beam.append(self.initialize_state())

        beam_costs = [self.evaluate(s) for s in beam]

        best_idx = beam_costs.index(min(beam_costs))
        best_state = beam[best_idx]
        best_cost = beam_costs[best_idx]

        evaluations = [best_cost]
        states_history = [best_state]

        imp_counter = 0

        for i in range(max_iterations):
            candidates = []
            for state in beam:
                for j in range(neighbors):
                    neighbor = self.get_neighbor(state)
                    cost = self.evaluate(neighbor)
                    candidates.append((cost, neighbor))

            candidates.sort(key=lambda x: x[0])
            beam = [c[1] for c in candidates[:k]]
            beam_costs = [c[0] for c in candidates[:k]]

            if beam_costs[0] < best_cost:
                best_cost = beam_costs[0]
                best_state = beam[0]
                imp_counter = 0
            else:
                imp_counter += 1

            evaluations.append(best_cost)
            states_history.append(best_state)

            if imp_counter >= patience:
                break

        return best_state, best_cost, evaluations, states_history