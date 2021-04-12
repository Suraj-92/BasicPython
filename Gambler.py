'''
Author: Suraj N Temkar
Date: 09/04/2021
Title: Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. 
        Keeps track of the number of times he/she wins and the number of bets he/she makes.
'''

import random

def gambler():
    global money
    global goal
    win = 1
    number_of_bets_won = 0
    number_of_bets = 0
    while(money > 0 and money < goal):
        gamble = (random.randint(0, 1))
        if(gamble == win):
            money = money + 1
            number_of_bets_won = number_of_bets_won + 1
        else:
            money = money - 1
        number_of_bets = number_of_bets + 1

    if(money == goal):
        print(f"Gambler reached the goal and has money Rs {money}")
    else:
        print(f"Gambler is broke and has money Rs {money}")

    print(f"Total number of bets played are {number_of_bets}")
    print(f"Number of bets won by gambler are {number_of_bets_won}")
    

if __name__ == '__main__':
    money = int(input("Gambler start with Rs: ")) # 100
    goal = int(input("Enter the goal of Rs: ")) # 200
    gambler()
