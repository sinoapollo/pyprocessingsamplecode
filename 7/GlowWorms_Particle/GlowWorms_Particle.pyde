"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 借鉴自openprocessing.org
             学习重点：粒子系统
"""

GRAVITY = -0.1
MOTION_BLUR = True


def setup() :
    global system
    size(800, 800)
    system = ParticleSystem()

def draw() :
    global system
    drawBackground()
    system.update()

def mouseDragged() :
    global system
    for i in range(3):
        system.particles.append(Particle(PVector(mouseX, mouseY)))

def drawBackground() :
    global MOTION_BLUR
    if (MOTION_BLUR) :
        # Background with motion blur
        noStroke()
        fill(0, 20)
        rect(0, 0, width, height)
    else :
        # Normal background
        background(0)

class ParticleSystem:
    def __init__(self) :
        self.particles = []
  
    def update(self) :
        for p in self.particles :
            # Apply gravity
            p.applyForce(PVector.random2D())
            # Move particle position
            p.move()
      
            # Remove dead particles
            if p.isDead():
                del(p)
            else :
                p.display()

class Particle :
  
    def __init__(self, p):
        self.BOUNCE = -0.5
        self.MAX_SPEED = 0.1
    
        self.vel = PVector(random(-self.MAX_SPEED,self.MAX_SPEED), random(-self.MAX_SPEED, self.MAX_SPEED))
        #acc = PVector(0, 0)
        #pos = PVector(0, 0)
    
        self.mass = random(2, 2.5)
        self.size = random(0.1, 2.0)
        #float r, g, b
        self.lifespan = 255
        self.pos = PVector (p.x, p.y)
        self.acc = PVector (random(0.1, 1.5), 0)
        self.r = random (100, 255)
        self.g = random (0, 50)
        self.b = 0

    def move(self) :
        self.vel.add(self.acc) # Apply acceleration
        self.pos.add(self.vel) # Apply our speed vector
        self.acc.mult(0)
    
        self.size += 0.01 #0.015
        self.lifespan -= 1

    def applyForce(self, force) :
        f = PVector.div(force, self.mass)
        self.acc.add(f)

    def display(self) :
        # Colour based on x and y velocity
        fill(constrain(abs(self.vel.y) * 100, 0, 255), constrain(abs(self.vel.x) * 100, 0, 255), self.b, self.lifespan)
        ellipse(self.pos.x, self.pos.y, self.size * 4, self.size * 4)

    def isDead(self) :
        if self.lifespan < 0 or self.pos.x > width or self.pos.x < 0 or self.pos.y > height or self.pos.y < 0 :
            return True
        return False
