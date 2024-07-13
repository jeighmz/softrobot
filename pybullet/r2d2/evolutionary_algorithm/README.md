# R2D2 Evolutionary Algorithm Implementation

This directory contains the implementation of an Evolutionary Algorithm (EA) for optimizing the parameters of an R2D2 robot simulation. The goal is to evolve the robot's parameters to improve its performance in a simulated environment.

## Directory Structure

- `training.py`: Contains the core logic for the evolutionary algorithm, including population initialization, evolution, and the reproduction mechanisms.
- `objective.py`: Defines the objective function used to evaluate the fitness of each individual in the population. It interacts with the PyBullet physics engine to simulate the R2D2 robot's performance.
- `main.py`: The main script that sets up the simulation environment, runs the evolutionary algorithm, and performs post-training analysis.

## Dependencies

- `numpy`: Used for numerical operations.
- `pybullet`: The physics engine used for and optimizing its parameters for better performance. The process will continue for a predefined number of generations, with the best-performing individuals being selected for reproduction at each step.

## Usage

1. **Install Dependencies**: First, make sure Python 3.x is installed on your system. Then, install the necessary Python packages using the following command:

    ```bash
    pip install requirements.txt
    ```

2. **Run the Simulation**: To start the evolutionary algorithm, navigate to the directory containing `main.py` and run the script using:

    ```bash
    python main.py
    ```

    This command initiates the simulation of the R2D2 robot within the PyBullet environment and begins the evolutionary process to optimize its performance.

## Configuration

The behavior of the evolutionary algorithm can be customized by modifying the relevant variables within the `main.py` file. These variables include parameters such as population size, mutation rate, and the number of generations. Adjust these settings directly in the code to experiment with different evolutionary strategies and observe how they affect the optimization process.

## Results

After the simulation completes, the results will be saved in the `trained_models` directory. This includes a log of the fitness scores over time, as well as the final optimized parameters for the R2D2 robot. Use these results to analyze the effectiveness of the evolutionary algorithm and to further refine the simulation parameters for improved performance.

## Contributing

Contributions to the R2D2 Evolutionary Algorithm project are welcome. Please submit pull requests or open issues to discuss proposed changes or report bugs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.