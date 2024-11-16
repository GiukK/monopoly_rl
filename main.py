from Func_plotboard import plot_board
from Class_Board import GameState
from Class_Player import Player


#set up players
player1 = Player("Giocatore1")
player2 = Player("Giocatore2")
player3 = Player("Giocatore3")
player4 = Player("Giocatore4")
player5 = Player("Giocatore5")
player6 = Player("Giocatore6")

#set up player list
players = [player1, player2, player3, player4, player5, player6]

#initialize game
gm = GameState(players)