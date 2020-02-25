import random

player = Actor('chicken')
player.center = 400, 400
food = Actor('pear')
treat = Actor('pineapple')
score = 0
playing = True

def move_food():
    food.center = (random.randint(60, 740),random.randint(60, 540))

def move_treat():
    treat.center = (random.randint(60, 740),random.randint(60, 540))

def hide_treat():
    treat.center = -100, -100

move_food()
hide_treat()

def draw():
    screen.fill((0, 150, 0))
    if playing:
        player.draw()
        food.draw()
        treat.draw()
        screen.draw.text("Score: " + str(score), (20, 20))
    else:
        screen.draw.text("Time up! You scored " + str(score), center=(400, 500), fontsize=60)

def update():
    global score
    if playing:
        check_keys()
        if player.collidepoint(food.pos):
            score = score + 5
            move_food()
        if player.collidepoint(treat.pos):
            score = score + 10
            hide_treat()

def check_keys():
    global player
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
    if keyboard.up:
        if player.y > 50: player.y -= 5
    if keyboard.down:
        if player.y < 550: player.y += 5

def game_over():
    global playing
    playing = False

clock.schedule_interval(move_treat, 3)
clock.schedule(game_over, 20)

