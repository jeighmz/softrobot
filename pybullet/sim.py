import pybullet as p
import time
import pybullet_data

# Connect to the physics server (GUI mode)
p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Add search path for PyBullet URDFs

# real time
p.setRealTimeSimulation(1)

# Set gravity
p.setGravity(0, 0, -9.8)

# Load the plane and R2D2
planeId = p.loadURDF("plane.urdf")
r2d2Id = p.loadURDF("r2d2.urdf", [0, 0, 1])

# Get the number of joints of R2D2
numJoints = p.getNumJoints(r2d2Id)

targetVelocity = 0  # Target velocity
maxForce = 10  # Maximum force that can be applied to the joint
turn = 0  # Turn direction
increment = 0.5  # Increment for smoother movement

# Simulate indefinitely
while True:
    # Get key events
    keys = p.getKeyboardEvents()
    
    # Check if 'up' arrow key is pressed or held
    if p.B3G_UP_ARROW in keys and (keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN):
        targetVelocity -= increment  # Increase velocity
    
    # Check if 'down' arrow key is pressed or held
    if p.B3G_DOWN_ARROW in keys and (keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN):
        targetVelocity += increment  # Decrease velocity
    
    # Check if 'right' arrow key is pressed or held
    if p.B3G_RIGHT_ARROW in keys and (keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN):
        turn -= increment  # Turn right
    
    # Check if 'left' arrow key is pressed or held
    if p.B3G_LEFT_ARROW in keys and (keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN):
        turn += increment  # Turn left
    
    # Reset velocity and turn when keys are released
    if p.B3G_UP_ARROW in keys and (keys[p.B3G_UP_ARROW] & p.KEY_WAS_RELEASED):
        targetVelocity = 0
    if p.B3G_DOWN_ARROW in keys and (keys[p.B3G_DOWN_ARROW] & p.KEY_WAS_RELEASED):
        targetVelocity = 0
    if p.B3G_RIGHT_ARROW in keys and (keys[p.B3G_RIGHT_ARROW] & p.KEY_WAS_RELEASED):
        turn = 0
    if p.B3G_LEFT_ARROW in keys and (keys[p.B3G_LEFT_ARROW] & p.KEY_WAS_RELEASED):
        turn = 0

    # Ensure targetVelocity and turn are within limits
    targetVelocity = max(min(targetVelocity, 10), -10)
    turn = max(min(turn, 10), -10)

    # Iterate over all joints
    for joint in range(numJoints):
        # Get joint info
        jointInfo = p.getJointInfo(r2d2Id, joint)
        
        # Check if "_wheel_joint" is in the name of the joint
        if "_wheel_joint" in jointInfo[1].decode('utf-8'):
            # Control the joint
            if "left" in jointInfo[1].decode('utf-8'):
                p.setJointMotorControl2(r2d2Id, joint, p.VELOCITY_CONTROL, targetVelocity=targetVelocity + turn, force=maxForce)
            elif "right" in jointInfo[1].decode('utf-8'):
                p.setJointMotorControl2(r2d2Id, joint, p.VELOCITY_CONTROL, targetVelocity=targetVelocity - turn, force=maxForce)
    
    p.stepSimulation()
    time.sleep(1./240.)

# Disconnect from the server
p.disconnect()