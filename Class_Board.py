import random
from Func_plotboard import plot_board
from Class_Tile import Tile

class GameState:
    
    def __init__(self, players= []):
        
        #number of turns
        self.turn = 0
        
        #list of player obj
        self.players = players
        
        self.current = None
        
        #int : number of players ingame
        self.numplayers = len(players)
        
        #list of ints, represents the order in which players alternate turns
        self.order = [x for x in range(0,self.numplayers)]
        
        #list of ints: placeholder for board
        self.squares = [i for i in range(0,40)]
        
        #Bool: if the gamestate is running
        self.running = True
        
        #Board set with minimum characteristics, just xy posistion with respect to img
        self.BOARD = {
    0: Tile((8.90, 1)),
    1: Tile((8.10, 1)),
    2: Tile((7.30, 1)),
    3: Tile((6.50, 1)),
    4: Tile((5.70, 1)),
    5: Tile((4.90, 1)),
    6: Tile((4.10, 1)),
    7: Tile((3.30, 1)),
    8: Tile((2.50, 1)),
    9: Tile((1.70, 1)),
    10: Tile((0.90, 1)),
    11: Tile((0.90, 1.80)),
    12: Tile((0.90, 2.60)),
    13: Tile((0.90, 3.40)),
    14: Tile((0.90, 4.20)),
    15: Tile((0.90, 5.00)),
    16: Tile((0.90, 5.80)),
    17: Tile((0.90, 6.60)),
    18: Tile((0.90, 7.40)),
    19: Tile((0.90, 8.20)),
    20: Tile((0.90, 9.00)),
    21: Tile((1.70, 9.00)),
    22: Tile((2.50, 9.00)),
    23: Tile((3.30, 9.00)),
    24: Tile((4.10, 9.00)),
    25: Tile((4.90, 9.00)),
    26: Tile((5.70, 9.00)),
    27: Tile((6.50, 9.00)),
    28: Tile((7.30, 9.00)),
    29: Tile((8.10, 9.00)),
    30: Tile((8.90, 9.00)),
    31: Tile((8.90, 8.20)),
    32: Tile((8.90, 7.40)),
    33: Tile((8.90, 6.60)),
    34: Tile((8.90, 5.80)),
    35: Tile((8.90, 5.00)),
    36: Tile((8.90, 4.20)),
    37: Tile((8.90, 3.40)),
    38: Tile((8.90, 2.60)),
    39: Tile((8.90, 1.80)),
}
        
        #Calls the starting function when initialized
        self.start()
        
        
    def start(self):
        
        #This are just for prettier logs in the command line
        print("------------------------   Game has started   ------------------------\n\n")
        
        
        #Shuffles randomly the order, once shouffled at the start, it will remain the same until the end.
        #The process of eliminating players and changing order of turns has to be treated carefully in the future.
        random.shuffle(self.order)

        
        print(f"------------------------   {self.players[self.order[0]]} goes first!   ------------------------\n\n")
        
        #Sets the first player on the order list as the current player.
        #current will be used in the gameloop as a placeholder to keep trace of the right player.
        self.current = self.players[self.order[0]]
        
        
        #Gameloop
        while self.running == True:
            
            print(f"Turn : {self.turn}\n\n")
            
            #Set turn true of the current player
            self.current.myturn = True
            
            print(f"----------------\nIts the turn of {self.current}\n")
            
            
                #they play ....
            self.current.random_turn(self)
            

            
            #Showcase of Gamestate variables, position, money etc... to be updated
            for player in self.players:
                
                print(f"{player} is in position : {player.pos}", f"{player} money : {player.money}")
 
            
            #-------------------------------Interacts with user-------------------------------------------
            #This part is basically to control the code while it is running.
            #Adding command features such as /back or showing some variables will be helpful in the future.
            #right now the part that shows the board is at the end of the while loop, changes can be done if it is not clear
            
            print("Press Enter to skip or write 'help'")
            
            
            
            #Fetch input
            x = input()
            
            #Commands:  just hold Enter to skip turns fast and "s" + Enter to show the current turn played
            
            # "s" = show
            # any = skip turn
            
            if x == "help":
                
                print("The commands currently are:")
                print("s : to SHOW the current board")
                print("stats : to see a players stats")
 
            elif x == "s":
            
                plot_board(self)
                
            elif x == "stats":
                
                print("Which player do you want to see?")
                x = input()
                
                for player in self.players:
                    if x == player.name:
                        print("-------------------------------")
                        for tile in player.properties:
                            print(f"{tile.name} : {tile.price} $")
                        
                        print("-------------------------------")
                        break
                        
                    print("No player has that name.")
                

            #----------------------------------------------------------------------------------------------


            #The turn has finished: update the important variables
            #Set current players turn to false
            self.current.myturn = False
            
            #update number of turn
            self.turn += 1
            
            #update player to next in queue
            self.current = self.players[self.order[self.turn % self.numplayers]]
            
            
            #------------------------------------------------------------------------------------------------
            
        #out of the gameloop
        print("\n\n------------------------GAME OVER------------------------")
            
        
        
        
        
        
        
        
        
        
    def load_gamestate(self,gamestate):
        
        #Set every local attribute == to the one loaded, can be useful in the future to replicate scenarios?
        
        self.turn = gamestate.turn
        self.players = gamestate.players
        self.numplayers = gamestate.numplayers
        self.order = gamestate.order
        self.squares = gamestate.squares
        self.running = True
        
            
            
            
            