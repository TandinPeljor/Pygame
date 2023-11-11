# https://www.youtube.com/watch?v=UEO1B_llDnc
# https://www.youtube.com/watch?v=W6cjx7t39d4&t=11s
# https://www.youtube.com/watch?v=d038LZp_Jhk

import pygame # This line imports the Pygame library which is a set of Python modules designed for writing games
import math # This line imports the math module which provides mathematical functions.
import random
from pygame import mixer # This line imports the mixer module from pygame. The mixer module contains functions for dealing with sound and music
from moviepy.editor import AudioFileClip # This line imports the AudioFileClip class from moviepy.editor. This class can be used to create an audio clip from a sound file or an array


pygame.init()
pygame.mixer.init()

# Adding Background Music
video_file = "OQFQ3750.MP4"  # Video file name 
audio_file = "audio.wav"  # Output audio file name

video = AudioFileClip(video_file) # This line creates an AudioFileClip object from the video file. This object represents the audio of the video
video.write_audiofile(audio_file) #  This line extracts the audio from the video and writes it to an audio file 

pygame.mixer.music.load(audio_file) # This line loads the audio file for playback.
pygame.mixer.music.play(-1) # This line starts playing the audio file. The -1 argument makes the music loop indefinitely.


# Setup display

pygame.init() #This initializes all the modules in Pygame. This function needs to be called before you can use any other Pygame function

WIDTH, HEIGHT = 800, 500 #setting the width (800 pixels) and height (500 pixels) of the game window.
win = pygame.display.set_mode((WIDTH, HEIGHT)) #This function creates the game window with the specified width and height
pygame.display.set_caption("Hangman Game") #This function sets the window title to "Hangman Game" 

# Button Variables
RADIUS = 20 # the radius of each button
GAP = 15 # the gap or distance between each button
letters = [] # an empty list that will be populated with the coordinates of each button
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) 
# (RADIUS * 2 + GAP) * 13 calculates the total width needed for 13 buttons (which is the number of buttons per row), including the gap between each button.
# WIDTH - (RADIUS * 2 + GAP) * 13 calculates the remaining width after placing the buttons. WIDTH is the total available width.
# (WIDTH - (RADIUS * 2 + GAP) * 13) / 2 divides the remaining width by 2 to find the margin on each side (left and right) of the buttons. This is done to center the buttons within the available width.
# round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) rounds the result to the nearest integer to avoid any potential issues with fractional pixels. This final result is the starting x-coordinate for the first button.
starty = 400 # This code sets the starting vertical position, or height, from where the buttons will start being placed.
A = 65 # This sets the ASCII value for the uppercase letter 'A'. This will be used to generate the characters for the buttons.

