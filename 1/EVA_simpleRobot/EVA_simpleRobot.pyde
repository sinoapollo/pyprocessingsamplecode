"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 借鉴自OpenProcessing.org
             学习重点：size, background, fill, stroke, noStroke, strokeWeight, ellipse, arc, line, random
"""

def setup() :
    size(800, 800)

def draw() :
    background(0)
    noStroke()
    fill(57)
    ellipse(480, 780, 140, 40)
    fill(50)
    ellipse(480, 780, 120, 30)
    stroke(220)
  
    #RIGHT ARM(BEHIND BODY)
    strokeWeight(1)
    fill(240)
    ellipse(530, 540, 60, 300)
  
    #BODY
    fill(255)
    arc(480, 350, 300, 800, 0, PI)
    fill(210)
    ellipse(480, 350, 300, 40)
    fill(190)
    ellipse(480, 350, 270, 40)
    fill(255)

    #LEFT ARM
    strokeWeight(1)
    fill(240)
    ellipse(293, 540, 60, 250)
    fill(255)
    ellipse(280, 540, 70, 320)
    
    #HEAD
    fill(255)
    ellipse(480, 200, 380, 280)
    fill(40)
    ellipse(480, 220, 300, 190)
    stroke(0, 159, 255)
    strokeWeight(45)
    line(random(340,342), random(220, 222), 370  ,223)
    line(random(478,480), random(220, 222), 450 ,223)
    stroke(0)
    
    
    strokeWeight(1)
