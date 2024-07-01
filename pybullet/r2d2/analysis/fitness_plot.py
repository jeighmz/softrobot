import matplotlib.pyplot as plt
import numpy as np

def plot_fitness_evolution(best_fitnesses, avg_fitnesses, worst_fitnesses):
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

# Example usage:
# best_fitnesses, avg_fitnesses, worst_fitnesses = [list_of_best_fitnesses], [list_of_avg_fitnesses], [list_of_worst_fitnesses]
# plot_fitness_evolution(best_fitnesses, avg_fitnesses, worst_fitnesses)