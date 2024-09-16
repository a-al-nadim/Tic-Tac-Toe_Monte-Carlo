import random
import numpy as np

def tic_tac_toe2(board, p):

    who = p;
    end_game = 0;
    reward = 0;
    action = [];
    
    while end_game == 0 and 0 in board:
        if who == 1:
            
            ##Check for attack and defense
            
            attack = 0;
            defense = 0;
            move_done = 0;
            
            ##diagonally 
            
            diag = 0;
            diag2 = 0;
            for i in range(3):
                diag = diag + board[i][i];
                diag2 = diag2 + board[i][2-i];
    
            if diag == 2 and move_done == 0:
                for i in range(3):
                    if board[i][i] == 0:
                        board[i][i] = 1;
                        attack = 1;
                        reward = 1;
                        move_done = 1;
                        a = [i, i];
                        action.append(a);
                        break;
            elif diag2 == 2 and move_done == 0:
                for i in range(3):
                    if board[i][2-i] == 0:
                        board[i][2-i] = 1;
                        attack = 1;
                        reward = 1;
                        move_done = 1;
                        a = [i, 2-i];
                        action.append(a);
                        break;
            elif diag == 10 and move_done == 0:
                for i in range(3):
                    if board[i][i] == 0:
                        board[i][i] = 1;
                        defense = 1; 
                        move_done = 1;
                        a = [i, i];
                        action.append(a);
                        break;
            elif diag2 == 10 and move_done == 0:
                for i in range(3):
                    if board[i][2-i] == 0:
                        board[i][2-i] = 1;
                        defense = 1;
                        move_done = 1;
                        a = [i, 2-i];
                        action.append(a);
                        break;
            
            #Horizontally and vertically
            else:
                if move_done == 0:
                    for i in range(3):
                        if sum(board[i][:]) == 2 and move_done == 0:
                            indices = np.where(board[i][:] == 0);
                            board[i][indices] = 1;
                            attack = 1;
                            reward = 1;
                            move_done = 1;
                            a = [i, indices];
                            action.append(a);
                            break;
                        elif sum(board[:][i]) == 2 and move_done == 0:
                            indices = np.where(board[:][i] == 0);
                            board[indices][i] = 1;
                            attack = 1;
                            reward = 1;
                            move_done = 1;
                            a = [indices, i];
                            action.append(a);
                            break;
                        
                    for i in range(3):
                        if sum(board[i][:]) == 10 and move_done == 0:
                            indices = np.where(board[i][:] == 0);
                            board[i][indices] = 1;
                            defense = 1;
                            move_done = 1;
                            a = [i, indices];
                            action.append(a);
                            break;
                        elif sum(board[:][i]) == 10 and move_done == 0:
                            indices = np.where(board[:][i] == 0);
                            board[indices][i] = 1;
                            defense = 1;
                            move_done = 1;
                            a = [indices, i];
                            action.append(a);
                            break;

                    
            
                        
            
            ## If there is no attack or defense, make a random move
            
            if attack == 0 and defense == 0:
                empty_cell = [];
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            temp = [i,j];
                            empty_cell.append(temp);
                random_move = random.choice(empty_cell);
                board[random_move[0]][random_move[1]] = 1;
                move_done = 1;
                action.append(random_move);
            
            
            ## Check if the game is over
            if reward != 0:
                end_game = 1;
            ## Next move is from the opponent
            else:
                who = who + 4;
            
            
        
        
        
        ## Same for the opponent player 
        elif who == 5:
            
            ##Check for attack and defense
            
            attack = 0;
            defense = 0;
            move_done = 0;
            
            ##diagonally 
            
            diag = 0;
            diag2 = 0;
            for i in range(3):
                diag = diag + board[i][i];
                diag2 = diag2 + board[i][2-i];
    
            if diag == 10 and move_done == 0:
                for i in range(3):
                    if board[i][i] == 0:
                        board[i][i] = 5;
                        attack = 1;
                        reward = -1;
                        move_done = 1;
                        break;
            elif diag2 == 10 and move_done == 0:
                for i in range(3):
                    if board[i][2-i] == 0:
                        board[i][2-i] = 5;
                        attack = 1;
                        reward = -1;
                        move_done = 1;
                        break;
            elif diag == 2 and move_done == 0:
                for i in range(3):
                    if board[i][i] == 0:
                        board[i][i] = 5;
                        defense = 1;
                        move_done = 1;
                        break;
            elif diag2 == 2 and move_done == 0:
                for i in range(3):
                    if board[i][2-i] == 0:
                        board[i][2-i] = 5;
                        defense = 1;
                        move_done = 1;
                        break;
            
            #Horizontally and vertically
            else:
                if move_done == 0:
                    for i in range(3):
                        if sum(board[i][:]) == 10 and move_done == 0:
                            indices = np.where(board[i][:] == 0);
                            board[i][indices] = 5;
                            attack = 1;
                            reward = -1;
                            move_done = 1;
                            break;
                        elif sum(board[:][i]) == 10 and move_done == 0:
                            indices = np.where(board[:][i] == 0);
                            board[indices][i] = 5;
                            attack = 1;
                            reward = -1;
                            move_done = 1;
                            break;
                    
                    for i in range(3):
                        if sum(board[i][:]) == 2 and move_done == 0:
                            indices = np.where(board[i][:] == 0);
                            board[i][indices] = 5;
                            defense = 1;
                            move_done = 1;
                            break;
                        elif sum(board[:][i]) == 2 and move_done == 0:
                            indices = np.where(board[:][i] == 0);
                            board[indices][i] = 5;
                            defense = 1;
                            move_done = 1;
                            break;

            
            ## If there is no attack or defense, make a random move
            
            if attack == 0 and defense == 0:
                empty_cell = [];
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            temp = [i,j];
                            empty_cell.append(temp);
                random_move = random.choice(empty_cell);
                board[random_move[0]][random_move[1]] = 5;
                move_done = 1;
            
            
            ## Check if the game is over
            if attack == 1:
                end_game = 1;
            ## Next move is from the opponent
            else:
                who = who - 4;
            
    return board, reward, action[0];


simul = 10000;
U = [];
action_space = [];
occur = [];

for i in range(simul):
    current_state = np.zeros([3,3]);
    a, b, c = tic_tac_toe2(current_state, 1);
    if c in action_space:
        for j in range(len(action_space)):
            if action_space[j] == c:
                U[j] = U[j] + b;
                occur[j] = occur[j] + 1;
    
    else:
        action_space.append(c);
        U.append(b);
        occur.append(1);

P = [];
for i in range(len(U)):
    P.append(U[i]/occur[i]);

print("Action = ", action_space)
print("P = ", P)


