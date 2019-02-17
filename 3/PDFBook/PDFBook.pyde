"""
Author: 陈天翼（Apollo Chen）
Date: 20190-2-18
Description: 学习重点：pdf多页导出，文字排版，文件和字符串处理
"""

add_library("pdf")
def setup() :
    fontSize = 500
    wordlist = loadStrings("words.txt")
    words = wordlist[0].split(",")
    pdf = createGraphics(600, 700, "processing.pdf.PGraphicsPDF", "book.pdf")
    tf = pdf.createFont("STKaiti", 48, True, "UTF-8")
    pdf.beginDraw()
    pdf.textFont(tf)
    pdf.stroke(0)
    for i in range(len(words) / 2) :
        pdf.fill(255)
        pdf.rect(0, 0, pdf.width, pdf.height)
        pdf.fill(0)
        pdf.textSize(fontSize / 3)
        textwidth = pdf.textWidth(words[2 * i + 1])
        pdf.text(words[2 * i + 1], (pdf.width - textwidth) / 2, pdf.height / 2 - fontSize / 2.5)
        pdf.textSize(fontSize)
        textwidth = pdf.textWidth(words[2 * i])
        pdf.text(words[2 * i], (pdf.width - textwidth) / 2, pdf.height / 2 + fontSize / 2.1)
        pdf.nextPage()

    pdf.dispose()
    pdf.endDraw()
    noLoop()
    
def draw() :
    pass
