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
    return (board==[1,1,1]).all(axis=1)

row_win(board, 1)

###############################################
# Exercise 7: check col for win

def col_win(board, player):
    return (board==[1,1,1]).all(axis=0)

col_win(board, 1)
