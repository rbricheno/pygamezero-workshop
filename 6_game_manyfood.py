import random

player = Actor('chicken')
player.center = 400, 400
food = Actor('pear')

def move_food():
    food.center = (random.randint(60, 740),
                   random.randint(60, 540))

move_food()

def draw():
    screen.fill((0, 150, 0))
    player.draw()
    food.draw()

def update():
    check_keys()
    if player.collidepoint(food.pos):
        move_food()

def check_keys():
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
    if keyboard.up:
        if player.y > 50: player.y -= 5
    if keyboard.down:
        if player.y < 550: player.y += 5