for i in range(26): # generates the x and y coordinates for each button and appends them to the letters list.
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) # This line calculates the x-coordinate for each button. The calculation takes into account the starting x-coordinate (startx), the gap between each button (GAP * 2), and the position of the button in the row. The expression (RADIUS * 2 + GAP) * (i % 13) calculates the x-coordinate offset for each button within a row. The % operator is used to find the remainder when i is divided by 13, which effectively wraps the button placement after every 13 buttons to create new rows.
    y = starty + ((i // 13) * (GAP + RADIUS * 2)) # This line calculates the y-coordinate for each button. The calculation takes into account the starting y-coordinate (starty) and the row number of the button. The expression (i // 13) * (GAP + RADIUS * 2) calculates the y-coordinate offset for each button, effectively grouping every 13 buttons into a new row. The // operator is used to perform an integer division, which discards the remainder and only keeps the integer part of the division.
    letters.append([x, y, chr(A + i), True]) # Finally, the x and y coordinates for each button are appended as a list to the letters list.

# Fonts
LETTER_FONT = pygame.font.SysFont('arial', 40) # This sets the font and size for the letters on the buttons.
WORD_FONT = pygame.font.SysFont('arial', 50)
TITLE_FONT = pygame.font.SysFont('arial', 70)

# Load Images 
images = [] # Creates an empty list named images
for i in range(7): # Starts a for loop that will iterate 7 times, with i taking on values from 0 to 6.
    image = pygame.image.load("hangman" + str(i) + ".png") # This line uses the pygame.image.load() function to load an image file. The filename is constructed by concatenating the strings "hangman", the string representation of i, and ".png". This means it will load the files "hangman0.png", "hangman1.png", ..., "hangman6.png" in sequence.
    images.append(image) # This line appends the loaded image to the images list. After the loop finishes, images will be a list of seven Pygame Surface objects, each representing one of the loaded images

# Game Variables
hangman_status = 0
words = ["SYNTAX", "PYTHON", "VARIABLE", "COMMIT", "BOOLEAN", "INTEGER", "FLOAT", "STRING", "OUTPUT", "LOOP"]
word = random.choice(words) # used to select a random word from the list words
guessed = [] #  empty list that will be used to keep track of the letters that the player has guessed. As the player guesses letters, they will be added to this list.

# colors
WHITE = (255,255,255) # This creates a tuple representing the color white. Pygame uses RGB values to represent colors, where (255,255,255) corresponds to white
BLUE = (0, 0, 255) # defining a tuple BLUE which represents the color blue in the RGB color model. 

# Setup Game Loop

FPS = 60 # Setting the frames per second (FPS) for the game. This is the number of times the game will update every second.
clock = pygame.time.Clock() # This creates a clock object that you can use to control the game's framerate.
run = True # This is a flag variable used to control the main game loop. As long as this variable is True, the game loop will keep running.

def draw():
    win.fill((WHITE)) #  fills the entire game window with white color.
    
    # Draw Title
    text = TITLE_FONT.render("TP HANGMAN GAME", 1, BLUE) # creates a text surface with the title "TP HANGMAN GAME" using the specified font and color. The render() function is used to create this surface.
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # displays this text surface on the game window
    
    
    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
# The code starts by initializing an empty string display_word. It then iterates over each letter in the secret word. 
# If the letter has been guessed (i.e., it's in the guessed list), it adds the letter to display_word. Otherwise, it adds an underscore (_). This effectively replaces unguessed letters with underscores in the displayed word.
            
    text = WORD_FONT.render(display_word, 1, BLUE)
    win.blit(text, (400, 200))
               
        
    # Draw buttons
    for letter in letters: # this line starts a for loop that iterates over the letters list. Each letter in this list is expected to be a list or tuple that contains two elements, representing the x and y coordinates of a button.
        x, y, ltr, visible = letter # This line unpacks the coordinate pair into x and y variables
        if visible:  # checks if the button is visible. If the button is not visible, the code inside this if statement will be skipped for this button. 
            pygame.draw.circle(win, BLUE, (x, y), RADIUS, 3) # This line uses the pygame.draw.circle() function to draw a circle on the game window
            text = LETTER_FONT.render(ltr, 1, BLUE)
            win.blit(text, (x - text.get_width() / 2,  y - text.get_height() / 2))
   
    win.blit(images[hangman_status], (150, 100)) # draws the current Hangman image onto the window at the position (150, 100)
    pygame.display.update() #  updates the entire screen to display the new content 
    


def display_message(message):
    pygame.time.delay(1000) # This line pauses the execution of the game for 1000 milliseconds (or 1 second). This can be used to give the player a moment to see the message before the game continues.
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLUE) # This line displays the text surface on the game window. The blit() function of the pygame.Surface class is used to do this. The position where the text will be displayed is calculated to center it both horizontally and vertically in the window.
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update() #  This line updates the entire screen to display the new content. This is necessary to actually show the message on the screen.
    pygame.time.delay(3000) # This line pauses the execution of the game for another 3000 milliseconds (or 3 seconds).
    

    

while run:  # This is the main game loop. Everything inside this loop will be executed every frame.
    clock.tick(FPS) # This function makes sure that your game runs at the FPS, specified earlier. It will delay the game to ensure it runs at the correct speed
    

    for event in pygame.event.get(): # This is an event loop. It checks for events such as keyboard presses or mouse movement.
        if event.type == pygame.QUIT: # This checks if the event is a QUIT event, which happens when the user clicks the close button on the game window.
            run = False # If the user clicked the close button, this sets the run variable to False, which will stop the main game loop.
        if event.type == pygame.MOUSEBUTTONDOWN: # This line checks if the event is a MOUSEBUTTONDOWN event, which happens when the user presses a mouse button.
            m_x, m_y = pygame.mouse.get_pos() # If the user has clicked the mouse button, this line gets the current position of the mouse cursor and assigns the x and y coordinates to m_x and m_y.
            for letter in letters:
                x, y, ltr, visible = letter #  This line unpacks the elements of the current letter into x, y, ltr, and visible variables.
                if visible: # This line checks if the button is visible. If the button is not visible, the code inside this if statement will be skipped for this button.
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2 ) # This line calculates the distance between the mouse click and the center of the button. The distance is calculated using the Pythagorean theorem.
                    if dis < RADIUS: # This line checks if the distance between the mouse click and the center of the button is less than the radius of the button. If it is, the button was clicked.
                        letter[3] = False # If the button was clicked, this line sets the visibility of the button to False, which means the button will not be drawn in the next frame
                        guessed.append(ltr) # This line adds the letter on the button to the list of guessed letters.
                        if ltr not in word: #  If the guessed letter is not in the word, this line increments the hangman_status, which keeps track of the current state of the Hangman
                            hangman_status += 1
    
    
    
    draw() # The draw() function call is executing the draw function that was previously defined.

    
    won = True # This line initializes a flag variable won as True. This variable is used to track whether the player has won the game.
    for letter in word: # his line starts a loop that iterates over each letter in the word that the player is trying to guess.
        if letter not in guessed: #  Inside the loop, this line checks if the current letter is in the list of letters that the player has guessed. If it's not, that means the player hasn't guessed this letter yet.
            won = False #  If the player hasn't guessed a letter, this line sets the won flag to False, indicating that the player hasn't won the game yet.
            break # This line immediately exits the loop. Since the won flag is now False, there's no need to check the rest of the letters in the word.
    if won:
        display_message("YOU WON!") # If the player has won, this line displays a "YOU WON!" message on the screen.
        break
    if hangman_status == 6: #  If it's 6, that means the Hangman image is fully drawn, indicating that the player has guessed the word incorrectly 6 times.
        display_message("YOU LOST!") # f the player has lost, this line displays a "YOU LOST!" message on the screen.
        break # This line immediately exits the game loop. Since the player has lost, there's no need to keep the game running

pygame.quit() # This function is called after the main game loop has ended. It will cleanly exit the Pygame library
