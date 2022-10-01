from vpython import *
from time import *
import numpy as np
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('--theta', type=float, required=True)
parser.add_argument('--v', type = int, required = True)

args = parser.parse_args()

## GRAVITY AND MOMENTUM

scene = canvas()
scene.width = 1000
scene.height = 600

x = box(pos= vector(0,20,0), length = 10, width = 1/2, height = 1/2, color = color.red)
y = box(pos= vector(0,20,0), length = 1/2, width = 10, height = 1/2, color = color.blue)
z = box(pos= vector(0,20,0), length = 1/2, width = 1/2, height = 10, color = color.yellow)

floor = box(pos = vector(0,0,0), length = 100, width = 10, height = 1)

v0 = args.v
p0 = vector(0,0,0)

direction= vector(cos(args.theta), sin(args.theta), +0)

ball = sphere(pos = vector(0,5,0), velocity = vector(0,0,0), color = color.green, radius = 1.0, make_trail = True)
ball.mass = 10
ball.p = ball.mass*v0*vector(direction)
g = vector(0,-9.81, 0)
damp = 0.9999

t = 0
dt = 0.01

horizontal_displacement = np.linalg.norm(p0.x - ball.pos.x)

def mag(x,y,z):
    k = math.sqrt(x**2+y**2+z**2)
    return k

while t<100:
    rate(100)
    Fnet = ball.mass * g
    
    ball.p = ball.p + Fnet *dt
    ball.velocity = ball.p/ball.mass
    ball.pos = ball.pos*damp+ball.velocity*dt
    
    if (ball.pos.y - ball.radius <= floor.pos.y + floor.height/2 and (-floor.length/2< ball.pos.x <floor.length/2)):
        ball.p.y = -ball.p.y
    #check case: negligable boost to avoid object boundaries crossing
        ball.pos.y+=0.001

    scene.caption= """A model of momentum and gravity on a launched projectile:


Input Parameters

    θ:    {} degrees
    v0:   {} m/s

Values:

    velocity:   {:.4f} m/s

    distance: {:.4f} """.format(args.theta, args.v, mag(ball.velocity.x, ball.velocity.y, ball.velocity.z), horizontal_displacement)

    horizontal_displacement = np.linalg.norm(p0.x - ball.pos.x)
    t= t+dt