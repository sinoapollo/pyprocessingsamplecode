"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 学习重点：重复规则图形计算
"""

def setup():
    size(800, 600)
    smooth()
    
def draw():
    background(255)
    drawMultiBezier(50, 8)
    
#多边形
def drawMultiAngle(r, n):
    angle = TWO_PI / n;
    pushMatrix()
    translate(width / 2, height / 2)
    rotate(-PI / 2)
    y1 = r * sin(angle / 2)
    x1 = r * cos(angle / 2)
    y2 = -y1
    x2 = x1
    for i in range(n) :
        pushMatrix()
        rotate(i * angle)
        line(x1, y1, x2, y2)
        popMatrix()
    popMatrix()
   
#多角形
def drawMultiInnerAngle(r, n):
    angle = TWO_PI / n;
    pushMatrix()
    translate(width / 2, height / 2)
    rotate(-PI / 2)
    y1 = r * sin(angle)
    x1 = r * cos(angle)
    y2 = -y1
    x2 = x1
    for i in range(n) :
        pushMatrix()
        rotate(i * angle)
        line(x1, y1, x2, y2)
        popMatrix()
    popMatrix()
    
#多曲线
def drawMultiCurve(r, n):
    angle = TWO_PI / n;
    pushMatrix()
    translate(width / 2, height / 2)
    rotate(-PI / 2)
    y1 = r * sin(angle) # angle / 2
    x1 = r * cos(angle) # angle / 2
    y2 = -y1
    x2 = x1
    for i in range(n) :
        pushMatrix()
        rotate(i * angle)
        #curve(x1, y2, x1, y1, x2, y2, x2, y1) #画出多边形
        #curve(0, 0, x1, y1, x2, y2, 0, 0) #电视机屏
        #curve(x2, y1, x1, y1, x2, y2, x1, y2) #多角形
        popMatrix()
    popMatrix()
    

#多贝塞尔曲线
def drawMultiBezier(r, n):
    angle = TWO_PI / n;
    pushMatrix()
    translate(width / 2, height / 2)
    rotate(-PI / 2)
    y1 = r * sin(angle / 2)
    x1 = r * cos(angle / 2)
    y2 = -y1
    x2 = x1
    for i in range(n) :
        pushMatrix()
        rotate(i * angle)
        bezier(x1, y1, n * x1, n * y1, n * x2, n * y2, x2, y2)
        popMatrix()
    popMatrix()
        
