"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 学习重点：for循环，函数定义，数学基础
"""

def setup() :
    size(500, 500)

def draw() :
    background(0)
    t = abs(sin(frameCount*0.005))
    flower(150*t + 50, 4, t, 5, 100, 68.0, 0.45*t + 0.1, 0.6, PI*(1-t))

def flower(r, c, t, petalCount, circleCount, maxRad, minRad, frac, rot) :
    rad = 0;
    noStroke();

    translate(width/2, height/2);  
    for j in range(petalCount) :
        for i in range(c, circleCount + 1) :
            x  = r * i / circleCount * cos( i * rot / circleCount + (2*PI*j)/petalCount-PI/2)
            y  = r * i / circleCount * sin( i * rot / circleCount + (2*PI*j)/petalCount-PI/2)

            if i < frac * circleCount :
                rad = map(i, 0, frac * circleCount, minRad, maxRad)
            else:
                rad = map(i, frac * circleCount, circleCount, maxRad, minRad)
            fill(lerpColor(color(255*t, 255, 0, 10), color(50*t + 205, 127*(1-t), 0, 100), i * 1.0 / circleCount))
            ellipse(x, y, 2 * rad, 2 * rad)
