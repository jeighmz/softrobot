import pybullet as p
import pybullet_data
import numpy as np
import random
import json
import os
import datetime


def save_training_data(data, filename):
    """Save the training data to a file."""
    directory = os.path.dirname(filename)
    
    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Add the current timestamp to the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename_with_timestamp = f"{filename}_{timestamp}"
    
    # Now save the data
    with open(filename_with_timestamp, "w") as f:
        json.dump(data, f)

def objective_function(robot_parameters):
    # Connect to the physics server
    if p.getConnectionInfo()['isConnected'] == 0:
        p.connect(p.GUI)  # Use p.DIRECT for no GUI

    # Reset the simulation
    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # To load URDF from PyBullet's data path
    p.setGravity(0, 0, -9.8)
    
    # Load the plane
    plane_id = p.loadURDF("plane.urdf")

    # Set the robot's initial position above the plane
    start_position = [0, 0, 1]  # Adjust z value as needed
    start_orientation = p.getQuaternionFromEuler([0, 0, 0])
    
    # Load the robot
    robot_id = p.loadURDF("r2d2.urdf", start_position, start_orientation)
    
    wheel_joint_indices = [2, 3, 6, 7]  # Assuming wheel joints are at indices 2 and 3

    for joint_index, param in enumerate(robot_parameters):
        if joint_index in wheel_joint_indices:
            p.setJointMotorControl2(robot_id, joint_index, p.VELOCITY_CONTROL, targetVelocity=param, force=500)

    # Run the simulation for a certain number of steps
    # Generate a random number of steps within a specified range for the simulation
    try:
        # Generate a random number of steps within a specified range for the simulation
        min_steps = 2000
        max_steps = 3000
        random_steps = random.randint(min_steps, max_steps)  # Random number of steps between min_steps and max_steps

        for _ in range(random_steps):
            p.stepSimulation()

        # Code to evaluate the robot's performance goes here...

        # Calculate the performance (e.g., distance to target)
        target_position = [0, 10, 0]
        robot_position = p.getBasePositionAndOrientation(robot_id)[0]
        distance_to_target = np.linalg.norm(np.array(target_position) - np.array(robot_position))

    except p.error as e:
        if "Not connected to physics server" in str(e):
            # Save the most recent training data before handling the error
            save_training_data(robot_parameters, "r2d2/evolutionary_algorithm/trained_models/latest_training_data.json")
            print("Error: Not connected to physics server. Latest training data saved.")
            # Handle the error, e.g., attempt to reconnect, log the error, or skip this simulation
        else:
            raise  # Re-raise the exception if it's not the specific error we're handling
   
    
    
    return -distance_to_target  # The negative distance (we want to minimize distance)