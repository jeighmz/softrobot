"""
This script demonstrates an evolutionary algorithm for optimizing the parameters of a robot using PyBullet.

The script performs the following steps:
1. Connects to the PyBullet physics server.
2. Loads the R2D2 robot and counts its joints.
3. Initializes the population of candidate solutions.
4. Evolves the population using an evolutionary algorithm.
5. Disconnects from the physics server.
6. Performs post-training analysis, including plotting fitness evolution, analyzing parameters, and visualizing the best solution.

Note: This script assumes that the necessary modules and packages are installed, including pybullet, pybullet_data, and the custom modules from the r2d2 package.
"""

from r2d2.evolutionary_algorithm.training import initialize_population, evolve_population
from r2d2.evolutionary_algorithm.objective import objective_function
import pybullet as p
import pybullet_data # type: ignore

from r2d2.analysis.fitness_plot import plot_fitness_evolution
from r2d2.analysis.parameter_analysis import analyze_parameters
from r2d2.analysis.final_performance import visualize_best_solution
import os
import re
import numpy as np

# Connect to PyBullet physics server
p.connect(p.GUI)  # Use p.DIRECT for no GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # To load URDF from PyBullet's data path

# Load the R2D2 robot to count its joints
robot_id = p.loadURDF("r2d2.urdf")
num_joints = p.getNumJoints(robot_id)
p.resetSimulation()

# Main script
population_size = 6
num_generations = 10
num_parameters = num_joints  # Dynamically set number of parameters based on the robot's joints

# Define the directory and regex pattern for the date
directory = 'r2d2/evolutionary_algorithm/trained_models'
date_pattern = r'best_generation_info_\d{14}.npy'  # Adjust the pattern as needed

# Search for files that match the regex pattern
matching_files = [f for f in os.listdir(directory) if re.match(date_pattern, f)]

# Optionally, sort the files by date or other criteria
# For simplicity, let's assume you want the first matching file
if matching_files:
    selected_file = matching_files[0]  # or use sorting logic to select a specific file
    population_file_path = os.path.join(directory, selected_file)
    population = np.load(population_file_path, allow_pickle=True)
    parameters_list = [item['parameters'] for item in population]
    population = np.array(parameters_list)
    print("Found matching file:", selected_file, "\nLoading population from file.")
else:
    # Handle the case where no matching file is found
    print("No matching file found. Initializing a new population.")
    population = initialize_population(population_size, num_parameters)  # Assuming this function exists

# Continue with the evolutionary algorithm
final_population, best_fitnesses, avg_fitnesses, worst_fitnesses, population_history = evolve_population(population, num_generations, objective_function)

# Disconnect from the physics server
p.disconnect()

# Post-training analysis
plot_fitness_evolution(best_fitnesses, avg_fitnesses, worst_fitnesses)
analyze_parameters(population_history)
best_solution = max(final_population, key=lambda candidate: objective_function(candidate))
visualize_best_solution(best_solution)