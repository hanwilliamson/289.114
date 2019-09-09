def setup():
    size(600,600)
    background('#004477')
    wendy = createFont('wendy.ttf', 20)
    textFont(wendy)
    noLoop()
    noStroke()
    
rainbow = [
    '#ff0000', '#ff9900', '#ffff00', '#00ff00', '#0099ff', '#6633ff'
    ]

brushColor = rainbow[0]
brushShape = ROUND
brushSize = 3
painting = False
paintMode = 'free'

def mousePressed():
    if mouseButton == LEFT:
        loop()

def mouseReleased():
    noLoop()
    global painting
    painting = False
    
def draw():
    global painting, paintMode
    print(frameCount)
    
    if paintMode == 'free':
        if not painting and frameCount > 1:
            line(mouseX,mouseY,pmouseX,pmouseY)
            painting = True
        elif painting:
            stroke(brushColor)
            strokeCap(brushShape)
            strokeWeight(brushSize)
            line(mouseX,mouseY,pmouseX,pmouseY)
    
    
