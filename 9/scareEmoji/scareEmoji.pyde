# self-scare

l = 6

def setup():
    size(527, 700)
    global img 
    img=loadImage("face.png")
 
def draw():
    background(255) 
    translate(width/2, height/2) 
    emoji(527, 700, 1) 
 
def emoji( w, h, level):
    global l 
    t=map(level, 1, l, 255, 80) 
    tint(t) 

    imageMode(CENTER) 
    image(img, 0, 0, w, h)
     
    if (level<l):
        level+=1
        pushMatrix() 
        translate(0, h/5.5) 
        emoji(w/1.7, h/1.7, level) 
        popMatrix() 
 
