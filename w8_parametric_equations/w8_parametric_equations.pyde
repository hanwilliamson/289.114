def setup():
    size(800,800)
    background('#004477')
    strokeWeight(3)
    
def parabola():
    return x*x
    
x = -300.0
y = 0.0
t = 0.0
    
def draw():
    translate(width/2,height/2)
    stroke('#0099ff')
    line(width/2*-1,0,width/2,0)
    line(0,height/2*-1,0,width/2)
    text('i want to go home', 30,-40)
    
