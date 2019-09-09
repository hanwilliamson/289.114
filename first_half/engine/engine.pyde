theta = 0
radius = 1


def setup():
    size(1000,500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    
def draw():
    global theta
    background('#004477')
    diameter = 50
    translate(750, 300)
    ellipse(0,0, diameter, diameter)
    x = cos(theta)
    y = sin(theta)
    line(0,0, x*diameter/2,y*diameter/2)
    
    line(x*diameter/2,y*diameter/2, 0,(y*diameter/2)-70)
    
    rect(-18,(y*diameter/2)-60,36,-35)
    line(-18,(y*diameter/2)-84,18,(y*diameter/2)-84)
    line(-18,(y*diameter/2)-89,18,(y*diameter/2)-89)
    
    translate(-420,0)
    y = sin(theta+3)
    line(0,(y*diameter/2), 0,(y*diameter/2)-70)
    rect(-18,(y*diameter/2)-60,36,-35)
    line(-18,(y*diameter/2)-84,18,(y*diameter/2)-84)
    line(-18,(y*diameter/2)-89,18,(y*diameter/2)-89)
    
    translate(-60,0)
    y = sin(theta+2)
    line(0,(y*diameter/2), 0,(y*diameter/2)-70)
    rect(-18,(y*diameter/2)-60,36,-35)
    line(-18,(y*diameter/2)-84,18,(y*diameter/2)-84)
    line(-18,(y*diameter/2)-89,18,(y*diameter/2)-89)
    
    translate(-60,0)
    y = sin(theta+1)
    line(0,(y*diameter/2), 0,(y*diameter/2)-70)
    rect(-18,(y*diameter/2)-60,36,-35)
    line(-18,(y*diameter/2)-84,18,(y*diameter/2)-84)
    line(-18,(y*diameter/2)-89,18,(y*diameter/2)-89)
    theta += 0.1
