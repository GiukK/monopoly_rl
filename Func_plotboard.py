import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle, Rectangle


import random 

def plot_board(gamestate):
    
    #Loads image
    img_path = 'board.jpg'
    board_img = mpimg.imread(img_path)
    
    #Creates img
    fig, ax = plt.subplots(figsize=(10, 10))
    
    #Shows background
    ax.imshow(board_img, extent=[0, 10, 0, 10])
    
    
    #----------------------------------------------------------
    #Plots properties based on color
    
    for i in range(0,40):
        
        tile = gamestate.BOARD[i]
        
        if not tile.owned:
            continue
        
        x, y = tile.pos_xy
        
        #height and width are the same
        dim = 0.5
        
        #compute the bottom left corner for correct plot
        x = x - dim / 2
        y = y - dim / 2
        
        #plot
        square = Rectangle((x,y) , dim , dim , linewidth=2, edgecolor= 'white', facecolor= tile.owner.color)
        ax.add_patch(square)
        
        
    #------------------------------------------------------------
    
    
    #Plots each player on the board
    for player in gamestate.players:
        
        x,y = gamestate.BOARD[player.pos].pos_xy
        
        
        
        #color picked from player.color
        #added randomness to position to prevent costant overlapping
        adj_x = random.uniform(-0.2,0.2)
        adj_y = random.uniform(-0.2,0.2)
        
        
        circle = Circle((x + adj_x , y + adj_y), 0.2, color= player.color, ec='white', lw=1.5, alpha = 0.8)
        ax.add_patch(circle)
        ax.text(x + adj_x, y + adj_y , f'{player.name}', ha='center', va='center', color='white', fontsize=10)
    
    #-----------------------------------------------------------
    
    # Can turn off for a cleaner look
    ax.axis('on')
    
    plt.show()
    
    return 0


#function that helps showing statistics
def show_stats(gamestate):
    
    print("Which player do you want to see?")
    
    while True:
        
        #support variable
        alert = 1
        
        #Fetch input
        x = input()
        
        if x == "":
            
            print("You are now out of stats mode.")
            
            return
        
        #show stats
        for player in gamestate.players:
            
            if x == player.name:
                
                alert = 0
                
                print("-------------------------\n")
                
                print(f"{player.name} : {player.color}\n")
                
                print(f"MONEY = {player.money}\n")
                
                print(f"The player is on top of {gamestate.BOARD[player.pos]}\n")
                
                
                print("-------------------------\n")
                
                for tile in player.properties:
                    
                    print(f"{tile} : {tile.price}")
                
                print("\n-------------------------")
                
                print("\nPress Enter to exit stats mode")
                
                
        #print alert if user misswrote
        if alert:
            
            print("This player does not exist")
                
            
                
        
                
        
        