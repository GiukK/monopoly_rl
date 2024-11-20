import random



class Player:
    
    def __init__(self, name = "random", color = "black"):
        
        #Basic attributes for the player class, to be udpated
        self.name = name
        
        #Pawn color on the board, color has to be valid with matplotlib
        self.color = color
        
        #Position
        self.pos = 0
        
        #Money
        self.money = 1500
        
        #Owned
        self.properties = []
        
        #Turn
        self.myturn = False
        
        #Lost
        self.lost = 0
        
        
        
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
            
            #Turn starts -> player moves -> player buys or not
            
            
            #Moves--------------------------------------------
            print(f"{self.name} moves!")
                
            self.move()
            #correct squares so that they do not exceed 40, probably inefficient
            if self.pos >= 40:
                self.pos = self.pos % 40
                
            #Buys--------------------------------------------
            want_to_buy = random.randint(0, 1)
                
            if want_to_buy:
                self.buy(gamestate)
                
            
        else:
            #This is to catch eventual errors in the flow of players
            print(f"{self.name} thinks its his turn!")
            
            
            
            #check if player ended up in a owned tile
        if gamestate.BOARD[self.pos].owned :
            
            price = gamestate.BOARD[gamestate.current.pos].price // 2
            
            #if player is broke, say it. In the future we will implement an endiing condition
            if self.money < price :
                
                print(f"{self.name} has to pay {gamestate.BOARD[self.pos].owner} but has no money!")
                
                self.emergency(gamestate,price)
            
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
            
        
        
    #This function handles selling to a random player that has money to buy
    
    def random_sell(self, gamestate):
        
        #choose random tile to sell
        tile = random.choice(self.properties)
        
        #decide price
        price = tile.price // 2
        
        #choose random player to sell - IT MUST NOT BE BROKE
        
        available = []
        
        for player in gamestate.players:
            
            if player.money >= price:
                
                available.append(player)
                
        #handle possible errors
        
        #SINCE this is called only in emergencies
        #if you want to sell buy no one can buy then you just lose
        #right now the money in cycle is fixed so idk...
        
        if len(available) == 0:
            
            self.lose()
            
            return
        
        buyer = random.choice(available)
        
        #remove tile from seller properties
        self.properties.remove(tile)
        
        #add tile to buyer 
        buyer.properties.append(tile)
        
        #add money to seller
        self.money += price
        
        #subtract money to buyer
        buyer.money -= price
        
        print(f"{self} has sold {tile} to {buyer} for {price}$")
    
    
    #this function handles emergencies, when player has to pay buy has no money
    #In case of failure it calls lose()
    
    def emergency(self, gamestate, price):
        
        while self.money < price:
            
            if self.properties == []:
                
                self.lose(gamestate)
                
                return
                
            self.random_sell(gamestate)
            
    
    #handles losses
    def lose(self, gamestate):
        
        #remove player from game
        
        #gamestate.players.remove(self)
        
        
        #to actually remove player from game the code should be changed to handle "next turn"
        # and to update list of players and lenght of lists and orders...
        
        #right now I just make an inner field to handle losses and skip turn if the player has lost
        
        self.lost = 1
        
        print(f"{self} HAS LOST! ")
        
        
        
            
            
        
        
        
        