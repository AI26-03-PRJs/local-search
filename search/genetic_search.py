from search.local_search_base import LocalSearchBase
import random
import copy


class GeneticAlgorithm(LocalSearchBase):
    def run(self, initial_state, **kwargs):
        population_size = kwargs.get('population_size', 50)
        max_generations = kwargs.get('max_generations', 200)
        mutation_probability = kwargs.get('mutation_probability', 0.1)

        population = [initial_state.copy()]
        for _ in range(population_size - 1):
            population.append(self.initialize_state())

        best_individual = initial_state.copy()
        best_cost = self.evaluate(best_individual)
        evaluations = []
        states_history = []

        for _ in range(max_generations):
            fitness_scores = []
            for individual in population:
                cost = self.evaluate(individual)
                fitness_scores.append(1.0 / (cost + 1))

            for individual, fitness in zip(population, fitness_scores):
                if fitness > 1.0 / (best_cost + 1):
                    best_individual = individual.copy()
                    best_cost = self.evaluate(best_individual)

            total = sum(fitness_scores)
            if total == 0:
                weights = [1.0 / len(population)] * len(population)
            else:
                weights = [f / total for f in fitness_scores]

            population2 = []
            for _ in range(len(population)):
                parent1, parent2 = random.choices(population, weights=weights, k=2)
                child = self._crossover(parent1, parent2)
                if random.random() < mutation_probability:
                    child = self.get_neighbor(child)
                population2.append(child)
            population = population2

            evaluations.append(best_cost)
            states_history.append(best_individual.copy())

        return best_individual, best_cost, evaluations, states_history

    def _crossover(self, parent1, parent2):
        p1 = copy.deepcopy(parent1)
        p2 = copy.deepcopy(parent2)
        if not p1:
            return p2[: self.world.max_sensors]
        c = random.randint(1, len(p1))
        child = p1[:c] + p2[c:]
        seen = set()
        unique = []
        for pos in child:
            if pos not in seen:
                seen.add(pos)
                unique.append(pos)
        if len(unique) > self.world.max_sensors:
            unique = random.sample(unique, self.world.max_sensors)
        return unique
