import numpy as np
import copy
import random

class Board:

    def __init__(self):
        self.state=np.array([['-','-', '-'],['-','-', '-'],['-','-', '-']])
        self.empty=self.state[0,0]
        self.player1="A"
        self.player2="B"
        self.player=self.player1 # player 1 starts
        self.free=[(x,y) for y in range(3) for x in range(3)]
        self.winner=None
        self.end=False
        self.turn=0
        self.win_pos = ( # list of lists containing each way to win
            [[(x, y) for y in range(3)] for x in range(3)] +
            [[(x, y) for x in range(3)] for y in range(3)] +
            [[(d, d) for d in range(3)]] + 
            [[(2-d, d) for d in range(3)]]
        )

    def __repr__(self):
        out=""
        for i in range(3):
            for j in range(3):

                out+=str(self.state[i][j])
                if j!=2:
                    out+="  "
                
            out+="\n"

        return out

    def check_win(self):
        # this code is not mine but adapted from:
        # https://codereview.stackexchange.com/questions/24764/tic-tac-toe-victory-check
        # it's genious
        for positions in self.win_pos:
            values = [self.state[x][y] for (x, y) in positions]
            if len(set(values))==1 and (self.empty != values[0]):
                self.winner=values[0]
                self.end=True
                return True

        return False

    def _update_player(self):
        if self.player==self.player1:
            self.player=self.player2
        else:
            self.player=self.player1

    def move(self,move):
        self.free.remove(move)
        self.state[move]=self.player
        self._update_player()
        self.turn+=1

        return self.check_win()

    def random_move(self):
        if len(self.free)==0:
            self.end=True
            return None

        move=random.choice(self.free)
        return self.move(move) 