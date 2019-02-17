"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 学习重点：bezier
"""

def setup():
    size(800, 800)
    
def draw():
    background(0)
    fill(255, 255, 0, 150)
    noStroke()
    bezier(400, 400, 250, 200, 550, 200, 400, 400)
    bezier(400, 400, 650, 450, 450, 650, 400, 400)
    bezier(400, 400, 150, 450, 350, 650, 400, 400)
    noFill()
    stroke(255, 255, 0, 150)
    strokeWeight(3)
    bezier(400, 400, 400, 450, 420, 600, 450, 800)

    
