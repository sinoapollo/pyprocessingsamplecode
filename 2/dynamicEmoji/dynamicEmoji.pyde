"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 学习重点：curve, bezier, 动画原理
"""

index = 0
step = 200.0
direction = 1

def setup():
    size(800, 600)
    
def draw():
    global index, step, direction
    background(255)
    fill(255, 255, 0)
    ellipse(400, 300, 400, 400)
    noFill()
    #smile
    #curve(230, 400, 280, 250, 380, 240, 430, 400)
    #curve(370, 400, 420, 240, 520, 250, 570, 400)
    #curve(300, 200, 320, 400, 480, 400, 500, 200)

    #cry
    #curve(230, 100, 280, 240, 380, 250, 430, 100)
    #curve(370, 100, 420, 250, 520, 240, 570, 100)
    #curve(300, 600, 320, 400, 480, 400, 500, 600)
    
    #smile to cry
    #x1 = 230
    #y1 = lerp(400, 100, index / step)
    #x2 = 280
    #y2 = lerp(250, 240, index / step)
    #x3 = 380
    #y3 = lerp(240, 250, index / step)
    #x4 = 430
    #y4 = lerp(400, 100, index / step)
    #curve(x1, y1, x2, y2, x3, y3, x4, y4)
    

    x1 = 230
    y1 = lerp(400 * (1 + direction) / 2 + 100 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 100 * (1 + direction) / 2, index / step)
    x2 = 280
    y2 = lerp(250 * (1 + direction) / 2 + 240 * (1 - direction) / 2, 250 * (1 - direction) / 2 + 240 * (1 + direction) / 2, index / step)
    x3 = 380
    y3 = lerp(240 * (1 + direction) / 2 + 250 * (1 - direction) / 2, 240 * (1 - direction) / 2 + 250 * (1 + direction) / 2, index / step)
    x4 = 430
    y4 = lerp(400 * (1 + direction) / 2 + 100 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 100 * (1 + direction) / 2, index / step)
    curve(x1, y1, x2, y2, x3, y3, x4, y4)
    
    x1 = 370
    y1 = lerp(400 * (1 + direction) / 2 + 100 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 100 * (1 + direction) / 2, index / step)
    x2 = 420
    y2 = lerp(240 * (1 + direction) / 2 + 250 * (1 - direction) / 2, 240 * (1 - direction) / 2 + 250 * (1 + direction) / 2, index / step)
    x3 = 520
    y3 = lerp(250 * (1 + direction) / 2 + 240 * (1 - direction) / 2, 250 * (1 - direction) / 2 + 240 * (1 + direction) / 2, index / step)
    x4 = 570
    y4 = lerp(400 * (1 + direction) / 2 + 100 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 100 * (1 + direction) / 2, index / step)
    curve(x1, y1, x2, y2, x3, y3, x4, y4)
    
    x1 = 300
    y1 = lerp(200 * (1 + direction) / 2 + 600 * (1 - direction) / 2, 200 * (1 - direction) / 2 + 600 * (1 + direction) / 2, index / step)
    x2 = 320
    y2 = lerp(400 * (1 + direction) / 2 + 400 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 400 * (1 + direction) / 2, index / step)
    x3 = 480
    y3 = lerp(400 * (1 + direction) / 2 + 400 * (1 - direction) / 2, 400 * (1 - direction) / 2 + 400 * (1 + direction) / 2, index / step)
    x4 = 500
    y4 = lerp(200 * (1 + direction) / 2 + 600 * (1 - direction) / 2, 200 * (1 - direction) / 2 + 600 * (1 + direction) / 2, index / step)
    curve(x1, y1, x2, y2, x3, y3, x4, y4)

                        
    index = (index + 1) % step
    if index == 0 :
        direction *= -1
    
    
