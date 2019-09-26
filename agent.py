from board import Board
import copy
import numpy as np

class Agent(Board):
    def __init__(self,b):
        self.b=b
        self.n=12 # number of random games to run

    def make_move(self):
        # get each possible move
        moves=self.b.free
        scores=np.zeros(len(moves))
        for i,move in enumerate(moves):
            scores[i]=self.test_move(move)

        i=np.argmax(scores)
        self.b.move(moves[i])

    def test_move(self,move):
        b_copy=copy.deepcopy(self.b)
        _=b_copy.move(move)
        win,tie,_=self.run_multiple_games_state(b_copy)

        return (win+0.1*tie)/self.n

    def run_multiple_games_state(self,board):

        w=0
        t=0
        l=0
        # print(board)s
        for _ in range(self.n):
            board_copy=copy.deepcopy(board)
            res=self.run_game(board_copy)

            if res==board_copy.player1: w+=1
            elif res is None: t+=1
            if res==board_copy.player2: l+=1

            del(board_copy)
        # print(won)
        return w,t,l

    def run_game(self,b=None):
        if b is None:
            b=Board()
        while not b.end:
            _=b.random_move()

        return b.winner