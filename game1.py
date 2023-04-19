import pgzrun

b = Rect((50,50), (150,50))
vx , vy = 5,1

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b, 'white')

def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
    if b.bottom > 600 or b.top < 0:
        vy = -vy


pgzrun.go()