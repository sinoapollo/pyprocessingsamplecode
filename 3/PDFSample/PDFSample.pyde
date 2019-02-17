"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 学习重点：pdf的不同导出方法
"""

add_library('pdf')


def setup():
    lines = loadStrings("list.txt")
    for line in lines:
        for c in line:
            println(c)

    size(600, 600)
    #输出PDF
    #beginRecord("processing.pdf.PGraphicsPDF", "line.pdf")
    
    #background(255)
    #stroke(0, 20)
    #strokeWeight(20.0)
    #line(200, 0, 400, height)
    #endRecord()
    
    pdf = createGraphics(300, 300, "processing.pdf.PGraphicsPDF", "line.pdf")
    pdf.beginDraw()
    pdf.line(50, 50, 250, 250)
    pdf.nextPage()
    pdf.dispose()
    pdf.endDraw()
    
    #输出中文
    # Uncomment the following two lines to see the available fonts 
    #fontList = PFont.list()
    #print(fontList)
    myFont = createFont("STKaiti", 18, True)
    #myFont = loadFont("STSong-48.vlw")
    textFont(myFont, 48)
    textAlign(CENTER, CENTER)
    fill(0, 0, 0)
    #python中使用中文字符串，引号前要加u
    text(u"中", width/2, height/2)
    
    #保存PDF
