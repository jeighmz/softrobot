import pybullet as p
import pybullet_data
import numpy as np

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
    
    # Apply the parameters to the robot joints using velocity control
    for joint_index, param in enumerate(robot_parameters):
        p.setJointMotorControl2(robot_id, joint_index, p.VELOCITY_CONTROL, targetVelocity=param, force=500)
    
    # Run the simulation for a certain number of steps
    for _ in range(2000):  # Increased steps to observe more movement
        p.stepSimulation()
    
    # Calculate the performance (e.g., distance to target)
    target_position = [0, 10, 0]
    robot_position = p.getBasePositionAndOrientation(robot_id)[0]
    distance_to_target = np.linalg.norm(np.array(target_position) - np.array(robot_position))
    
    return -distance_to_target  # The negative distance (we want to minimize distance)