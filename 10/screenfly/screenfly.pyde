"""
Author: 陈天翼（Apollo Chen）
Date: 2019-02-18
Description: 学习重点：随机函数，字符串函数，汉字处理，字体函数，列表
"""

lines = []

def setup() :
    global lines, img
    size(1024, 576)
    strings = [u"2019 新年快乐！", u"Happy New Year!", u"不用熬夜，心想事成。", u"多写程序，万事如意:-)", u"学业有成，找到朋友:-P", u"玩个痛快，老师再见:-("]
    #lines = new ArrayList<Line>(strings.length);
    textSize = height / 3 / len(strings)
    textFont(createFont("Heiti", textSize))
  
    img = loadImage("happynewyear.jpg")
  
    for i in range(len(strings) - 1, -1, -1) :
        lines.insert(0, Line((i + 1) * textSize, strings[i]));

def draw() :
    global img, lines
    image(img, 0, 0, width, height)
    for item in lines :
        item.update()
        item.draw()

class Line :
    def __init__(self, lineY, lineString) :
        self.__lineY = lineY
        self.__lineString = lineString
        self.__lineX = width
        self.__textWidth = textWidth(self.__lineString)
        self.randomSpeed()

    def update(self) :
        self.__lineX -= self.__speed;
        if self.__lineX + self.__textWidth < 0 :
            self.randomSpeed()
            self.__lineX = width

    def draw(self) :
        text(self.__lineString, self.__lineX, self.__lineY)

    def randomSpeed(self) :
        self.__speed = random(2, 5)
