#script to play tic tac toe
import tic_tac_toe_module
import tabular_qlearning
game = tic_tac_toe_module.tic_tac_toe()

print('1 = human vs human; 2 = human vs computer (tabq)')
isvalidin = 0
while isvalidin == 0:
    val = int(input('make selection: '))
    if val == 1 or val == 2:
        isvalidin = 1

#player 1 is X (1)
#player 2 is O (-1)
if val == 1:
    iswinner = 0
    while iswinner == 0:
        game.printboard()
        print('')
        game.printboardindex()

        pos = int(input('player 1, input move: '))
        game.update(1,pos)
        game.iswinner()




        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            game.printboard()
            print('')
            game.printboardindex()
            break

        game.printboard()
        print('')
        game.printboardindex()
        
        pos = int(input('player 2, input move: '))
        game.update(-1,pos)
        game.iswinner()

        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            game.printboard()
            print('')
            game.printboardindex()
            break
        

if val == 2:
    iswinner = 0
    qlearning = tabular_qlearning.tabular_qlearning(game,1)
    qlearning.load_qtable()
    
    while iswinner == 0:
        game.printboard()
        print('')
        game.printboardindex()

        print('player 1 (computer) turn: ')
        qlearning.tic_tac_toe = game
        [possible_moves,qval] = qlearning.get_move(game.board)
        game.update(1,possible_moves[0])
        game.iswinner()
        
        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            game.printboard()
            print('')
            game.printboardindex()
            break

        game.printboard()
        print('')
        game.printboardindex()
        
        pos = int(input('player 2, input move: '))
        game.update(-1,pos)
        game.iswinner()

        if game.winner == 1 or game.winner == -1 or game.winner == 0.5:
            iswinner = 1
            game.printboard()
            print('')
            game.printboardindex()
            break
        
if game.winner == 1:
    qlearning.update_Q_function(1)
    print('player 1 wins!')
elif game.winner == -1:
    print('player 2 wins!')
    qlearning.update_Q_function(-1)
elif game.winner == 0.5:
    print('draw!')
    qlearning.update_Q_function(0)