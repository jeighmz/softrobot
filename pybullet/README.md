# R2D2 Simulation

This is a simple simulation of R2D2 using PyBullet.

## Requirements

- Python
- PyBullet

## Installation

1. Install Python.
2. Install PyBullet by running `pip install pybullet` in your terminal.

## Running the Simulation

1. Run `python3 r2d2/sim-key-control.py` in your terminal.

## Running the Evoluionary Algorithm training:

1. Run `export PYTHONPATH=$(pwd)` in your terminal.
2. Run `python3 r2d2/evolutionary_algorithm/main.py`

## How it Works

The script `sim-control.py` connects to a PyBullet physics server in GUI mode, sets up a real-time simulation with gravity, and loads a plane and an R2D2 URDF.

The simulation runs indefinitely, listening for key events. The 'up' and 'down' arrow keys control the target velocity of R2D2, while the 'left' and 'right' arrow keys control the turn direction.

The script iterates over all joints of R2D2, and if a joint is a wheel joint, it controls the joint based on the target velocity and turn direction.

The simulation steps forward and then sleeps for a short time before repeating the loop.

## License

This project is licensed under the terms of the MIT license.