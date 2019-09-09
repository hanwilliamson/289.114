size(800,800)
background('#E1C699')

mug = 110
col = 1
row = 1

coffees = [
  { 'name':'cafe con leche','espresso':50, 'hotwater':0, 'steamedmilk':30,'foamedmilk':0  },
  { 'name':'espresso',      'espresso':60, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'demi-creme',    'espresso':40, 'hotwater':0, 'steamedmilk':40,'foamedmilk':0  },
  { 'name':'americano',     'espresso':60, 'hotwater':30,'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'capucchino',    'espresso':40, 'hotwater':0, 'steamedmilk':30,'foamedmilk':30 },
  { 'name':'latte',         'espresso':35, 'hotwater':0, 'steamedmilk':10,'foamedmilk':30 },
  { 'name':'ristretto',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'macchiato',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':60 },
  { 'name':'flat white',    'espresso':30, 'hotwater':0, 'steamedmilk':60, 'foamedmilk':0 },
]

for coffee in coffees:
    print(coffee['espresso'])
    
    x = width/4*col
    y = height/4*row
    level = 0

    #espresso
    fill('#352120')
    noStroke()
    rect(x-mug/2, y+mug/2-coffee['espresso']-level,mug,coffee['espresso'])
    level += coffee['espresso']
    
    #water
    fill('#c7e5ff')
    noStroke()
    rect(x-mug/2, y+mug/2-coffee['hotwater']-level,mug,coffee['hotwater'])
    level += coffee['hotwater']
    
    #steamed milk
    fill('#fffcf2')
    noStroke()
    rect(x-mug/2, y+mug/2-coffee['steamedmilk']-level,mug,coffee['steamedmilk'])
    level += coffee['steamedmilk']
    
    #foamed milk
    fill('#e8e5da')
    noStroke()
    rect(x-mug/2, y+mug/2-coffee['foamedmilk']-level,mug,coffee['foamedmilk'])
    level += coffee['foamedmilk']
    
    #mug
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+55,y,40,40, -HALF_PI,HALF_PI)
    arc(x+55,y,65,65, -HALF_PI,HALF_PI)
    rect(x-mug/2, y-mug/2, mug,mug)
    
    #name
    textSize(18)
    textAlign(LEFT)
    fill('#FFFFFF')
    text(coffee['name'], x-mug/2, y+mug/2+30)
    
    if col%3 == 0:
        row += 1
        col = 1
        
    else:
        col += 1

        
    
