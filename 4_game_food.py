player = Actor('chicken')
player.center = 400, 400
food = Actor('pear')
food.center = 700, 500

def draw():
    screen.fill((0, 150, 0))
    player.draw()
    food.draw()

def update():
    checkKeys()
    if player.collidepoint(food.pos):
        food.center = -100, -100

def checkKeys():
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
    if keyboard.up:
        if player.y > 50: player.y -= 5
    if keyboard.down:
        if player.y < 550: player.y += 5

