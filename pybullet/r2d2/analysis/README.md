# R2D2 Evolutionary Algorithm (EA) Implementation Analysis

This directory contains the analysis tools for the R2D2 Evolutionary Algorithm (EA) implementation. These tools are designed to help visualize and understand the performance and evolution of the algorithm over time.

## Files Overview

- `parameter_analysis.py`: This script analyzes the evolution of parameters in the population history. It plots the average and best parameter values across generations, helping to visualize how the parameters evolve.

- `fitness_plot.py`: This script plots the evolution of fitness over generations. It shows the best, average, and worst fitness values for each generation, providing insights into the algorithm's optimization process.

- `final_performance.py`: This script visualizes the best solution found by the EA. It connects to a physics server, resets the simulation, loads the plane and robot, applies the best parameters to the robot joints, runs the simulation for a certain number of steps, and then disconnects from the physics server. This visualization helps in understanding how the best-found parameters perform in a simulated environment.

## Usage
To use these analysis tools, ensure you have the necessary dependencies installed. You can find all the required dependencies listed in the `requirements.txt` file. 

The analysis is automatically executed via function calls from within `main.py` and happens at the end of the training pipeline. Each script can be run independently to analyze different aspects of the EA's performance.

## Individual script calling
### Analyzing Parameter Evolution

Run `parameter_analysis.py` with a list of population history as input to visualize the parameter evolution:

```bash
python parameter_analysis.py
```

### Plotting Fitness Evolution

Run `fitness_plot.py` with lists of best, average, and worst fitness values for each generation:

### Visualizing the Best Solution

Run `final_performance.py` with the best parameters list to see the best solution in action:

### Contributing
Contributions to improve these analysis tools are welcome. Please ensure to follow the project's contribution guidelines and code of conduct.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
