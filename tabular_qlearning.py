import numpy
import pickle
import os.path

class tabular_qlearning(object):

    initial_qval = 0.6
    win_reward = 1
    draw_reward = 0.5
    loss_reward = 0
    alpha = 0.9 #learning rate
    gamma = 0.95 #discount rate
    player = 0 #set to 1 if X and -1 if O
    qtable_filename = "qtable.p"
    qtable = dict()

    def __init__(self,tic_tac_toe,player):
        self.tic_tac_toe = tic_tac_toe
        self.player = player

    def load_qtable(self):
        #load previous qtable if it exist
        if os.path.exists(self.qtable_filename):
            self.qtable = pickle.load(open(self.qtable_filename,"rb"))
            return True
        else:
            return False

    #create a key for the board
    #state = self.board
    #pos = action
    def get_key(self,board,pos):
        board_and_pos = board.copy()
        board_and_pos.append(pos)
        return hash(tuple(board_and_pos))

    def add_qtable_entry(self,board,pos):
        self.qtable[self.get_key(board,pos)] = self.initial_qval

    def update_qtable_entry(self,board,pos,qval):
        self.qtable[self.get_key(board,pos)] = qval

    #find what is the best move (action) for the current state
    def get_move(self,board):
        #find the action that has the highest Q value
        possible_moves = list()
        qval_list = list()
        temp = list()

        #iterate through all board position and get possible moves and their qvalue
        for pos in range(9):
            #if board position is unoccupied, consider the move
            if board[pos] == 0:
                #if in qtable, get qvalue, otherwise create entry
                
                if self.get_key(board,pos) in self.qtable:
                    possible_moves.append(pos)
                    qval_list.append(self.qtable[self.get_key(board,pos)])
                else:
                    self.add_qtable_entry(board,pos)
                    possible_moves.append(pos)
                    qval_list.append(self.initial_qval)


        temp = qval_list.copy()
        for i in range(len(qval_list)):
            temp[i] = -qval_list[i]
            
        ind = numpy.argsort(temp)
        qval_list.sort(reverse = True)
        
        temp = list()
        for i in ind:
            temp.append(possible_moves[i])

        possible_moves = temp

        #returns the possible moves, starting with the best possible move;
        #along with their corresponding qvalues
        return possible_moves, qval_list

    #result = 1 if winner, 0 draw, -1 if loser
    def update_Q_function(self,result):
        if self.player == 1:
            history = self.tic_tac_toe.historyX.copy()
            action = self.tic_tac_toe.actionX.copy()
        elif self.player == -1:
            history = self.tic_tac_toe.historyO.copy()
            action = self.tic_tac_toe.actionO.copy()

        history.reverse()
        action.reverse()
        
        #update last move qtable entry
        if result == 1:
            self.update_qtable_entry(history[0],action[0],self.win_reward)
        elif result == 0:
            self.update_qtable_entry(history[0],action[0],self.draw_reward)
        else:
            self.update_qtable_entry(history[0],action[0],self.loss_reward)
        
        historyfull = history.copy()
        #update all other moves
        history = history[1:]
        action = action[1:]
        
        #update all other moves
        for i in range(len(history)):
            board = history[i]
            pos = action[i]
            currQ = self.qtable[self.get_key(board,pos)]
        
            boardnext = historyfull[i] #board after after action pos
            [possible_moves,qval_list] = self.get_move(boardnext)
            maxQ = qval_list[0]
            newQ = currQ + self.alpha*(self.gamma*maxQ-currQ)
            self.update_qtable_entry(board,pos,newQ)
            
        #save new q function
        pickle.dump(self.qtable,open(self.qtable_filename,"wb"))