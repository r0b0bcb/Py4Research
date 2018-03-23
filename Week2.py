###############################################
#    Week 2: tic-tac-toe with numpy arrays    #
#           r0b0bcb                           #
#           3/23/2018                         #
###############################################

# Exersize 1: empty 3x3 board

import numpy

def create_board():
    array = numpy.zeros((3,3), dtype=int)
    return array
    
board = create_board()
