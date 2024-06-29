import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Initialize the font module
pygame.font.init()

# Create a font object
font = pygame.font.SysFont(None, 24)

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Ball Physics Simulation")

# Set up the ball
ball_radius = 20
ball_color = (255, 0, 0)
ball_pos = [width // 2, 0]
ball_velocity = [0, 0]
ball_mass = 5
gravity = 0.01
friction = 0.1



mouse_down = False
last_mouse_pos = [0, 0]


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] - ball_pos[0])**2 + (pygame.mouse.get_pos()[1] - ball_pos[1])**2 <= ball_radius**2:
                mouse_down = True
                last_mouse_pos = list(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_down:
                mouse_down = False
                ball_velocity = [(ball_pos[0] - last_mouse_pos[0]) / 5, (ball_pos[1] - last_mouse_pos[1]) / 5]

    # Update ball position
    ball_velocity[1] += gravity
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check for collision with the ground or the ceiling
    if ball_pos[1] + ball_radius >= height or ball_pos[1] - ball_radius <= 0:
        ball_velocity[1] = -ball_velocity[1] * 0.8
        ball_pos[1] = height - ball_radius if ball_pos[1] + ball_radius >= height else ball_radius

    # Check for collision with the sides
    if ball_pos[0] + ball_radius >= width or ball_pos[0] - ball_radius <= 0:
        ball_velocity[0] = -ball_velocity[0] * 0.8
        ball_pos[0] = width - ball_radius if ball_pos[0] + ball_radius >= width else ball_radius

    # If the mouse button is down and the cursor is within the ball, move the ball with the cursor
    if mouse_down and (pygame.mouse.get_pos()[0] - ball_pos[0])**2 + (pygame.mouse.get_pos()[1] - ball_pos[1])**2 <= ball_radius**2:
        ball_pos = list(pygame.mouse.get_pos())

    # Clear the screen
    screen.fill((255, 255, 255))

    # Calculate speed
    speed = math.sqrt(ball_velocity[0]**2 + ball_velocity[1]**2)
    momentum = ball_mass * speed 

    

    # Render the text
    acceleration_text = font.render(f'Acceleration (a): {gravity}', True, (0, 0, 0))
    velocity_text = font.render(f'Velocity (v): {ball_velocity}', True, (0, 0, 0))
    position_text = font.render(f'Position (x): {ball_pos}', True, (0, 0, 0))
    speed_text = font.render(f'Speed (s): {speed}', True, (0, 0, 0))
    ball_mass_text = font.render(f'Mass: {ball_mass}', True, (0, 0, 0))
    momentum_text = font.render(f'Momentum (p): {momentum}', True, (0, 0, 0))  
    friction_text = font.render(f'Friction (μ): {friction}', True, (0, 0, 0)) 


    # Blit the text onto the screen
    screen.blit(acceleration_text, (10, 10))
    screen.blit(velocity_text, (10, 50))
    screen.blit(position_text, (10, 90))
    screen.blit(speed_text, (10, 130))
    screen.blit(ball_mass_text, (10, 560))
    screen.blit(momentum_text, (10, 580))
    screen.blit(friction_text, (100, 560))


    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()