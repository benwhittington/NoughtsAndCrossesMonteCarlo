# Ben Whittington
# September 2019

import numpy as np
import random
import copy
from board import Board
from agent import Agent

def run_multiple_games(n):

    won=0
    tie=0
    lost=0

    for _ in range(n):
        
        res=run_game()

        if res==1: won+=1
        elif res==0: tie+=1
        if res==2: lost+=1

    return won,tie,lost

def run_game(b=None):
    if b is None:
        b=Board()
    while not b.end:
        _=b.random_move()

    return b.winner

if __name__=="__main__":
    # currently runs 100 games of the agent against a random player. Takes about a minte

    random.seed(2)

    win=0
    loss=0
    tie=0
    turn=0

    n=10

    for i in range(n):
        game=Board()
        A=Agent(game)
        print("Game {}".format(i))
        while not game.end:
            
            A.make_move()
            game.random_move()
        
        if game.winner=='A': 
            win+=1
            turn+=game.turn

        elif game.winner=='B':
            loss+=1
            
        elif game.winner is None: tie+=1

        del(game)
        del(A)

    print("\nWin: {}".format(win))
    print("Loss: {}".format(loss))
    print("Tie: {}".format(tie))
    print("Avg. Turns to win: {}".format(turn/win))
