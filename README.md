# Pygame
# CSF101, CAP2_Pygame

# Overview.
This project is an implementation of the classic Hangman game, built using the Pygame library in Python. The game allows players to guess letters in a word. Each wrong guess adds a part to the hangman's figure, and the game ends when the hangman is fully drawn or the player has correctly guessed the word.

# Dependencies.
The game requires the following Python libraries.

pygame: a set of Python modules designed for writing video games.

math: provides mathematical functions.

random: generates pseudo-random numbers.

pygame.mixer: contains functions for dealing with sound and music.

moviepy.editor: a module for video editing, which provides classes like AudioFileClip and VideoFileClip to work with audio and video files respectively.


# Game Features.
The game includes the following features:

Background Music: The game extracts audio from a video file and plays it as background music. The pygame.mixer module is used to load and play the audio file.

Game Display: The game window is created using pygame.display.set_mode() with a width of 800 pixels and a height of 500 pixels. The window title is set to "Hangman Game".

Buttons: The game uses buttons for the player to guess letters. Each button has the radius of 20 pixels and there is a gap of 15 pixels between each button. The buttons are placed in two rows and centered within the game window.

Fonts: The game uses the Arial font for displaying the title, the letters on the buttons, and the secret word.

Hangman Images: The game loads seven images of the hangman, which are displayed one by one for each wrong guess.

Secret Word: The game randomly selects a secret word from a list of words. The secret word is displayed as a series of underscores, which are replaced by the correct letters as the player guesses them.

Game Loop: The game loop controls the game's main functionality. It checks for events such as mouse clicks and updates the game window accordingly.


# Running the Game.
To run the game, simply execute the main Python script. You can interact with the game using your mouse. Click on the buttons to guess letters. The game ends when you have either guessed the word correctly or made six wrong guesses.

# Conclusion.
This Hangman game showcases how the Pygame library can be used to create a simple yet entertaining game. It demonstrates key Pygame concepts such as game loops, event handling, and drawing on the screen. Enjoy playing Hangman!






# CAP3_TestCase

# Overview
This repository contains the unit tests for the Hangman game implemented using Pygame in Python. The tests aim to ensure the correct functionality of various features of the game such as background music, game display setup, font creation, color constants, button placement, image loading, game setup, button drawing, and win/lose conditions.

# Dependencies
The tests require the following Python libraries.

unittest: Provides a rich set of tools for constructing and running tests.

pygame: A set of Python modules designed for writing video games.

random: Generates pseudo-random numbers.

unittest.mock: Provides tools for mocking objects and methods.



# Test Cases
The test cases cover the following aspects of the Hangman game.

Background Music: Tests if the audio is correctly extracted from a video file and is played as background music.

Game Display Setup: Checks if the game window is correctly set up with the right size and title.

Font Creation: Tests if the fonts are correctly created and their size is greater than zero.

Color Constants: Checks if the color constants are correctly defined.

Button Placement: Tests if the buttons are correctly placed on the game window.

Image Loading: Checks if the images are correctly loaded.

Game Setup: Tests if the game is correctly set up with a random word selected and the hangman status set to 0.

Button Drawing: Checks if the buttons are correctly drawn on the game window.

Win/Lose Conditions: Tests if the win/lose conditions are correctly checked.


# Running the Tests
To run the tests, execute the main Python test script using the following command:

python test_hangman.py

This will run all the test cases and display the results in the console.


# Conclusion
Unit testing is an essential part of software development that ensures the correctness of code. It helps in identifying and fixing bugs early in the development cycle, preventing regressions, and maintaining high code quality.
