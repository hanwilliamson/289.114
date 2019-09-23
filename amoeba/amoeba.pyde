def setup():
    size(800,800)
    
class Amoeba:
    
    def __init__(self,x,y):
        self.location = PVector(x,y)
        self.velocity = PVector(xspeed,yspeed)
        self.diameter = float(diameter)
    
    def update(self):
        fill(0x880099ff)
        stroke('#FFFFFF')
        strokeWeight(3)
        self.location += self.velocity
        ellipse(self.location.x,self.location.y,self.diameter.x,self.diamter.y)
    
a = Amoeba(300,200,0.3,0.3,150)
b = Amoeba(100,100,-0.3,0.5,80)

def draw():
    background('#004477')
    
