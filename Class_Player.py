import random



class Player:
    
    def __init__(self, name = "random"):
        
        #Basic attributes for the player class, to be udpated
        self.name = name
        
        #Position
        self.pos = 0
        
        #Money
        self.money = 1500
        
        #Owned
        self.properties = []
        
        #Turn
        self.myturn = False
        
        
        
    def __str__(self):
        return self.name
#-----------------------------------------------------        
        
    #just a normal dice roll
    def dices(self):
        
        res = random.randint(1, 6)
        
        print(f"Rolled a {res}")
        
        return res
    
    
    #updates pos with the dice roll
    def move(self):
        self.pos += self.dices()
        
    
    #MAIN function that handles how players act in their turns
    
    def random_turn(self, gamestate):
        
        if self.myturn == True:
            
            print(f"{self.name} moves!")
            
            want_to_buy = random.randint(0, 1)
            
            if want_to_buy:
                self.buy(gamestate)
                
            self.move()
        else:
            print(f"{self.name} thinks its his turn!")
            
    
    #function that handles buys
    
    def buy(self, gamestate):
        
        tile = gamestate.BOARD[gamestate.current.pos]
        
        if self.money >= tile.price :
            
            tile.owner = self
            
            tile.owned = True
            
            self.money -= tile.price
            
            self.properties.append(tile)
        
            print(f"{self} has bought {tile.name}")
        else:
            print(f"{self} has no Money to buy!")
        
        
        
        
        