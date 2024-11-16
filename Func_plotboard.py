import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle

def plot_board(gamestate):
    
    #Loads image
    img_path = 'board.jpg'
    board_img = mpimg.imread(img_path)
    
    #Creates img
    fig, ax = plt.subplots(figsize=(10, 10))
    
    #Shows background
    ax.imshow(board_img, extent=[0, 10, 0, 10])
    
    #Plots each player on the board
    for player in gamestate.players:
        
        x,y = gamestate.BOARD[player.pos].pos_xy
        
        circle = Circle((x,y), 0.3, color='black', ec='white', lw=1.5, alpha = 0.8)
        ax.add_patch(circle)
        ax.text(x, y, f'{player.name}', ha='center', va='center', color='red', fontsize=10)
    
    # Can turn off for a cleaner look
    ax.axis('on')
    
    plt.show()
    
    return 0