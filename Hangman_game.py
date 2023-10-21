from tkinter import *

score = 0
run = True

while run:
    root = Tk()
    root.geometry('905x700')
    root.title('Hangman')
    root.config(bg = '#F0F8FF')
    count = 0
    win_count = 0