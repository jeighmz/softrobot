import numpy as np
import matplotlib.pyplot as plt

def analyze_parameters(population_history):
    num_generations = len(population_history)
    num_parameters = len(population_history[0][0])

    avg_parameters = np.zeros((num_generations, num_parameters))
    best_parameters = np.zeros((num_generations, num_parameters))

    for gen_idx, generation in enumerate(population_history):
        best_candidate = max(generation, key=lambda candidate: candidate['fitness'])
        avg_parameters[gen_idx, :] = np.mean([candidate['parameters'] for candidate in generation], axis=0)
        best_parameters[gen_idx, :] = best_candidate['parameters']

    for param_idx in range(num_parameters):
        plt.figure(figsize=(10, 6))
        plt.plot(range(num_generations), avg_parameters[:, param_idx], label=f'Average Parameter {param_idx}')
        plt.plot(range(num_generations), best_parameters[:, param_idx], label=f'Best Parameter {param_idx}')
        plt.xlabel('Generation')
        plt.ylabel('Parameter Value')
        plt.title(f'Parameter {param_idx} Evolution')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage:
# population_history = [
#     [{'parameters': np.array([...]), 'fitness': ...}, ...],
#     ...
# ]
# analyze_parameters(population_history)