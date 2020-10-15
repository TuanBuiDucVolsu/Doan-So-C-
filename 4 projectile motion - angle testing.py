from visual import *

scene.width = 1300
scene.height = 1000
scene.autoscale = False

launch_pos = vector(-5,0,0) # Initial position of projectile.

### Make display adjustable.
global drag,lastpos
drag = False
def down():
    global drag,lastpos
    #print "mousedown"
    scene.center = scene.mouse.pos
    drag = True
    lastpos = vector(scene.mouse.pos.x,scene.mouse.pos.y,0)

##def move(): ### Not working yet...
##    global drag, lastpos
##    if drag: # mouse button is down
##        dpos = scene.mouse.pos-lastpos
##        scene.center += dpos
##        lastpos = vector(scene.mouse.pos.x,scene.mouse.pos.y,0)
##        print scene.center

def up():
    global drag
    drag = False

scene.bind("mousedown", down)

#scene.bind("mousemove", move)

scene.bind("mouseup", up)
###

use_ruler = True
## Start rulers at projectile initial position.
if (use_ruler):
    # Make x-axis.
    dx = 1.0 # Box center-to-center separation (AKA ruler marking).
    box_x = launch_pos.x + 0.5*dx # Box's x-coordinate.
    box_x_max = -box_x ## Will likely need to change.
    while box_x <= box_x_max:
        box(pos=(box_x,-0.05,0),
            size=(0.95*dx,0.05,0.05),
            color=color.white,
            opacity=0.5)
        box_x += dx

    # Make y-axis.
    dy = dx # Box center-to-center separation (AKA ruler marking).
    box_y = launch_pos.y + 0.5*dy # Box's y-coordinate.
    box_y_max = max(-box_y,box_x_max) ## Will likely need to change.
    ### May need to generate more ruler boxes within the motion loop.
    while box_y <= box_y_max:
        box(pos=(-0.05,box_y,0),
            size=(0.05,0.95*dy,0.05),
            color=color.white,
            opacity=0.5)
        box_y += dy

### Projectile information here.

## Loop over initial angle.
angle = 5 # Initial angle measured in degrees.
delta_angle = 5
max_angle = 90

while (angle <= max_angle):

    projectile = sphere(pos = launch_pos,
                        radius = 0.1,
                        color = color.red,
                        make_trail = True)


    projectile.speed = 4.0 # Initial speed.
    projectile.angle = angle*3.141459/180 # Initial angle, from the +x-axis.

    projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                                 projectile.speed*sin(projectile.angle),
                                 0)



    projectile.mass = 1.0
    grav_field = 1.0

    dt = 0.01
    time = 0

    while (projectile.pos.y >=0):
        rate(150)

        # Calculate the force.
        grav_force = vector(0,-projectile.mass*grav_field,0)

        force = grav_force
        
        # Update velocity.
        projectile.velocity = projectile.velocity + force/projectile.mass * dt

        # Update position.
        projectile.pos = projectile.pos + projectile.velocity * dt

        # Update time.
        time = time + dt

        # Add ruler boxes as necessary.
        if (projectile.pos.x > box_x_max):
            # Add box on x-axis.
            box_x_max += dx
            box(pos=(box_x_max,-0.05,0),
                size=(0.95*dx,0.05,0.05),
                color=color.white,
                opacity=0.5)

        if (projectile.pos.y > box_y_max):
            # Add box on y-axis.
            box_y_max += dy
            box(pos=(-0.05,box_y_max,0),
                size=(0.05,0.95*dy,0.05),
                color=color.white,
                opacity=0.5)

    angle += delta_angle
