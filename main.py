import random
from argparse import Action
from enum import IntEnum


class Action(IntEnum):
    rock=0
    paper=1
    scissors=2


def players_choice():
    player_input=input("please enter 1 for rock, 2 for scissors and 3 for ")
    attack=int(player_input)
    action=Action(attack)
    return action


def computers_choice():

    defense=random.randint(0, len(Action)-1)
    action=Action(defense)
    return action


def choosing_the_winner(user_action,computer_action):
    if user_action == computer_action:
        print("it's a tie")
    elif user_action == Action.rock:
        if computer_action == Action.scissors:
            print("YOU WON THE GAME")
        else:
                print("YOU WON THE GAME")
    elif user_action == Action.paper:
                if computer_action == Action.scissors:
                    print("COMPUTER WON THE GAME")
                else:
                    print("YOU WON THE GAME")
    elif user_action == Action.scissors:
        if computer_action == Action.paper:
            print("COMPUTER WON THE GAME")
        else:
            print("YOU WON THE GAME")


while True:

    user_action=players_choice()
    computer_action=computers_choice()
    choosing_the_winner(user_action, computer_action)
    play=input("do you want to play again? type y")
    play_again= str(play)
    if play_again.lower() != "y":
        break

















