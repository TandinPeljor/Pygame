import random
from tkinter import *

score = 0
run = True

#main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('Hangman')
    root.config(bg = '#F0F8FF')
    count = 0
    win_count = 0

#Choosing word
index = random.randit(0,853)
file = open('D:\'Python Glossary')
l = file.readlines()
selected_word = [index].strip('\n')

#Creation of word dash variable
x = 250 
for i in range(0,len(selected_word)):
    x += 60
    exec('d{}=Label(root, text="_",bg="#F0F8FF",font=("arial",40)))'.format(i))
    exec('d{}.place(x={},y={})'.format(i,x,450))
         
#Letters Icon
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for let in al:
    exec('d{}=PhotoImage(file="{}.png")'.format(let,let))

#Hangman Images
