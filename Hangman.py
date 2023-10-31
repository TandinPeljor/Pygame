import pygame #This line imports the Pygame library which is a set of Python modules designed for writing games

# Setup display

pygame.init() #This initializes all the modules in Pygame. This function needs to be called before you can use any other Pygame function

WIDTH, HEIGHT = 800, 500 #setting the width (800 pixels) and height (500 pixels) of the game window.
win = pygame.display.set_mode((WIDTH, HEIGHT)) #This function creates the game window with the specified width and height
pygame.display.set_caption("Hangman Game") #This function sets the window title to "Hangman Game" 

# Button Variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) 
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y])


# Load Images 
images = [] # Creates an empty list named images
for i in range(7): # Starts a for loop that will iterate 7 times, with i taking on values from 0 to 6.
    image = pygame.image.load("hangman" + str(i) + ".png") # This line uses the pygame.image.load() function to load an image file. The filename is constructed by concatenating the strings "hangman", the string representation of i, and ".png". This means it will load the files "hangman0.png", "hangman1.png", ..., "hangman6.png" in sequence.
    images.append(image) # This line appends the loaded image to the images list. After the loop finishes, images will be a list of seven Pygame Surface objects, each representing one of the loaded images

# Game Variables
hangman_status = 6

# colors
WHITE = (255,255,255) # This creates a tuple representing the color white. Pygame uses RGB values to represent colors, where (255,255,255) corresponds to white
BLUE = (0, 0, 255)

# Setup Game Loop

FPS = 60 # Setting the frames per second (FPS) for the game. This is the number of times the game will update every second.
clock = pygame.time.Clock() # This creates a clock object that you can use to control the game's framerate.
run = True # This is a flag variable used to control the main game loop. As long as this variable is True, the game loop will keep running.

def draw():
    win.fill((WHITE)) #  fills the entire game window with white color.
    
    # Draw buttons
    for letter in letters:
        x, y = letter
        pygame.draw.circle(win, BLUE, (x, y), RADIUS, 3) 
    
    win.blit(images[hangman_status], (150, 100)) # draws the current Hangman image onto the window at the position (150, 100)
    pygame.display.update() #  updates the entire screen to display the new content 
    


while run:  # This is the main game loop. Everything inside this loop will be executed every frame.
    clock.tick(FPS) # This function makes sure that your game runs at the FPS, specified earlier. It will delay the game to ensure it runs at the correct speed
    
    draw()

    for event in pygame.event.get(): # This is an event loop. It checks for events such as keyboard presses or mouse movement.
        if event.type == pygame.QUIT: # This checks if the event is a QUIT event, which happens when the user clicks the close button on the game window.
            run = False # If the user clicked the close button, this sets the run variable to False, which will stop the main game loop.
            
pygame.quit() # This function is called after the main game loop has ended. It will cleanly exit the Pygame library

