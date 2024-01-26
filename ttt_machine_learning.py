import numpy as np
import random
import json
import time
import os
from ttt_random import check_win, board_full, random_move


board_ml = np.zeros((3,3))


try:
    os.remove("data.json")
except FileNotFoundError:
    None


try:
    with open("data.json", "r") as file:
        data_ml = json.loads(file.read())
        file.close


except FileNotFoundError:
    data_ml = {}


def update_data(data  :dict, key, num_free_spaces  :int):
    """adds a new key value pair to the data dict - key: hashable board; value: array of tens, array_length = number of free spaces"""
    data[key] = [10 for i in range(num_free_spaces)]  
    return None


def ml_move(board, player  :int, data  :dict):
    """picks a free space according to the weights in data; returns array of game situation and made move"""
    board_str = str(board)
    free_spaces = np.where(board == 0)
    count_free_spaces = free_spaces[0].__len__()
   
    try:
        choice = int(random.choices(range(count_free_spaces), data[board_str], k=1)[0])
        board[free_spaces[0][choice]][free_spaces[1][choice]] = player


    except KeyError:  #occurs whenever there is a new game situation
        update_data(data, board_str, count_free_spaces)  #adds new situation to data
        choice = int(random.choices(range(0,count_free_spaces), data[board_str], k=1)[0])
        board[free_spaces[0][choice]][free_spaces[1][choice]] = player
   
    except ValueError: #occurs if all weights are zero
        choice = random.randint(0, count_free_spaces-1)
        board[free_spaces[0][choice]][free_spaces[1][choice]] = player
   
    return ([board_str, choice])  #Game Situation and move to save, later accessible to do the learning


def stats(result  :int, data):
    """updates the data of frequency of tie, player win"""
    data[result] += 1
    return data


statistics_ml = {
    0: 0,
    1: 0,
    2: 0
}


x = 10  #number of game repetitions
moves_list = []
start_time = time.time()


if __name__ == "__main__":
    for i in range(x):
        if i%2 == 0:
            player_ml = 1
        else:
            player_ml = 2
        while not board_full(board_ml) and check_win(board_ml) == 0: #play game till tie or winner
            if player_ml == 1:
                move = ml_move(board_ml, player_ml, data_ml)
                moves_list.append(move)
            else:
                move = random_move(board_ml, player_ml)
           
            player_ml = player_ml%2+1  #switch player
       
        stats(check_win(board_ml), statistics_ml)


        if check_win(board_ml) == 1:  #reward and punishment
            for i in range(0, len(moves_list)):
                if  data_ml[moves_list[i][0]][moves_list[i][1]] != 0:
                    data_ml[moves_list[i][0]][moves_list[i][1]] += 5
        else:
            for i in range(0,len(moves_list)):
                if  data_ml[moves_list[i][0]][moves_list[i][1]] != 0:
                    data_ml[moves_list[i][0]][moves_list[i][1]] -= 5
       
        #reset everything
        moves_list = []
        board_ml = np.zeros((3,3))
       


    with open("data.json", "w") as file:
        file.write(json.dumps(data_ml))
        file.close


    #analysis
    print(statistics_ml)
    for i in range(3):  #percentage of tie, win
        print(statistics_ml[i] / x)


    #duration
    end_time = time.time()
    real_time = end_time - start_time
    print(real_time)
