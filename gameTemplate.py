# First non-Uni Python program
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
pygame.display.set_caption("Wololo")

# Loop until the user clicks the close button.
gameOver = False
gameStart = True														# Game has just started. Ball starts moving down.
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialise positions of game objects
ballX = 165
ballY = 240

# Initialise speed/direction of ball
ballX_change = 0
ballY_change = 3
 
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

    if (mouseX <= 35):													# Handle limits of how far player paddle can go.
    	mouseX = 35
    elif (mouseX >= 275):
    	mouseX = 275

    # Draw the game environment
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [30, 33, 280, 420], 10)				# Game area
    pygame.draw.rect(screen, GREEN, [ballX, ballY, 10, 10])
    pygame.draw.line(screen, BLUE,  [mouseX, 425], [mouseX+30, 425], 5)	# Paddle
    
    if gameStart:
    	ballY += ballY_change
    	ballX += ballX_change

    if (ballX >= 297 or ballX <= 35):
    	ballX_change = ballX_change * -1
    elif (ballY >= 440 or ballY <= 38):
    	ballY_change = ballY_change * -1
    elif ((mouseX <= ballX) and (ballX <= paddleEnd) and (ballY == 420)):
    	ballY_change = ballY_change * -1
    	print("Ball X movement is now ",ballX_change)
    	if (ballX < paddleMid):
    		ballX_change -= 1
    		print "Change left"
    	else:
    		ballX_change += 1
    		print "Change right"

    # Update the screen with what has been drawn
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()