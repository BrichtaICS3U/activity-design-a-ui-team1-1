# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame

pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (177, 227, 102)
BRIGHT_GREEN = (205, 237, 157)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BRIGHT_Blue = (135,212,223)
Blue = (67,188,205)

# Open a new window
 # The window is defined as (width, height), measured in pixels
SCREENWIDTH = 800
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Button")

# --- Text elements

# Define text for title of game
fontTitle = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400,100)   # place the centre of the text

fontTitleGreen = pygame.font.Font('freesansbold.ttf', 8)
textSurfaceTitleGreen = fontTitle.render('PLAY!', True, BLACK) 
textRectTitleGreen = textSurfaceTitleGreen.get_rect()
textRectTitleGreen.center = (400, 175)

fontTitleRed = pygame.font.Font('freesansbold.ttf', 8)
textSurfaceTitleRed = fontTitle.render('SETTINGS!', True, BLACK) 
textRectTitleRed = textSurfaceTitleRed.get_rect()
textRectTitleRed.center = (400, 325)

fontTitleBLue = pygame.font.Font('freesansbold.ttf', 5)
textSurfaceTitleBLue = fontTitle.render('QUIT!', True, BLACK) 
textRectTitleBLue = textSurfaceTitleBLue.get_rect()
textRectTitleBLue.center = (400, 480)




def my_next_function():
    global level
    level += 1
    
# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print(click) # Uncomment to see mouse buttons clicked in shell
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue shapes to be drawn
    
    # Buttons

    # RED button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT/4 < mouse[1] < SCREENHEIGHT/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, RED, (SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))
        print('You pressed the button! You maniac!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT/4 < mouse[1] < SCREENHEIGHT/4 + 50:
        pygame.draw.rect(screen, BRIGHT_RED, (SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))
    else:
        pygame.draw.rect(screen, RED,(SCREENWIDTH/2-50, SCREENHEIGHT/4, 100, 50))

    # GREEN button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*2/4 < mouse[1] < SCREENHEIGHT*2/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, GREEN, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
        print('You have quit the Game!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*2/4 < mouse[1] < SCREENHEIGHT*2/4 + 50:
        pygame.draw.rect(screen, BRIGHT_GREEN, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
    else:
        pygame.draw.rect(screen, GREEN, (SCREENWIDTH/2-50, SCREENHEIGHT*2/4, 100, 50))
        
    # Blue button
    if SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*3/4 < mouse[1] < SCREENHEIGHT*3/4 + 50 and click[0] == 1:
        pygame.draw.rect(screen, Blue, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))
        print('You have paused the game!')
    elif SCREENWIDTH/2-50 < mouse[0] < SCREENWIDTH/2+50 and SCREENHEIGHT*3/4 < mouse[1] < SCREENHEIGHT*3/4 + 50:
        pygame.draw.rect(screen, BRIGHT_Blue, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))
    else:
        pygame.draw.rect(screen, Blue, (SCREENWIDTH/2-50, SCREENHEIGHT*3/4, 100, 50))

    # Text
    screen.blit(textSurfaceTitleGreen, textRectTitleGreen)
    screen.blit(textSurfaceTitleRed, textRectTitleRed)
    screen.blit(textSurfaceTitleBLue, textRectTitleBLue)
    screen.blit(textSurfaceTitle, textRectTitle)

    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
