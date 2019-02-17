"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 借鉴自openprocessing.org
             学习重点：粒子系统基本概念
"""

def setup() :
    global _fire;
    size(400, 400)
    _fire = Fire()
    _fire.init();

def draw() :
    global _fire;
    background(0)
    _fire.update()

class Fire :

    __particleCount = 0

    #Particle[] _particles;
    __RARTICLE_MIN = 0
    __PARTICLE_MAX = 5000
    __COUNT_MAX = 15
    __FIRE_CENTER = 0;

    def __init__(self):
        pass

    def init(self) :
        self._particles = [] #Particle[self.__PARTICLE_MAX]
        count = 0
        for i in range(self.__PARTICLE_MAX) :
            self._particles.append(Particle())
            self._particles[i].init(count)
            count = (count + 1) % self.__COUNT_MAX
        self._particleCount = self.__RARTICLE_MIN
        self.__FIRE_CENTER = width/2

    def update(self) :
        count = 0
        for i in range(self.__particleCount) :
            self._particles[i].positionUp();
            self._particles[i].draw();
            if self._particles[i].getY() < 0 :
                self._particles[i].init(count)
                count = (count + 1) % self.__COUNT_MAX
        if self.__particleCount < self.__PARTICLE_MAX :
            self.__particleCount += 50
  
    def setParticleCount(self, particleCount) :
        self.__particleCount = floor((100.0/self.__PARTICLE_MAX)*100)


class Particle :    
    RANGE_X = 25
    RANGE_Y = 5
    SPEED_Y = 3

    def __init__(self) :
        pass

    def init(self, count) :
        self.__x = width/2 + random(-self.RANGE_X + count, self.RANGE_X - count)
        self.__y = height/2 + height/4 +random(-self.RANGE_Y, self.RANGE_Y + count)
        self.__redPower = 255
        self.__greenPower = 165
        self.__bluePower = 0
        self.__alphaPower = 255
        self.__size = 10

    def draw(self) :
        smooth()
        noStroke()
        fill(self.__redPower, self.__greenPower, self.__bluePower, self.__alphaPower/2)
        ellipse(self.__x - (self.__size/2), self.__y - (self.__size/2), self.__size, self.__size*2)


    def positionUp(self) :
        #color adjustment
        if self.__redPower >= 0 and self.__redPower <= 255 :
            self.__redPower += 1
        if self.__greenPower >= 0 and self.__greenPower <= 255 :
            self.__greenPower -= 5
        if self.__bluePower >= 0 and self.__bluePower <= 255 :
            self.__bluePower -= 1
        self.__alphaPower -= 3
        if self.__alphaPower < 0 :
            self.__alphaPower = 0
        self.__y -= self.SPEED_Y
        self.__size -= 0.1
        if self.__x > width / 2 + random(0, self.RANGE_X/2) :
            self.__x -= 0.2;
        elif self.__x < width / 2 - random(-self.RANGE_X/2, 0) :
            self.__x += 0.2


    def getY(self) :
        return self.__y
