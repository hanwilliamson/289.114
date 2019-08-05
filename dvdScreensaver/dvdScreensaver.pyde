logo = None
x = 0
y = 0
xspeed = 2
yspeed = 2

def setup():
    global logo
    size(800,600)
    logo = loadImage('dvd-logo.png')
    
def draw():
    global x, xspeed, y, yspeed
    background('#000000')
    image(logo, x,y)
    x += xspeed
    y += yspeed
    
    if y == 550:
        yspeed = -2
    elif y == 00:
        yspeed = 2
        
    if x == 700:
        xspeed = -2
    elif x == 0:
        xspeed = 2
    
