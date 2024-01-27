# TicTacToe-Reinforcement-Learning

The aim of this project was to get a first hands-on experience of Machine Learning methods, specifically Reinforcement Learning, through the simple example TicTacToe.
The created code should win the game more often than a program choosing all moves randomly.

Overview

Starting point is a random selection of all moves.
All possible moves get saved in a dictionary with a corresponding weight.
This weight is altered based on the outcome of the game. 
Winnning moves gain weight hrough addition, while for moves that lead to losing or a tie weight is subtracted. 
The weights are taken into consideration within the random selection. Winning moves have a higher probability.
After any amount of game repititions the dictionary is saved as a JSON file.
The amount of wins, ties and losses is outputted.
The oppenent is a random player.
To prove the code is learning, a second program, in which all moves are choosen randomly, is used as comparison.

Example JSON files are within the repo.

Requirements: numpy, random, os, time, json
