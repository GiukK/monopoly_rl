Here’s a clear summary of the code for this project:

---

### General Overview  
The code simulates a simplified board game similar to Monopoly. It includes:  
1. **Main Classes**:  
   - `GameState` (manages the game flow).  
   - `Player` (represents a player with attributes like money and properties).  
   - `Tile` (represents the board spaces).  
2. **Core Mechanics**:  
   - Players take turns rolling dice, moving on the board, and interacting with spaces (buying, paying, or triggering events).  
   - The game handles turns, property transactions, and emergency scenarios (e.g., selling properties when out of money).  

---

### Key Components  
#### 1. `Class_Board.py` (manages the board and game flow)  
- **GameState**:  
  - Initializes the board with 40 tiles (e.g., "Go," properties, chance spaces).  
  - Tracks the turn order, current player, and overall game state.  
  - **Main Loop**: Each turn, a player rolls dice, moves, and decides on actions (e.g., buying a property).  
  - **User Interaction** (optional): Allows pausing the game to display stats or the board state.  

---

#### 2. `Class_Player.py` (manages players)  
- **Key Attributes**:  
  - Name, token color, position on the board, money (starting with $1500), and owned properties.  
- **Core Actions**:  
  - **Rolling Dice** and moving on the board.  
  - **Buying Properties** if available and the player has enough money.  
  - **Paying Rent** if landing on another player's property.  
  - **Selling Properties** in emergencies to cover debts.  
  - **Handling Losses**: A player loses if they cannot pay and have no properties to sell.  

---

#### 3. `Class_Tile.py` (defines board tiles)  
- Each tile has:  
  - **Position** (coordinates on the board), name, and price.  
  - Ownership information: whether it is owned and who the owner is.  

---

### Game Flow  
1. The game starts by creating the board (`GameState`) and a list of players (`Player`).  
2. Players take turns:  
   - Roll dice and move.  
   - Interact with the tile they land on (e.g., buy, pay rent, or do nothing for special tiles).  
3. The game continues until only one player remains with money or properties.  

---

### How to Play or Test  
1. **Start the Game**: Create an instance of `GameState` with a list of players.  
2. You can activate interactive mode (commands include):  
   - `s`: Display the board.  
   - `stats`: Show player stats.  
   - `fast`: Disable interaction for automatic game progression.  
3. The game automatically ends when there is a winner.  
