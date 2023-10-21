from tkinter import *

score = 0
run = True

while run:
    root = Tk()
    root.geometry('905x700')
    root.title('Hangman')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0