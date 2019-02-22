"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 借鉴自openprocessing.org
             学习重点：类
"""


def setup () :
    global tree
    pixelDensity (displayDensity ())
    size (800, 600)
    background (255)
    colorMode (RGB, 255, 255, 255, 100)
    tree = Branches(80.0)
    frameRate(10)

def draw () :
    global tree
    tree.draw()

class Branches:
    def __init__(self, sl):
        self.__branches = []
        self.color = 0
        self.weight = 0
        self.offset = -90.0
        sx = random (width)
        self.__branches.append (Branch (sx, height, sx, height - sl, sl, 0.0))
    def draw(self):
        self.color = len(self.__branches) / 5.0
        self.weight = 3.0 / (len(self.__branches) / 100 + 1)
        blen = len(self.__branches)
        for i in range(blen) :
            b = self.__branches[i]
            b.render (self.color, self.weight)
            b.update ()
            for i in range(floor(random(2, 4))) :
                sx = b.endx
                sy = b.endy
                sl = random (random (10.0, 20.0), b.length * 0.99)
                sd = random (-60.0, 60.0)
                ex = sx + sl * cos (radians (sd + b.degree + self.offset))
                ey = sy + sl * sin (radians (sd + b.degree + self.offset))
                self.__branches.append (Branch (sx, sy, ex, ey, sl, sd + b.degree))
        if (len(self.__branches) > 6000) :
            self.__init__(random (0.0, 180.0))

class Branch:
    def __init__(self, sx, sy, ex, ey, sl, sd) :
        self.startx = sx
        self.starty = sy
        self.endx = ex
        self.endy = ey
        self.length = sl
        self.degree = sd
        self.nextx = self.startx
        self.nexty = self.starty
        self.prevx = self.startx
        self.prevy = self.starty
        self.next_flag = True
        self.draw_flag = True
    
    def update(self) :
        self.nextx += (self.endx - self.nextx) * 0.4
        self.nexty += (self.endy - self.nexty) * 0.4
        if abs (self.nextx - self.endx) < 1.0 and abs (self.nexty - self.endy) < 1.0 and self.next_flag :
            self.next_flag = False
            self.draw_flag = False
            self.nextx = self.endx
            self.nexty = self.endy

    def render(self, bcolor, bweight) :
        if self.draw_flag :
            stroke (bcolor)
            strokeWeight (bweight)
            line (self.prevx, self.prevy, self.nextx, self.nexty)
        self.prevx = self.nextx
        self.prevy = self.nexty
