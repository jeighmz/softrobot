from vpython import *
from time import *

## GRAVITY AND MOMENTUM


scene = canvas()

x = box(pos= vector(10,20,0), length = 10, width = 1, height = 1, color = color.red)
y = box(pos= vector(10,20,0), length = 1, width = 10, height = 1, color = color.blue)
z = box(pos= vector(10,20,0), length = 1, width = 1, height = 10, color = color.yellow)

floor = box(pos = vector(0,0,0), length = 100, width = 20, height = 1)

v0 = 10
direction= vector(+0.11, +0.31, +0)

ball = sphere (pos = vector(-50,5,0), velocity = vector(0,0,0), color = color.green, radius = 1.0, make_trail = True)
ball.mass = 10
ball.p = ball.mass*v0*vector(direction)
g = vector (0,-9.81, 0)
damp = 0.998

t = 0
dt = 0.01

while t<100:
    rate(100)
    Fnet = ball.mass * g
    
    ball.p = ball.p + Fnet *dt
    ball.velocity = ball.p/ball.mass
    ball.pos = ball.pos+ball.velocity*damp*dt
    
    if (ball.pos.y - ball.radius <= floor.pos.y + floor.height/2 and ball.pos.x <floor.length/2):
        ball.p.y = -ball.p.y
        ball.pos.y+=0.001
    #dist = ball.pos.y
    #if dist <= 2*floor.height/3:
    #    ball.pos.y+=ball.radius/2
    
    t= t+dt