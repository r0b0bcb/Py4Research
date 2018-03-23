###############################################
#    Week 2: tic-tac-toe with numpy arrays    #
#           r0b0bcb                           #
#           3/23/2018                         #
###############################################
# write your code here!
import numpy

# Exersize 1: empty 3x3 board function called create_board

def create_board():
    array = numpy.zeros((3,3), dtype=int)
    return array
    
board = create_board()

# Exersize 2: change (0,0) to player 1 with function place

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

# Exersize 3: function to show availible placement optiions after a move

def possibilities(board):
    xy = numpy.where(board == 0)
    list = []
    for loop in range (board.size-1):
        list.append([xy[0][loop],xy[1][loop]])
    return list
    
possibilities(board)

