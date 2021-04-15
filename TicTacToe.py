'''
Author: Suraj N Temkar
Date: 14/04/2021
Title: -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. 
            Player 1 is the Computer and the Player 2 is the user. Player 1 take Random Cell that is the Column and Row. 
'''

import random

boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
Human = 'X'
Computer = 'O'
first_player = Human
turn = 1
winning_turns = [ [0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6] ]

def print_board(initial=False):
    print(('''
                {} | {} | {}
               -----------
                {} | {} | {}
               -----------
                {} | {} | {}
        ''').format(*([x for x in range(1, 10)] if initial else boxes)))

def take_turn(player, turn):
    while True:
        if player is Computer:
            box = Computer_move()
        else:
            box = input(f'Player {player}, type a number from 1-9 to select a box {player} : ')

            try:
                box = int(box) - 1
            except ValueError:
                print("Enter Valid Number....")
                continue

        if box < 0 or box > 8:
            print("Number is Out Of Range, Please Enter Valid Number")
            continue
        if boxes[box] == ' ':
            boxes[box] = player
            break
        else:
            print("Already Taken Please Enter Another Number...")


def Computer_move():
    return random.randint(0, 8)

def check_win(player, turn):
    if turn > 4:
        for turns in winning_turns:
            score = 0
            for index in turns:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'
        if turn == 9:
            return 'tie'

def switch_player(turn):
    current_player = Computer if turn % 2 == 0 else Human
    return current_player

def play(player, turn):
    while True:
        take_turn(player, turn)
        print_board()
        result = check_win(player, turn)
        if result == 'win':
            print(f"Game Over...{result} win.....\n {player}")
            break
        elif result == 'tie':
            print(f"Game Over... Its Tie...\n")
            break
        turn += 1
        player = switch_player(turn)

# Start The Game (Main Function)
if __name__ == '__main__':
    print("\n Welcome To The Tic Tac Toe.....")
    print_board(initial=True)
    play(first_player, turn)
