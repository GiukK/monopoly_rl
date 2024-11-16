class Tile():
    
    def __init__(self, pos, price = 100, name = "unknown"):
        
        #common to all tiles
        
        self.pos = pos
        
        self.name = name
        
        #for properties
        
        self.price = price
        
        self.owner = 0
        
        self.owned = False
        
    def __str__(self):
        return self.name
    
    
    
    
    