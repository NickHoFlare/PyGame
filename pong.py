# Pong!
# by Nicholas Ho

import sys
import pygame


# Initialise constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE	 = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PI = 3.141592653

pygame.init()

# Create Window
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong!")

# Loop until the user clicks the close button.
gameOver = False														

# initialize font/label; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
messageCounter = 0
redCounter = 0
blueCounter = 0
eScoreBool = False
pScoreBool = False
myfont = pygame.font.SysFont("impact", 30)
scoreBoard = myfont.render("SCOREBOARD", 1, BLACK)
redScoreboard = myfont.render("RED", 1, RED)
blueScoreboard = myfont.render("BLUE", 1, BLUE)
enemyScore = myfont.render("ENEMY HAS SCORED!", 1, RED)
playerScore = myfont.render("YOU HAVE SCORED!", 1, BLUE)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialise score booleans
pScored = False
eScored = False

# Initialise positions of game objects
ballX = 165
ballY = 240
enemyXStart = ballX - 15
enemyXEnd   = ballX + 15

# Initialise speed/direction of ball
ballX_change = 0
ballY_change = 3

# Subroutines
def collidePaddle():
    global ballX_change, ballY_change

    ballY_change = ballY_change * -1
    print("Ball X movement is now ",ballX_change)
    if (ballX < paddleMid):
        ballX_change -= 1
        print "Change left"
    else:
        ballX_change += 1
        print "Change right"

def scoreMessage(person):
    global messageCounter, eScoreBool, pScoreBool

    messageCounter = 60
    if (person == "enemy"):
        eScoreBool = True
    elif (person == "player"):
        pScoreBool = True

# ---------- Main Program Loop -----------
while not gameOver:
    # Event Processing
    for event in pygame.event.get(): 									# User did something
        if event.type == pygame.QUIT: 									# If user clicked close
            gameOver = True 											# Flag that we are done so we exit this loop
    
    # Handle mouse movement - get mouse position
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    paddleEnd = mouseX+30
    paddleMid = (mouseX + paddleEnd) / 2
    mouseY = pos[1]
    pygame.mouse.set_visible(False)
    #print("("+str(mouseX)+","+str(mouseY)+")")                         # Prints the coordinates of mouse's current position

    if (mouseX <= 35):													# Handle limits of how far player paddle can go.
    	mouseX = 35
    elif (mouseX >= 275):
    	mouseX = 275
    elif (enemyXStart <= 35):
        enemyXStart = 35
        enemyXEnd = enemyXStart+30
    elif (enemyXStart >= 275):
        enemyXStart = 275
        enemyXEnd = enemyXStart+30

    # Draw the game environment
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [30, 33, 280, 420], 10)				# Game area
    pygame.draw.rect(screen, GREEN, [ballX, ballY, 10, 10])
    pygame.draw.line(screen, BLUE,  [mouseX, 425], [mouseX+30, 425], 5)	# Paddle
    pygame.draw.line(screen, RED,   [enemyXStart, 60], [enemyXEnd, 60], 5)
    redScore = myfont.render(str(redCounter), 1, BLACK)
    blueScore = myfont.render(str(blueCounter), 1, BLACK)
    screen.blit(scoreBoard, (325, 50))
    screen.blit(redScoreboard, (325, 90))
    screen.blit(blueScoreboard, (325, 200))
    screen.blit(redScore, (325, 120))
    screen.blit(blueScore, (325, 230))
    
    ballY += ballY_change
    ballX += ballX_change
    enemyXStart = ballX - 15
    enemyXEnd   = ballX + 15

    if (messageCounter == 0):
        eScoreBool = False
        pScoreBool = False
    elif (eScoreBool):
        messageCounter -= 1
        screen.blit(enemyScore, (60, 250))
    elif (pScoreBool):
        messageCounter -= 1
        screen.blit(playerScore, (60, 250))

    if (ballX >= 297 or ballX <= 35):
    	ballX_change = ballX_change * -1
    elif (ballY >= 440):
        ballY_change = ballY_change * -1
        redCounter += 1
        scoreMessage("enemy")
    elif (ballY <= 38):
        ballY_change = ballY_change * -1
        blueCounter += 1
    	scoreMessage("player")
    elif ((mouseX <= ballX) and (ballX <= paddleEnd) and (ballY == 420)):
    	collidePaddle()
    elif ((enemyXStart <= ballX) and (ballX <= enemyXEnd) and (ballY == 60)):
        collidePaddle()

    # Update the screen with what has been drawn
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


