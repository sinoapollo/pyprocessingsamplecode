"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 借鉴自openprocessing.org
             学习重点：读取图像文件，像素及处理，列表，颜色
"""

imgs = []
imgIndex = -1
subStep = 800
z = 0
isStop = False
count = 0

def setup() :
    global imgs, paint
    size(600, 600)
    imgs.append(loadImage("demo.jpg"))
    nextImage()
    background(255, 255, 255)
    colorMode(RGB, 255, 255, 255, 255)
    
def draw() :
    global isStop, subStep, paint, count, z
    if not isStop :
        for i in range(subStep) :
            paint.update()
            paint.show()
            z+= 0.01
    count += 1
    if count > width :
        isStop = True
    #background(255)
    #image(img, 0, 0, width, height)

def keyPressed() :
    global isStop
    if key == 's' or key == 'S' :
        isStop = not isStop

def mouseClicked() :
    global isStop, count
    nextImage()
    isStop = False
    count = 0


def nextImage() :
    global imgIndex, imgs, paint
    img = createImage(width, height, ARGB)#createGraphics(width, height)
    imgIndex = (1 + imgIndex) % len(imgs)
    #img.beginDraw()
    #img.image(imgs[imgIndex], 0, 0, width, height)
    #img.endDraw()
    img.copy(imgs[imgIndex], 0, 0, imgs[imgIndex].width, imgs[imgIndex].height, 0, 0, img.width, img.height);
    img.loadPixels()
    background(255)
    paint = Paint(PVector(width/2, height/2), img)

class Paint :
    def __init__(self, p, img) :
        self.__img = img
        self.__ppos = p.copy()
        self.__pos = p.copy()
        self.__vel = PVector(0, 0)
        self.__force = PVector(0, 0)
        
        self.__maxSpeed = 3.0
        self.__perception = 3
        self.__bound = 60.0
        self.__boundForceFactor = 0.16
        self.__noiseScale = 100.0
        self.__noiseInfluence = 1 / 20.0
        
        self.__dropRate = 0.004
        self.__dropRange = 40
        self.__dropAlpha = 150
        self.__drawAlpha = 50
        self.__drawColor = color(0, 0, 0, self.__drawAlpha)
        self.__drawWeight = 1
        self.__count = 0
        self.__maxCount = 100
    
    def update(self) :
        global z
        self.__ppos = self.__pos.copy()
        self.__force.mult(0)
    
        # Add pixels force
        target = PVector(0, 0)
        count = 0
        for i in range(-1 * floor(self.__perception/2), ceil(self.__perception/2), 1) :
            for j in range(-1 * floor(self.__perception/2), ceil(self.__perception/2), 1) :
                if i == 0 and j == 0 :
                    continue
                x = floor(self.__pos.x + i)
                y = floor(self.__pos.y + j)
                if x <= self.__img.width - 1 and x >= 0 and y < self.__img.height - 1 and y >= 0 :
                    c = self.__img.pixels[y * self.__img.width + x]
                    b = 1 - brightness(c) / 100.0
                    b = random(0, b)
                    p = PVector(i, j)
                    target.add(p.normalize().copy().mult(b).div(p.mag()))
                    count += 1
        if count > 0 :
            self.__force.add(target.div(count))
        
        #Add noise force
        n = noise(self.__pos.x/self.__noiseScale, self.__pos.y/self.__noiseScale, z)
        n = map(n, 0, 1, 0, 5 * TWO_PI)
        p = PVector.fromAngle(n)
        if self.__force.mag() < 0.01 :
            self.__force.add(p.mult(self.__noiseInfluence * 5))
        else :
            self.__force.add(p.mult(self.__noiseInfluence))
           
        # Add bound force
        boundForce = PVector(0, 0)
        if self.__pos.x < self.__bound :
            boundForce.x = (self.__bound - self.__pos.x) / self.__bound
        if self.__pos.x > width - self.__bound :
            boundForce.x = (self.__pos.x - width) / self.__bound
        if self.__pos.y < self.__bound :
            boundForce.y = (self.__bound - self.__pos.y) / self.__bound
        if self.__pos.y > height - self.__bound :
            boundForce.y = (self.__pos.y - height) / self.__bound
        self.__force.add(boundForce.mult(self.__boundForceFactor))
        
        
        self.__vel.add(self.__force)
        self.__vel.mult(0.9999)
        if self.__vel.mag() > self.__maxSpeed :
            self.__vel.mult(self.__maxSpeed / self.__vel.mag())

        self.__pos.add(self.__vel)
        
        if self.__pos.x > width or self.__pos.x < 0 or self.__pos.y > height or self.__pos.y < 0 :
            self.reset()
    
    def reset(self) :
        self.__img.updatePixels()
        self.__img.loadPixels()
    
        self.__count = 0
        #self.__maxCount = 200
        hasFound = False
        while not hasFound :
            self.__pos.x = random(width)
            self.__pos.y = random(height)
            c = self.__img.pixels[floor(self.__pos.y) * self.__img.width + floor(self.__pos.x)]
            b = brightness(c)
            if b < 120 :
                hasFound = True
        self._maxcount = random(80, 120)
        self.__drawColor = self.__img.pixels[floor(self.__pos.y) * self.__img.width + floor(self.__pos.x)]
        self.__drawColor = color(red(self.__drawColor), green(self.__drawColor), blue(self.__drawColor), self.__drawAlpha)
        self.__ppos = self.__pos.copy()
        self.__vel.mult(0)

    def show(self) :
        self.__count += 1
        if self.__count > self.__maxCount :
            self.reset()
        stroke(self.__drawColor)
        strokeWeight(self.__drawWeight)
        if self.__force.mag() > 0.1 and random(1) < self.__dropRate :
            self.__drawColor = color(red(self.__drawColor), green(self.__drawColor), blue(self.__drawColor), self.__dropAlpha)
            stroke(self.__drawColor)
            self.__boldWeight = self.__drawWeight + random(5)
            strokeWeight(self.__boldWeight)
            self.__drawColor = color(red(self.__drawColor), green(self.__drawColor), blue(self.__drawColor), self.__drawAlpha)
        line(self.__ppos.x, self.__ppos.y, self.__pos.x, self.__pos.y)
        self.fadeLineFromImg(self.__ppos.x, self.__ppos.y, self.__pos.x, self.__pos.y)

    # Fade the pixels of the line
    def fadeLineFromImg(self, x1, y1, x2, y2) :
        """self.__img.beginDraw()
        self.__img.stroke(255, 255, 255, 255)
        self.__img.line(x1, y1, x2, y2)
        self.__img.endDraw()
        """
        xOffset = floor(abs(x1 - x2))
        yOffset = floor(abs(y1 - y2))
        step = yOffset if xOffset < yOffset else xOffset #三元
        for i in range(step) :
            x = floor(x1 + (x2 - x1) * i / step)
            y = floor(y1 + (y2 - y1) * i / step)
            originColor = self.__img.pixels[y * self.__img.width + x]
        
            r = red(originColor)
            g = green(originColor)
            b = blue(originColor)
        
            originColor = color(r+50 > 255 and 255 or r+50, g+50 > 255 and 255 or g+50, b+50 > 255 and 255 or b+50, alpha(originColor)) #三元的另一种表示方法
        
            self.__img.pixels[y * self.__img.width + x] = originColor
        #"""
