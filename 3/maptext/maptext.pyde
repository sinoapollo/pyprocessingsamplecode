"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-22
Description: 学习重点：字符，map函数, 内置变量mouseX, mouseY
"""

def setup() :
    size(800, 800)
    stroke(0)
    fill(0)
    
def draw() :
    background(255)
    textSize(map(mouseY, height, 0, 12, 120))
    text("A",map(mouseX, width, 0, 0, width), height / 2)
