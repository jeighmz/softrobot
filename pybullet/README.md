# R2D2 Simulation

This is a simple simulation of R2D2 using PyBullet.

## Requirements

- Python
- PyBullet

## Installation

1. Create a virtual python environment `python3 -m venv pybullet-venv`
2. Activate the environment with `source pybullet-venv/bin/activate`
3. Install PyBullet and other dependencies by running `pip3 install -r requirements.txt` in your terminal

## Running the Simulation

1. Run `python3 r2d2/sim-key-control.py` in your terminal.

## Running the Evoluionary Algorithm training:

1. Run `export PYTHONPATH=$(pwd)` in your terminal.
2. Run `python3 r2d2/evolutionary_algorithm/main.py`

## How it Works

The script `sim-key-control.py` connects to a PyBullet physics server in GUI mode, sets up a real-time simulation with gravity, and loads a plane and an R2D2 URDF.

The simulation runs indefinitely, listening for key events. The 'up' and 'down' arrow keys control the target velocity of R2D2, while the 'left' and 'right' arrow keys control the turn direction.

The script iterates over all joints of R2D2, and if a joint is a wheel joint, it controls the joint based on the target velocity and turn direction.

The simulation steps forward and then sleeps for a short time before repeating the loop.

The Evolutionay Algorithm trains automatically, and is not controllable by the user. You may change the population size or the number of generations that the algorithm will train towards it's objective. In this case the objective is to reach a position <0,1,0> which is directly forward.

## License

This project is licensed under the terms of the MIT license.
