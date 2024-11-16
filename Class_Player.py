import random



class Player:
    
    def __init__(self, name = "random"):
        
        #Basic attributes for the player class, to be udpated
        self.name = name
        
        #Position
        self.pos = 0
        
        #Money
        self.money = 1500
        
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
        
    
    #Checks if it is his turn, if it is it moves, otherwise it will not alt the code but just alert you that you somehow called his turn mistakenly
    def random_turn(self):
        if self.myturn == True:
            
            print(f"{self.name} moves!")
            self.move()
        else:
            print(f"{self.name} thinks its his turn!")
            
            
            
        
        
        
        
        