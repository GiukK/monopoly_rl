#from Func_plotboard import plot_board
from Class_Board import GameState
from Class_Player import Player


#set up players
player1 = Player("p1")
player2 = Player("p2", "red")
player3 = Player("p3", "blue")
player4 = Player("p4", "green")
player5 = Player("p5", "purple")
player6 = Player("p6", "orange")

#set up player list
players = [player1, player2, player3, player4, player5, player6]

#initialize game


gm = GameState(players)