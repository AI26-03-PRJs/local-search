import random

def GENETIC_ALGORITHM(population, fitness, max_generations=1000):
    for generation in range(max_generations):
        weights = WEIGHTED_BY(population, fitness)
        population2 = []
        for i in range(len(population)):
            parent1, parent2 = WEIGHTED_RANDOM_CHOICES(population, weights, 2)
            child = REPRODUCE(parent1, parent2)
            if random.random() < 0.1:
                child = MUTATE(child)
            population2.append(child)
        population = population2
        best_fitness = max(fitness(ind) for ind in population)
        if best_fitness == 28:
            break
    return max(population, key=fitness)

def WEIGHTED_BY(population, fitness):
    scores = [fitness(ind) for ind in population]
    total = sum(scores)
    if total == 0:
        return [1/len(population)] * len(population)
    return [s / total for s in scores]

def WEIGHTED_RANDOM_CHOICES(population, weights, k):
    return random.choices(population, weights=weights, k=k)

def REPRODUCE(parent1, parent2):
    n = len(parent1)
    c = random.randint(1, n - 1)
    return parent1[:c] + parent2[c:]

def MUTATE(child):
    idx = random.randint(0, len(child) - 1)
    child = list(child)
    child[idx] = random.randint(0, 7)
    return child

def queens_fitness(state):

    attacks = 0
    
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return 28 - attacks

population = [[random.randint(0, 7) for _ in range(8)] for _ in range(50)]

best = GENETIC_ALGORITHM(population, queens_fitness)
print("Best Solution:", best)
print("Fitness:", queens_fitness(best))