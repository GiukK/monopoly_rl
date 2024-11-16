import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle


#Dictionary used to plot, makes sense only if used with a specific img
BOARD = {
    0: (8.90, 1),
    1: (8.10, 1),
    2: (7.30, 1),
    3: (6.50, 1),
    4: (5.70, 1),
    5: (4.90, 1),
    6: (4.10, 1),
    7: (3.30, 1),
    8: (2.50, 1),
    9: (1.70, 1),
    10: (0.90, 1),
    11: (0.90, 1.80),
    12: (0.90, 2.60),
    13: (0.90, 3.40),
    14: (0.90, 4.20),
    15: (0.90, 5.00),
    16: (0.90, 5.80),
    17: (0.90, 6.60),
    18: (0.90, 7.40),
    19: (0.90, 8.20),
    20: (0.90, 9.00),
    21: (1.70, 9.00),
    22: (2.50, 9.00),
    23: (3.30, 9.00),
    24: (4.10, 9.00),
    25: (4.90, 9.00),
    26: (5.70, 9.00),
    27: (6.50, 9.00),
    28: (7.30, 9.00),
    29: (8.10, 9.00),
    30: (8.90, 9.00),
    31: (8.90, 8.20),
    32: (8.90, 7.40),
    33: (8.90, 6.60),
    34: (8.90, 5.80),
    35: (8.90, 5.00),
    36: (8.90, 4.20),
    37: (8.90, 3.40),
    38: (8.90, 2.60),
    39: (8.90, 1.80)
}

def plot_board(gamestate):
    
    #Loads image
    img_path = 'board.jpg'
    board_img = mpimg.imread(img_path)
    
    #Creates img
    fig, ax = plt.subplots(figsize=(10, 10))
    
    #Shows background
    ax.imshow(board_img, extent=[0, 10, 0, 10])
    
    #list of ints, player.pos represents the number of the square of the player.
    player_positions = [player.pos for player in gamestate.players]
    
    
    #Plots each player on the board
    for player in gamestate.players:
        
        x,y = BOARD[player.pos]
        
        circle = Circle((x,y), 0.3, color='black', ec='white', lw=1.5, alpha = 0.8)
        ax.add_patch(circle)
        ax.text(x, y, f'{player.name}', ha='center', va='center', color='red', fontsize=10)
    
    # Can turn off for a cleaner look
    ax.axis('on')
    
    plt.show()
    
    return 0