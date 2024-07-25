import numpy as np
import random
import os
import datetime

def initialize_population(pop_size, num_parameters):
    return np.random.uniform(-10, 10, (pop_size, num_parameters))  # Increased range of initial parameters


def evolve_population(population, num_generations, objective_function, mutation_rate=0.1):
    """
    Evolves a population over a specified number of generations using an evolutionary algorithm.

    Args:
        population (numpy.ndarray): The initial population of candidate solutions.
        num_generations (int): The number of generations to evolve the population.
        objective_function (function): The function used to evaluate the fitness of each candidate solution.
        mutation_rate (float, optional): The rate at which mutations occur during reproduction. Defaults to 0.1.

    Returns:
        tuple: A tuple containing the final population, best fitnesses, average fitnesses, worst fitnesses, and population history.

    Raises:
        None

    """

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

    # save population history
    final_population_history_path = f'r2d2/evolutionary_algorithm/trained_models/final_population_history_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy'
    directory = os.path.dirname(final_population_history_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    np.save(final_population_history_path, np.array(generation_info))

    # Save the final population for future training sessions
    final_population_path = f'r2d2/evolutionary_algorithm/trained_models/final_population_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy'
    directory = os.path.dirname(final_population_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    np.save(final_population_path, population)  # Save the final population
    
    # Optional: Save fitness history
    best_fitness_index = np.argmax(best_fitnesses)
    best_generation_info = population_history[best_fitness_index]
    np.save(f"r2d2/evolutionary_algorithm/trained_models/best_generation_info_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.npy", np.array(best_generation_info))
    
    np.save(f"r2d2/evolutionary_algorithm/trained_models/avg_fitnesses_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy", np.array(avg_fitnesses))
    np.save(f"r2d2/evolutionary_algorithm/trained_models/worst_fitnesses_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.npy", np.array(worst_fitnesses))
    print('Final population saved to:', final_population_path)
    # print(shape(population_history)

    return population, best_fitnesses, avg_fitnesses, worst_fitnesses, population_history

def select_candidates(population, fitnesses, num_selected=4):
    """
    Selects the top candidates from the population based on their fitness scores.

    Args:
        population (numpy.ndarray): The population of candidates.
        fitnesses (numpy.ndarray): The fitness scores of the candidates.
        num_selected (int, optional): The number of candidates to select. Defaults to 10.

    Returns:
        numpy.ndarray: The selected candidates from the population.
    """
    selected_indices = np.argsort(fitnesses)[-num_selected:]
    return population[selected_indices]

def reproduce(selected, mutation_rate):
    """
    Reproduces the selected individuals by performing crossover and mutation.

    Args:
        selected (list): A list of selected individuals.
        mutation_rate (float): The probability of mutation for each gene.

    Returns:
        list: A list of offspring generated through reproduction.
    """
    offspring = []
    for _ in range(len(selected) * 2):
        parent1, parent2 = random.sample(list(selected), 2)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        offspring.append(child)
    return offspring

def crossover(parent1, parent2):
    """
    Perform crossover between two parents to create a child.

    Args:
        parent1 (numpy.ndarray): The first parent.
        parent2 (numpy.ndarray): The second parent.

    Returns:
        numpy.ndarray: The child created through crossover.
    """
    crossover_point = random.randint(0, len(parent1) - 1)
    child = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    return child

def mutate(candidate, mutation_rate):
    """
    Mutates the given candidate by adding random noise to each element.

    Args:
        candidate (list): The candidate solution to be mutated.
        mutation_rate (float): The probability of mutation for each element.

    Returns:
        list: The mutated candidate solution.
    """
    for i in range(len(candidate)):
        if random.random() < mutation_rate:
            candidate[i] += np.random.normal()
    return candidate