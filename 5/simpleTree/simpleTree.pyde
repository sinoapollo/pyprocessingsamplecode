"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 借鉴自openprocessing.org
             学习重点：函数，递归
"""

def setup():
    size(800, 800) 
    smooth()
    stroke(0,0,0,64)
    strokeCap(ROUND)
    drawTree(width / 2, height / 2)
    noLoop()

def draw():
    pass

def drawTree(x, y):
    pushMatrix()
    pushStyle()
    background(255)
    translate(x, y)
    drawBranch(1)
    popStyle()
    popMatrix()

def drawBranch(level):
    angle = 30
    treeSize = 100
    divisor = 0.8
    maxRandomBranchSize = 0.02
    maxRandomAngle = 30
    maxLevel = 16
    trunk = #000000
    leaves = #000000
    
    if level > maxLevel:
        return
    branchSize = -treeSize * pow(divisor + random(maxRandomBranchSize * 2.) - maxRandomBranchSize, level)
    strokeWeight(0.1 * -(branchSize))
    stroke(lerpColor(trunk,leaves,level/maxLevel))
    line(0,0,0,branchSize)
    translate(0,branchSize)
    thisAngle = angle + random(maxRandomAngle * 2.) - maxRandomAngle
    rotate(radians(-thisAngle))
    drawBranch(level + 1)
    rotate(radians(thisAngle))
    thisAngle = angle + random(maxRandomAngle * 2.) - maxRandomAngle
    rotate(radians(thisAngle))
    drawBranch(level + 1)
    rotate(radians(-thisAngle))
    translate(0,-branchSize)
