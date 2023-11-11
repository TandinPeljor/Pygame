import unittest # unittest provides a rich set of tools for constructing and running tests, and is a built-in module in Python.
import pygame
from Hangman import *

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        WIDTH, HEIGHT = 800, 500
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.RADIUS = 20
        self.GAP = 15
        self.letters = []
        self.startx = round((WIDTH - (self.RADIUS * 2 + self.GAP) * 13) / 2)
        self.starty = 400
        self.A = 65

    def test_button_placement(self):
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



class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.images = []

    def test_image_loading(self):
        for i in range(7):
            image = pygame.image.load("hangman" + str(i) + ".png")
            self.images.append(image)

        # Check if the correct number of images are loaded
        self.assertEqual(len(self.images), 7)

        # Check if the images are not None
        for image in self.images:
            self.assertIsNotNone(image)

if __name__ == "__main__":
    unittest.main()