## Flask Application Design for Tetris Terminal Game

### HTML Files

- **index.html**:
   - Main page containing the game board and controls.
   - Includes JavaScript code for handling player input and game logic.

- **game_over.html**:
   - Page displayed when the player loses the game.
   - Provides options to restart or quit the game.

### Routes

- **`@app.route('/')`**:
   - Renders the `index.html` page and initializes the game.

- **`@app.route('/move')`**:
   - Handles player input for moving the falling tetromino.
   - Updates the game state and sends it back to the client.

- **`@app.route('/rotate')`**:
   - Handles player input for rotating the falling tetromino.
   - Updates the game state and sends it back to the client.

- **`@app.route('/game_over')`**:
   - Renders the `game_over.html` page.
   - Allows the user to restart or quit the game.

### Example Usage

The HTML files and routes work together as follows:

1. The user accesses the `/` route, which renders the `index.html` page and initializes the game.
2. The JavaScript code in `index.html` captures user input for moving and rotating the tetromino and sends it to the server using the `/move` and `/rotate` routes, respectively.
3. The `/move` and `/rotate` routes update the game state and send the updated state back to the client.
4. The JavaScript code in `index.html` updates the game board based on the updated state.
5. If the player loses the game, the `/game_over` route is triggered, rendering the `game_over.html` page.
6. From the `game_over.html` page, the user can either restart the game or quit.