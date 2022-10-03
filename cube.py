from vpython import * 

N = 2 # N by N by N array of atoms
# Surrounding the N**3 atoms is another layer of invisible fixed-position atoms
# that provide stability to the lattice.
k = 10
m = 1
spacing = 1
atom_radius = 0.25*spacing
L0 = spacing-1.8*atom_radius
V0 = pi*(0.5*atom_radius)**2*L0 # initial volume of spring
scene.center = 0.5*(N-1)*vector(1,1,1)
dt = 0.004*(2*pi*sqrt(m/k))
axes = [vector(1,0,0), vector(0,1,0), vector(0,0,1)]


floor = box(pos = vector(0,0,0), length = 10, width = 10, height = 1)
u = 5


class crystal:
        
    def __init__(self,  N, atom_radius, spacing, momentumRange ):
        self.atoms = []
        self.springs = []
        
        # Create (N+2)^3 atoms in a grid; the outermost atoms are fixed and invisible
        for z in range(-1,N+1,1):
            for y in range(-1,N+1,1):
                for x in range(-1,N+1,1):
                    atom = sphere()
                    atom.pos = vector(x,y,z)*spacing
                    atom.radius = atom_radius
                    atom.color = vector(0,0.58,0.69)
                    if 0 <= x < N and 0 <= y < N and 0 <= z < N:
                        p = vec.random()
                        #p = 0
                        atom.momentum = momentumRange*p
                        #atom.momentum = vector(0,-9.81,0)
                    else:
                        atom.visible = False
                        atom.momentum = vec(0,0,0)
                    atom.index = len(self.atoms)
                    self.atoms.append( atom )
        for atom in self.atoms:
            if atom.visible:
                if atom.pos.x == 0:
                    self.make_spring(self.atoms[atom.index-1], atom, False)
                    self.make_spring(atom, self.atoms[atom.index+1], True)
                elif atom.pos.x == N-1:
                    self.make_spring(atom, self.atoms[atom.index+1], False)
                else:
                    self.make_spring(atom, self.atoms[atom.index+1], True)

                if atom.pos.y == 0:
                    self.make_spring(self.atoms[atom.index-(N+2)], atom, False)
                    self.make_spring(atom, self.atoms[atom.index+(N+2)], True)
                elif atom.pos.y == N-1:
                    self.make_spring(atom, self.atoms[atom.index+(N+2)], False)
                else:
                    self.make_spring(atom, self.atoms[atom.index+(N+2)], True)
                    
                if atom.pos.z == 0:
                    self.make_spring(self.atoms[atom.index-(N+2)**2], atom, False)
                    self.make_spring(atom, self.atoms[atom.index+(N+2)**2], True)
                elif atom.pos.z == N-1:
                    self.make_spring(atom, self.atoms[atom.index+(N+2)**2], False)
                else:
                    self.make_spring(atom, self.atoms[atom.index+(N+2)**2], True)
    
    # Create a grid of springs linking each atom to the adjacent atoms
    # in each dimension, or to invisible motionless atoms
    def make_spring(self, start, end, visible):
        spring = helix()
        spring.pos = start.pos
        spring.axis = end.pos-start.pos
        spring.visible = visible
        spring.thickness = 0.5* atom_radius
        spring.radius = 0.0001
        spring.length = spacing
        spring.start = start
        spring.end = end
        spring.color = color.orange
        self.springs.append(spring)

c = crystal(N, atom_radius, spacing, 0.00001*spacing*sqrt(k/m))

for atom in c.atoms:
    if atom.visible:
        atom.pos.y += u

g = vector(0,-9.81,0)

while True:
    rate(60)
    for atom in c.atoms:
        if atom.visible:
            Fnet = m * g
            atom.momentum = atom.momentum + Fnet *dt
            atom.velocity = atom.momentum / m
            atom.pos = atom.pos + atom.velocity*dt
            if atom.pos.y <= floor.height/2 + atom_radius:
                atom.momentum.y = -atom.momentum.y
                atom.pos.y += 0.01

    for spring in c.springs:
        spring.axis = spring.end.pos - spring.start.pos
        L = mag(spring.axis)
        spring.axis = spring.axis.norm()
        spring.pos = spring.start.pos+0.5*atom_radius*spring.axis
        Ls = L-atom_radius
        spring.length = Ls
        Fdt = spring.axis * (k*dt * (1-spacing/L))
        if spring.start.visible:
            spring.start.momentum = spring.start.momentum + Fdt
        if spring.end.visible:
            spring.end.momentum = spring.end.momentum - Fdt
