#compare two random computer players playing each other

#train the tabq computer player against a random computer player
import tic_tac_toe_module
import tabular_qlearning
import random
import pickle
import matplotlib.pyplot as plt
ngames = 1000

result = list()
np1win = 0
np2win = 0
ndraw = 0
for i in range(ngames):
    print('playing game '+str(i))
    iswinner = 0
    game = tic_tac_toe_module.tic_tac_toe()
    qlearning = tabular_qlearning.tabular_qlearning(game,1)
    qlearning.load_qtable()
    
    while iswinner == 0:
        qlearning.tic_tac_toe = game
        [possible_moves,qval] = qlearning.get_move(game.board)
        npm = len(possible_moves)
        game.update(1,possible_moves[random.randint(0,npm-1)])
        game.iswinner()
        
        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            break

        
        [possible_moves,qval] = qlearning.get_move(game.board)
        npm = len(possible_moves)
        game.update(-1,possible_moves[random.randint(0,npm-1)])
        game.iswinner()

        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            break
        
    if game.winner == 1:
        np1win += 1 
        print('player 1 wins!')
    elif game.winner == -1:
        print('player 2 wins!')
        np2win += 1
    elif game.winner == 0.5:
        print('draw!')
        ndraw += 1
        
    result.append(game.winner)
    
#save history of game results
pickle.dump(result,open("result_2randoms.p","wb"))

plt.plot(range(ngames),result,'rX')
plt.xlabel('game number')
plt.ylabel('result')
plt.show()