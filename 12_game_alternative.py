import random

player = Actor('shark')
player.center = 400, 400
food = Actor('fish')
treat = Actor('puffer')
score = 0
playing = True

def move_food():
    food.center = (random.randint(60, 740),random.randint(60, 540))

def move_treat():
    treat.center = (random.randint(60, 740),random.randint(60, 540))

def hide_treat():
    treat.center = (-100, -100)

move_food()
hide_treat()

def draw():
    screen.blit('sea', (0, 0))
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
        checkKeys()
        if player.collidepoint(food.pos):
            score = score + 5
            sounds.crunch.play()
            move_food()
        if player.collidepoint(treat.pos):
            score = score + 10
            sounds.munch.play()
            hide_treat()

def checkKeys():
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
music.set_volume(0.2)
music.play("backing")

