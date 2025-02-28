import random


FirstPopulation = [
    [5, 5, 15, 15, 2, 2, 7, 7, 17, 17],
    [1, 15, 15, 25, 25, 25, 12, 17, 22, 3],
    [10, 10, 10, 20, 20, 7, 2, 12, 12, 3],
    [1, 10, 15, 15, 2, 2, 7, 7, 12, 22],
    [5, 5, 20, 25, 20, 25, 12, 12, 17, 3],
    [10, 10, 20, 15, 25, 25, 2, 7, 22, 22],
    [5, 5, 15, 20, 20, 7, 7, 7, 12, 22],
    [10, 15, 15, 25, 20, 2, 2, 12, 17, 17],
    [10, 10, 20, 25, 25, 2, 7, 12, 12, 17],
    [5, 15, 20, 20, 2, 2, 2, 22, 22, 17]
]


def calculate_fitness(chromosome):
    return len(set(chromosome))


population_size = len(FirstPopulation)
generations = 1000


results = {
    "one_point": None,
    "two_point": None,
    "uniform": None
}

for crossover_type in ["one_point", "two_point", "uniform"]:
    FirstPopulation = [
        [5, 5, 15, 15, 2, 2, 7, 7, 17, 17],
        [1, 15, 15, 25, 25, 25, 12, 17, 22, 3],
        [10, 10, 10, 20, 20, 7, 2, 12, 12, 3],
        [1, 10, 15, 15, 2, 2, 7, 7, 12, 22],
        [5, 5, 20, 25, 20, 25, 12, 12, 17, 3],
        [10, 10, 20, 15, 25, 25, 2, 7, 22, 22],
        [5, 5, 15, 20, 20, 7, 7, 7, 12, 22],
        [10, 15, 15, 25, 20, 2, 2, 12, 17, 17],
        [10, 10, 20, 25, 25, 2, 7, 12, 12, 17],
        [5, 15, 20, 20, 2, 2, 2, 22, 22, 17]
    ]

    for generation in range(generations):

        fitness_scores = [calculate_fitness(chromosome) for chromosome in FirstPopulation]


        if max(fitness_scores) == 10:
            results[crossover_type] = FirstPopulation[fitness_scores.index(10)]
            break


        selected_parents = []
        tournament_size = 3
        for _ in range(population_size):
            participants = random.sample(range(population_size), tournament_size)
            selected_parent = max(participants, key=lambda x: fitness_scores[x])
            selected_parents.append(FirstPopulation[selected_parent])


        offspring = []
        for i in range(0, population_size, 2):
            if crossover_type == "one_point":
                crossover_point = random.randint(0, len(selected_parents[i]))
                child1 = selected_parents[i][:crossover_point] + selected_parents[i + 1][crossover_point:]
                child2 = selected_parents[i + 1][:crossover_point] + selected_parents[i][crossover_point:]
            elif crossover_type == "two_point":
                crossover_points = sorted(random.sample(range(0, len(selected_parents[i])), 2))
                child1 = selected_parents[i][:crossover_points[0]] + selected_parents[i + 1][crossover_points[0]:crossover_points[1]] + selected_parents[i][crossover_points[1]:]
                child2 = selected_parents[i + 1][:crossover_points[0]] + selected_parents[i][crossover_points[0]:crossover_points[1]] + selected_parents[i + 1][crossover_points[1]:]
            else:
                mask = [random.randint(0, 1) for _ in range(len(selected_parents[i]))]
                child1 = [selected_parents[i][j] if mask[j] == 0 else selected_parents[i + 1][j] for j in range(len(selected_parents[i]))]
                child2 = [selected_parents[i + 1][j] if mask[j] == 0 else selected_parents[i][j] for j in range(len(selected_parents[i]))]

            offspring.extend([child1, child2])


        mutation_rate = 0.1
        for i in range(population_size):
            if random.random() < mutation_rate:
                gene_to_mutate = random.randint(0, len(offspring[i]) - 1)
                new_gene = random.randint(1, 25)
                offspring[i][gene_to_mutate] = new_gene


        FirstPopulation = offspring


for method, result in results.items():
    print(f"Result for {method} crossover method:", result)
