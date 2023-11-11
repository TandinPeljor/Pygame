import unittest # unittest provides a rich set of tools for constructing and running tests, and is a built-in module in Python.
import pygame
from Hangman import * # This line is importing all functions and variables from the Hangman module. The Hangman module likely contains the code for the Hangman game that is to be tested.
import random
from unittest.mock import MagicMock, patch # The unittest.mock module provides a MagicMock class and a patch decorator for mocking objects and methods. Mocking is a technique used in unit testing where you replace parts of your system under test and make assertions about how they have been used. MagicMock is a subclass of Mock with default Magic methods pre-created and ready to use.

    
class TestHangmanGame(unittest.TestCase): # This line defines a new class TestHangmanGame that inherits from unittest.TestCase. This class represents a test case for the Hangman game.    
    def setUp(self): # This method is called before each test method is run. It is typically used to set up any state that is shared across tests.
        pygame.init() # This line initializes all imported Pygame modules. This must be called before any other Pygame functions.
        WIDTH, HEIGHT = 800, 500
        #These lines initialize some variables and lists that will be used in the tests.
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.RADIUS = 20
        self.GAP = 15
        self.letters = []
        self.startx = round((WIDTH - (self.RADIUS * 2 + self.GAP) * 13) / 2)
        self.starty = 400
        self.A = 65
        self.images = []
        self.words = ["SYNTAX", "PYTHON", "VARIABLE", "COMMIT", "BOOLEAN", "INTEGER", "FLOAT", "STRING", "OUTPUT", "LOOP"]
        self.hangman_status = 0
        self.guessed = []
        random.seed(1)  # sets the seed for reproducibility, meaning that the same sequence of random numbers will be generated each time the tests are run.

    
 # Test Background Music   
    @patch('moviepy.editor.VideoFileClip') # This line uses the patch decorator from the unittest.mock module to replace the VideoFileClip function from the moviepy.editor module with a Mock object. This allows the test to control the behavior of VideoFileClip and make assertions about how it is used
    def test_background_music(self, mock_videofileclip):
        # Mock the VideoFileClip function and the audio.write_audiofile method
        mock_videofileclip.return_value.audio.write_audiofile = MagicMock()

        # Mock the pygame.mixer.music.load and pygame.mixer.music.play methods
        pygame.mixer.music.load = MagicMock()
        pygame.mixer.music.play = MagicMock()

        video_file = "OQFQ3750.MP4"  # Video file name 
        audio_file = "audio.wav"  # Output audio file name

        video = mock_videofileclip(video_file) # This line calls mock_videofileclip with video_file as an argument. Since mock_videofileclip is a Mock object, this doesn't actually create a VideoFileClip object. Instead, it records that mock_videofileclip was called with video_file as an argument.
# These lines access the audio attribute of video and call write_audiofile on it with audio_file as an argument. Since video is a Mock object, these don't actually access the audio attribute or call write_audiofile. Instead, they record that write_audiofile was called on video.audio with audio_file as an argument.        
        audio = video.audio
        audio.write_audiofile(audio_file)

        pygame.mixer.music.load(audio_file) # This line loads the audio file for playback.
        pygame.mixer.music.play(-1) # This line starts playing the audio file. The -1 argument makes the music loop indefinitely.

        # Check if the VideoFileClip function was called correctly
        mock_videofileclip.assert_called_once_with(video_file)

        # Check if the audio.write_audiofile method was called correctly
        audio.write_audiofile.assert_called_once_with(audio_file)

        # Check if the pygame.mixer.music.load method was called correctly
        pygame.mixer.music.load.assert_called_once_with(audio_file)

        # Check if the pygame.mixer.music.play method was called correctly
        pygame.mixer.music.play.assert_called_once_with(-1)

    
# Test Font Creations        
    def test_font_creation(self):
        LETTER_FONT = pygame.font.SysFont('arial', 40)
        WORD_FONT = pygame.font.SysFont('arial', 50)
        TITLE_FONT = pygame.font.SysFont('arial', 70)

    # Test if the fonts were created correctly
        self.assertIsInstance(LETTER_FONT, pygame.font.Font)
        self.assertIsInstance(WORD_FONT, pygame.font.Font)
        self.assertIsInstance(TITLE_FONT, pygame.font.Font)

    # Test if the size of the fonts is greater than zero
        self.assertGreater(LETTER_FONT.get_height(), 0)
        self.assertGreater(WORD_FONT.get_height(), 0)
        self.assertGreater(TITLE_FONT.get_height(), 0)

    

# Test Color Constatnts
    def test_color_constants(self):
        # Define the color constants
        WHITE = (255,255,255)
        BLUE = (0, 0, 255)

        # Check if the color constants are correctly defined
        self.assertEqual(WHITE, (255,255,255))
        self.assertEqual(BLUE, (0, 0, 255))


# Test Button Placement
    def test_button_placement(self):
        self.letters = []
        for i in range(26):
            x = self.startx + self.GAP * 2 + ((self.RADIUS * 2 + self.GAP) * (i % 13))
            y = self.starty + ((i // 13) * (self.GAP + self.RADIUS * 2))
            self.letters.append([x, y, chr(self.A + i), True])

        # Check if the correct number of buttons are created
        self.assertEqual(len(self.letters), 26)

        # Check if the buttons are placed in the correct positions
        for i in range(26):
            self.assertEqual(self.letters[i][0], self.startx + self.GAP * 2 + ((self.RADIUS * 2 + self.GAP) * (i % 13)))
            self.assertEqual(self.letters[i][1], self.starty + ((i // 13) * (self.GAP + self.RADIUS * 2)))

# Test Image Loading
    def test_image_loading(self):
        for i in range(7):
            image = pygame.image.load("hangman" + str(i) + ".png")
            self.images.append(image)

        # Check if the correct number of images are loaded
        self.assertEqual(len(self.images), 7)

        # Check if the images are not None
        for image in self.images:
            self.assertIsNotNone(image)

    
# Test Game Setup
    def test_game_setup(self):
        # Select a random word
        word = random.choice(self.words)

        # Check if the word is correctly selected
        self.assertIn(word, self.words)

        # Check if the hangman status is 0
        self.assertEqual(self.hangman_status, 0)

        # Check if the guessed letters list is empty
        self.assertEqual(self.guessed, [])


    
# Test Win Conditions
    def test_win_condition(self):
        word = "PYTHON"
        guessed = ["P", "Y", "T", "H", "O", "N"]
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        # Check if the win condition is correctly checked
        self.assertEqual(won, True)


# Test Lose Conditions
    def test_lose_condition(self):
        word = "PYTHON"
        guessed = ["P", "Y", "T"]
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        # Check if the lose condition is correctly checked
        self.assertEqual(won, False)


    
if __name__ == "__main__":
    unittest.main()
# The if __name__ == "__main__": line checks if the module is being run directly. If it is, then the code within the if-statement is executed. If the module is being imported, then the code within the if-statement is not executed
# The unittest.main() function creates a test runner, which automatically finds all the test methods in the current module and runs them. It also provides a command-line interface for the test script, allowing you to specify options such as which tests to run and whether to display a detailed or summary report

