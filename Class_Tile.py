class Tile():
    
    def __init__(self, pos_xy, price = 100, name = "unknown"):
        
        #common to all tiles
        
        self.pos_xy = pos_xy
        
        self.name = name
        
        #for properties
        
        self.price = price
        
        self.owner = None
        
        self.owned = False
        
    def __str__(self):
        return self.name
    
    
    
    
    