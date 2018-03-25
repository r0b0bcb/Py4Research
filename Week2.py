###############################################
#    Week 2: tic-tac-toe with numpy arrays    #
#           r0b0bcb                           #
#           3/23/2018                         #
###############################################
# write your code here!
import numpy

###############################################
# Exercise 1: empty 3x3 board function called create_board

def create_board():
    array = numpy.zeros((3,3), dtype=int)
    return array
    
board = create_board()

###############################################
# Exercise 2: change (0,0) to player 1 with function place

def place(board, player, position):
    if player == 1:
        board[position] = player
    elif player == 2:
       board[position] = player
    else:
        print("Error: invaild player #.")
    
board = create_board()
print(board) #show blank starting board
place(board, 1, (0,0))
print(board) #show move placed

###############################################
# Exercise 3: function to show availible placement optiions after a move

def possibilities(board):
    xy = numpy.where(board == 0)
    list = []
    for loop in range (board.size-1):
        list.append([xy[0][loop],xy[1][loop]])
    return list
    
possibilities(board)

###############################################
# Exercise 4: function to place random move for player 2

def random_place(board, player):
    selection = possibilities(board)
    board[random.choice(selection)] = player

random_place(board, 2)
print(board)

###############################################
# Exercise 5: 3 random move game per player

board = create_board()
for loop in range(3):
    random_place(board, 1)
    random_place(board, 2)

print(board)

###############################################
# Exercise 6: check row for win

def row_win(board, player):
    return (board==[player]).all(axis=1)

row_win(board, 1)

###############################################
# Exercise 7: check col for win

def col_win(board, player):
    return (board==[player]).all(axis=0)

col_win(board, 1)

###############################################
# Exercise 8: check diagonal wins

def diag_win(board, player):
    array = board[np.diag_indices(3)]#, np.diag(np.fliplr(board))
    if (board[np.diag_indices(3)] == [player]).all() is True or (np.diag(np.fliplr(board)) == [player]).all() is True:
        return True
    else:
        return False
    
diag_win(board, 1)

###############################################
# Exercise 9: check for winner

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) == True or col_win(board, player) == True or diag_win(board, player) == True:
            winner = player
            return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

###############################################
# Exercise 10: two robots walk into a game

def play_game():
    board = create_board()
    print(board)
    for loop in range (board.size-1):
      for player in [1,2]:
        random_place(board, player)
        if evaluate(board) != 0:
            break
      if evaluate(board) == 1:
            print("Player 1 wins")
            break
      elif evaluate(board) == 2:
            print("Player 2 wins")
            break
    if evaluate(board) == -1:
        print("Draw")
    print(board)
    
play_game()

###############################################
# Exercise 11: analize the game and bots, print timer and show graph

import time

array = []
start = time.time()
for loop in range(100):
    array.append(play_game())
stop = time.time()
timer = stop - start
print(timer)

plt.hist(array, bins=[-1,0,1,2,3])
plt.show()

###############################################
# Exercise 12: eval strategic game

import time
array = []
start = time.time()
for loop in range(1000):
    array.append(play_strategic_game())
stop = time.time()
timer = stop - start
print(timer)

plt.hist(array, bins=[-1,0,1,2,3])
plt.show()

###############################################
# Exercise 12: player 1 always starts in the middle, two bots play

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            random_place(board, player)
            if evaluate(board) != 0:
                break
        if evaluate(board) == 1:
            print("Player 1 wins")
            winner = 1
            break
        elif evaluate(board) == 2:
            print("Player 2 wins")
            winner = 2
            break
        if evaluate(board) == -1:
            print("Draw")
            winner = -1
    return winner

play_strategic_game()
