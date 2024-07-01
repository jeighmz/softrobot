from r2d2.evolutionary_algorithm.training import initialize_population, evolve_population
from r2d2.evolutionary_algorithm.objective import objective_function
import pybullet as p
import pybullet_data

from r2d2.analysis.fitness_plot import plot_fitness_evolution
from r2d2.analysis.parameter_analysis import analyze_parameters
from r2d2.analysis.final_performance import visualize_best_solution

# Connect to PyBullet physics server
p.connect(p.GUI)  # Use p.DIRECT for no GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # To load URDF from PyBullet's data path

# Load the R2D2 robot to count its joints
robot_id = p.loadURDF("r2d2.urdf")
num_joints = p.getNumJoints(robot_id)
p.resetSimulation()

# Main script
population_size = 20
num_generations = 8
num_parameters = num_joints  # Dynamically set number of parameters based on the robot's joints

# Initialize population and run evolutionary algorithm
population = initialize_population(population_size, num_parameters)
final_population, best_fitnesses, avg_fitnesses, worst_fitnesses, population_history = evolve_population(population, num_generations, objective_function)

# Disconnect from the physics server
p.disconnect()

# Post-training analysis
plot_fitness_evolution(best_fitnesses, avg_fitnesses, worst_fitnesses)
analyze_parameters(population_history)
best_solution = max(final_population, key=lambda candidate: objective_function(candidate))
visualize_best_solution(best_solution)