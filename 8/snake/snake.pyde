"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 学习重点：键盘响应，条件判断，游戏设计，类定义
"""

def cellSize() :
    return 10

def goThroughBorder() :
    return False

def setup():
    global snake, foods
    size(800, 600)
    frameRate(5)
    snake = Snake()
    foods = Food(5)
    
def draw():
    global snake, foods
    background(255)
    hitIndex = foods.checkPosHit(snake.head())
    if hitIndex >= 0 :
        snake.append()
        foods.remove(hitIndex)
    foods.update()
    foods.display()
    snake.update()
    snake.display()

def keyPressed():
    if key == CODED:
        if keyCode == UP:
                snake.move(0, -1)
        elif keyCode == DOWN:
                snake.move(0, 1)
        elif keyCode == LEFT:
                snake.move(-1, 0)
        elif keyCode == RIGHT:
                snake.move(1, 0)

class Snake:
    def __init__(self):
        self.__body = []
        self.__body.append(PVector(0, 0))
        self.__direction = PVector(1, 0)
        self.__run = True
    
    def update(self):
        if not self.__run :
            return
        newposx = self.__body[0].x + self.__direction.x
        newposy = self.__body[0].y + self.__direction.y
        if goThroughBorder() :
            newposx = (newposx + (width / cellSize())) % (width / cellSize())
            newposy = (newposy + (height / cellSize())) % (height / cellSize())
        else :
            if newposx < 0 or newposx >= width / cellSize() or newposy < 0 or newposy >= height / cellSize():
                self.__run = False;
                return
        for i in range(len(self.__body) - 1, 0, -1) :
            self.__body[i].x = self.__body[i - 1].x
            self.__body[i].y = self.__body[i - 1].y
        self.__body[0].x = newposx
        self.__body[0].y = newposy
        
    def display(self):
        fill(0)
        stroke(255)
        for v in self.__body:
            rect(v.x * cellSize(), v.y * cellSize(), cellSize(), cellSize())
    def move(self, x, y):
        if len(self.__body)> 1:
            if self.__direction.x * x == -1 : 
                return
            elif self.__direction.y * y == -1:
                return
        self.__direction.x = x
        self.__direction.y = y
    def head(self) :
        return self.__body[0]
    def append(self):
        self.__body.append(PVector(0, 0))
        
        
class Food:
    def __init__(self, count):
        self.__count = count
        self.__pos = []
        for i in range(self.__count):
            self.__pos.append(PVector(-1, 0))
    def update(self):
        for i in range(self.__count):
            if self.__pos[i].x < 0:
                self.__pos[i].x = floor(random(width / cellSize()))
                self.__pos[i].y = floor(random(height / cellSize()))
    def display(self):
        fill(255)
        stroke(0)
        for i in range(self.__count):
            rect(self.__pos[i].x * cellSize(), self.__pos[i].y * cellSize(), cellSize(), cellSize())
    def checkPosHit(self, pos):
        for i in range(self.__count):
            if self.__pos[i].x == pos.x and self.__pos[i].y == pos.y :
                return i
        return -1
    def remove(self, index):
        self.__pos[index].x = -1
