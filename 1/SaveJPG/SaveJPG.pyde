"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 学习重点：beginShape, vertex, endShape, save, saveFrame
"""

x = 0

def setup():
    size(800, 600)
    triangle(400, 150, 400, 250, 500, 200)
    triangle(250, 250, 300, 300, 300, 250)
    rect(300, 250, 200, 50)
    triangle(550, 250, 500, 300, 500, 250)
    save("t1.jpg");
    
    background(255)
    
    beginShape()
    vertex(400, 150)
    vertex(400, 250)
    vertex(500, 200)
    endShape(CLOSE)
    
    beginShape()
    vertex(250, 250)
    vertex(550, 250)
    vertex(500, 300)
    vertex(300, 300)
    endShape(CLOSE)
    save("t2.jpg")
    
def draw():
    global x
    background(204)
    if x < 100:
        line(x, 0, x, 100)
        x = x + 1
    else:
        noLoop()
    # Saves each frame as line-000001.png, line-000002.png, etc.
    saveFrame("line-######.png")
