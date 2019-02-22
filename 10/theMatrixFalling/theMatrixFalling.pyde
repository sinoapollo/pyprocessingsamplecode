"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 借鉴自github.org
             学习重点：unicode字符, 类的运用
"""

streams = []

def tsize() :
    return 24

def setup():
    global streams
    size(1800, 1000)
    textFont(createFont('STHeiti', tsize()))
    x = 0
    for i in range(width / tsize() + 1):
        stream = Stream(x)
        streams.append(stream)
        x += tsize()

def draw():
    global streams
    background(0, 150)
    for stream in streams:
        stream.render()

class Symbol:
    def __init__(self, x, y, speed, first):
        self.x = x
        self.y = y
        self.value = 0
        self.__speed = speed
        self.__switchInterval = round(random(2,20))
        self.first = first
    
    def setToRandomSymbol(self):
        if (frameCount % self.__switchInterval == 0):
            self.value = unichr(0x30A0 + round(random(0, 96)))

    def rain(self):
        self.y += self.__speed

class Stream():
    def __init__(self, x) :
        self.__symbols = []
        self.__totalSymbols = round(random(5, 30))
        self.__speed = random(5, 30)
        self.__generateSymbols(x, random(-750, 0))

    def __generateSymbols(self, x, y):
        first = round(random(0, 4)) == 1
        for i in range(ceil(self.__totalSymbols)):
            symbol = Symbol(x, y, self.__speed, first)
            symbol.setToRandomSymbol()
            self.__symbols.append(symbol)
            y -= tsize()
            first = False

    def render(self):
        lastY = 0
        lastX = 0
        for symbol in self.__symbols:
            if (symbol.first):
                fill(180, 255, 180)
            else :
                fill(0, 255, 70, 125)
            text(symbol.value, symbol.x, symbol.y)
            symbol.rain()
            symbol.setToRandomSymbol()
            lastX = symbol.x
            lastY = symbol.y
        if lastY > height :
            self.__init__(lastX)
