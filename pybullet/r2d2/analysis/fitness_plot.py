import matplotlib.pyplot as plt
import numpy as np

def plot_fitness_evolution(best_fitnesses, avg_fitnesses, worst_fitnesses):
    """
    Plots the evolution of fitness over generations.

    Args:
        best_fitnesses (list): List of best fitness values for each generation.
        avg_fitnesses (list): List of average fitness values for each generation.
        worst_fitnesses (list): List of worst fitness values for each generation.

    Returns:
        None
    """
    generations = np.arange(len(best_fitnesses))
    
    plt.figure(figsize=(10, 6))
    plt.plot(generations, best_fitnesses, label='Best Fitness')
    plt.plot(generations, avg_fitnesses, label='Average Fitness')
    plt.plot(generations, worst_fitnesses, label='Worst Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness Evolution')
    plt.legend()
    plt.grid(True)
    plt.show()