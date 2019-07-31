import numpy

class tic_tac_toe(object):

    #0 = empty
    #-1 = O
    #1 = X
    history = [] #board history
    action = [] #action history (in terms of pos)
    historyX = [] #board history for player X
    actionX = [] #action history (in terms of pos) for player X
    historyO = [] #board history for player O
    actionO = [] #action history (in terms of pos) for player O
    
    
    def __init__(self):
        self.board = [0 for i in range(9)] #actual game board
        self.rboard = [' ' for i in range(9)]
        self.eboard = [i for i in range(9)] #empty board to show index
        self.winner = 0 #1 = player 1, -1 = player 2, 0.5 = draw

    def update(self,mark,pos):
        if mark == 1:
            self.rboard[pos] = 'X'
            self.historyX.append(self.board.copy())
            self.actionX.append(pos)
        elif mark == -1:
            self.rboard[pos] = 'O'
            self.historyO.append(self.board.copy())
            self.actionO.append(pos)

        #store move history
        self.history.append(self.board.copy())
        self.action.append(pos)
        
        self.board[pos] = mark

    def iswinner(self):
        #check any horizontal
        for i in range(3):
            z = sum(self.board[0+3*i:3+3*i])
            if z == 3:
                #print('player X won')
                self.winner = 1
                return None
            elif z == -3:
                #print('player O won')
                self.winner = -1
                return None
                
        #check any vertical
        for i in range(3):
            z = 0
            for j in range(3):
                z += self.board[i+j*3]
            if z == 3:
                #print('player X won')
                self.winner = 1
                return None
            elif z == -3:
                #print('player O won')
                self.winner = -1
                return None

        #check diagonals
        md = self.board[0]+self.board[4]+self.board[8]
        ad = self.board[2]+self.board[4]+self.board[6]
        if md == 3 or ad == 3:
            #print('player X won')
            self.winner = 1
            return None
        elif md == -3 or ad == -3:
            #print('player O won')
            self.winner = -1
            return None
            
        #draw condition
        if numpy.prod(self.board) != 0:
            self.winner = 0.5
            return None

    def printboard(self):
        for i in range(3):
            print(self.rboard[0+3*i:3+3*i])

    def printboardindex(self):
        for i in range(3):
            print(self.eboard[0+3*i:3+3*i])
