import numpy as np
import random


board_random = np.zeros((3,3))


def board_full(board):
    """returns True if board is full and False if not"""
    if np.count_nonzero(board) == 9:
        return True
    return False


def check_win(array):
        """return 0: No winner; 1: Player1 won; 2: Player2 won"""


        #vertical win
        for row in range(3):
            if array[row][0] == array[row][1] == array[row][2] != 0:
                return array[row][0]
           
        #horizontal win
        for col in range(3):
            if array[0][col] == array[1][col] == array[2][col] != 0:
               return array[0][col]
           
        #diagonal win
        if array [0][0] == array [1][1] == array[2][2] != 0 or array[2][0] == array[1][1] == array[0][2] != 0:
            return array[1][1]
       
        #no win
        return 0


def random_move(board, player):
    """picks a random free space and plays 1 or 2 depending on player"""
    free_spaces = np.where(board == 0) #returns 2D arr [rows][cols] all squares with a zero in them, so [arr[0][0]];[arr[1][0]] is index of one playable square
    count_free_spaces = free_spaces[0].__len__()
    pick = random.randint(0,count_free_spaces-1) #choose a random square
    board[free_spaces[0][pick]][free_spaces[1][pick]] = player
   
def stats(result  :int, data):
    """updates the data of frequency of tie, player win"""
    data[result] += 1
    return data


statistics_random = {
    0: 0,
    1: 0,
    2: 0
}


x = 100  #number of game repetitions


if __name__ == "__main__":
    for i in range(x):  #play game x times
        if i%2 == 0: #switch first player each time
            player_random = 1
        else:
            player_random = 2


        while not board_full(board_random) and check_win(board_random) == 0: #play game till tie or winner
            move = random_move(board_random, player_random)
            player_random = player_random%2+1  #switch player
   
        stats(check_win(board_random),statistics_random) #update stats


        board_random = np.zeros((3,3))  #reset board
        player_random = 1


    #analysis
    print(statistics_random)
    for i in range(3):  #percentage of tie, win
        print(statistics_random[i] / x)
