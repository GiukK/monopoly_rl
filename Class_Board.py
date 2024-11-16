import random
from Func_plotboard import plot_board

class GameState:
    
    def __init__(self, players= []):
        
        #number of turns
        self.turn = 0
        
        #list of player obj
        self.players = players
        
        #int : number of players ingame
        self.numplayers = len(players)
        
        #list of ints, represents the order in which players alternate turns
        self.order = [x for x in range(0,self.numplayers)]
        
        #list of ints: placeholder for board
        self.squares = [i for i in range(0,40)]
        
        #Bool: if the gamestate is running
        self.running = True
        
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
        current = self.players[self.order[0]]
        
        
        #Gameloop
        while self.running == True:
            
            print(f"Turn : {self.turn}\n\n")
            
            #Set turn true of the current player
            current.myturn = True
            
            print(f"----------------\nIts the turn of {current}\n")
            
            
                #they play .... now its just throw of dice. Random 1-6
            current.random_turn()
            
            
            
            #correct squares so that they do not exceed 40, probably inefficient
            if current.pos >= 40:
                current.pos = current.pos % 40

            
            #Showcase of Gamestate variables, position, money etc... to be updated
            for player in self.players:
                
                print(f"{player} is in position : {player.pos}", f"{player} money : {player.money}")
 
            
            #-------------------------------Interacts with user-------------------------------------------
            #This part is basically to control the code while it is running.
            #Adding command features such as /back or showing some variables will be helpful in the future.
            #right now the part that shows the board is at the end of the while loop, changes can be done if it is not clear
            
            print("Press Enter to skip or 's' + Enter to show the board.")
            x = input()
            #----------------------------------------------------------------------------------------------


            #The turn has finished: update the important variables
            #Set current players turn to false
            current.myturn = False
            
            #update number of turn
            self.turn += 1
            
            #update player to next in queue
            current = self.players[self.order[self.turn % self.numplayers]]
            
            
            #------------------------------------------------------------------------------------------------
            
            
            
            #Commands:  just hold Enter to skip turns fast and "s" + Enter to show the current turn played
            
            # "s" = show
            # any = skip turn
            
            if x == "s":
                
                plot_board(self)
           
            
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
        
            
            
            
            