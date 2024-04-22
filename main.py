import random
from argparse import Action
from enum import IntEnum
from tkinter import *
import tkinter as tk



class Action(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def players_choice(user_choice):
    attack = int(user_choice)
    action = Action(attack)
    return action

def computers_choice():
    defense = random.randint(0, len(Action)-1)
    action = Action(defense)
    return action

def choosing_the_winner(user_action, computer_action):
    if user_action == computer_action:
        result_label.config(text="It's a tie",font='arial 20 bold')
    elif user_action == Action.ROCK:
        if computer_action == Action.SCISSORS:
            result_label.config(text="YOU WON THE GAME",font='arial 20 bold',fg="#445919")
        else:
            result_label.config(text="COMPUTER WON THE GAME",font='arial 20 bold',fg="red")
    elif user_action == Action.PAPER:
        if computer_action == Action.SCISSORS:
            result_label.config(text="COMPUTER WON THE GAME",font='arial 20 bold',fg="red")
        else:
            result_label.config(text="YOU WON THE GAME",font='arial 20 bold',fg="#445919")
    elif user_action == Action.SCISSORS:
        if computer_action == Action.PAPER:
            result_label.config(text="COMPUTER WON THE GAME",font='arial 20 bold',fg="red")
        else:
            result_label.config(text="YOU WON THE GAME",font='arial 20 bold',fg="#445919")


def play():
    user_action = players_choice(choice_var.get())
    computer_action = computers_choice()
    choosing_the_winner(user_action, computer_action)

root=Tk()
root.geometry("900x500")
root.configure(bg="#FFFFFF")
root.title("Rock Paper Scissors")

choice_var = tk.StringVar()

rockimg=PhotoImage(file="images/rock.png")
rock_btn = tk.Radiobutton(root, image=rockimg, variable=choice_var, value="0")
rock_btn.place(x=0,y=50)

paperimg=PhotoImage(file="images/paper.png")
paper_btn = tk.Radiobutton(root, image=paperimg,text="Paper", variable=choice_var, value="1")
paper_btn.place(x=300,y=50)

scissorsimg=PhotoImage(file="images/scissors.png")
scissors_btn = tk.Radiobutton(root,image=scissorsimg, text="Scissors", variable=choice_var, value="2")
scissors_btn.place(x=600,y=50)

playimg=PhotoImage(file="images/play.png")
play_btn = tk.Button(root, image=playimg,text="Play", command=play,bd=0)
play_btn.place(x=350,y=300)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

















