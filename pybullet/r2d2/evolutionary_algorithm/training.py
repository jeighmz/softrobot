import numpy as np
import random
import os
import datetime

def initialize_population(pop_size, num_parameters):
    return np.random.uniform(-10, 10, (pop_size, num_parameters))  # Increased range of initial parameters


def evolve_population(population, num_generations, objective_function, mutation_rate=0.1):
    best_fitnesses = []
    avg_fitnesses = []
    worst_fitnesses = []
    population_history = []

    for generation in range(num_generations):
        # Evaluate each candidate
        fitnesses = [objective_function(candidate) for candidate in population]

        # Log fitness values
        best_fitnesses.append(max(fitnesses))
        avg_fitnesses.append(np.mean(fitnesses))
        worst_fitnesses.append(min(fitnesses))

        # Store population history
        generation_info = [{'parameters': candidate.tolist(), 'fitness': fitness} for candidate, fitness in zip(population, fitnesses)]
        population_history.append(generation_info)
        
        # Select the best candidates
        selected = select_candidates(population, fitnesses)
        
        # Reproduce
        offspring = reproduce(selected, mutation_rate)
        
        # Create the new population
        population = np.array(offspring)

        # Logging the details of each generation
        print(f"Generation {generation + 1}: Best fitness = {best_fitnesses[-1]}")


    final_population_path = f'r2d2/evolutionary_algorithm/trained_models/final_population_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy'
    directory = os.path.dirname(final_population_path)

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Now that the directory surely exists, save the final population
    np.save(final_population_path, population)  # This should no longer raise an error

    # Optional: Save fitness history
    np.save(f"r2d2/evolutionary_algorithm/trained_models/best_fitnesses_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy", np.array(best_fitnesses))
    np.save(f"r2d2/evolutionary_algorithm/trained_models/avg_fitnesses_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy", np.array(avg_fitnesses))
    np.save(f"r2d2/evolutionary_algorithm/trained_models/worst_fitnesses_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy", np.array(worst_fitnesses))
    print('Final population saved to:', final_population_path)

    return population, best_fitnesses, avg_fitnesses, worst_fitnesses, population_history

def select_candidates(population, fitnesses, num_selected=10):
    selected_indices = np.argsort(fitnesses)[-num_selected:]
    return population[selected_indices]

def reproduce(selected, mutation_rate):
    offspring = []
    for _ in range(len(selected) * 2):
        parent1, parent2 = random.sample(list(selected), 2)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        offspring.append(child)
    return offspring

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    return child

def mutate(candidate, mutation_rate):
    for i in range(len(candidate)):
        if random.random() < mutation_rate:
            candidate[i] += np.random.normal()
    return candidate