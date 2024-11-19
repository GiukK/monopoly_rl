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
            #correct squares so that they do not exceed 40, probably inefficient
            if self.pos >= 40:
                self.pos = self.pos % 40
            
            
            
        else:
            print(f"{self.name} thinks its his turn!")
            
            
            
            #check if player ended up in a owned tile
        if gamestate.BOARD[self.pos].owned :
            
            price = gamestate.BOARD[gamestate.current.pos].price // 2
            
            #if player is broke, say it. In the future we will implement an endiing condition
            if self.money < price :
                
                print(f"{self.name} has to pay {gamestate.BOARD[self.pos].owner} but has no money!")
                
                gamestate.BOARD[self.pos].owner.money += self.money
                
                self.money = 0
            
            #if it has money, pay
            else:
                
                print(f"{self.name} has paid {gamestate.BOARD[self.pos].owner} {price}$!")
                
                gamestate.BOARD[self.pos].owner.money += price
                
                self.money -= price
                
            
            
    
    #function that handles buys
    
    def buy(self, gamestate):
        
        tile = gamestate.BOARD[self.pos]
        
        if tile.owned:
            
            print(f"{self.name} wanted to BUY but the property is owned!")
            
            return
        
        if self.money >= tile.price :
            
            tile.owner = self
            
            tile.owned = True
            
            self.money -= tile.price
            
            self.properties.append(tile)
        
            print(f"{self} has bought {tile.name}")
        else:
            print(f"{self} has no Money to buy!")
        
        
        
        
        