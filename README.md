"# flappy-bird" 
"# flappy-bird" 
# Flappy Bird Game in Python

This is a simple Flappy Bird clone implemented in Python using the Pygame library. The game includes realistic physics, sound effects, and a high-score tracking system.

## Features
- Classic Flappy Bird gameplay mechanics
- Animated bird sprite
- Randomly generated obstacles
- Gravity and jumping mechanics
- Sound effects for flapping, scoring, and collisions
- High score tracking
- Start and game-over menus

## Prerequisites
Make sure you have Python installed on your system. You also need to install the Pygame library.

### Install Pygame
```bash
pip install pygame
```

## How to Run the Game
1. Clone this repository or download the script.
2. Ensure all image and sound assets are available in the specified file paths.
3. Run the script using:
   ```bash
   python flappybird.py
   ```

## Controls
- Press `S` to start the game from the main menu.
- Press `Spacebar` or `Mouse Click` to make the bird jump.
- Press `R` to restart after a game over.
- Press `E` to exit the game.

## Game Mechanics
- The player controls the bird, trying to navigate through randomly placed pipes.
- The bird falls due to gravity and can flap to move upward.
- Colliding with pipes or falling off the screen results in a game over.
- The game keeps track of the highest score achieved.

## File Structure
- `flappybird.py` - Main game script
- `high_score.txt` - File to store the highest score
- `Assets/` - Folder containing images and sound effects

## Dependencies
- Python 3.x
- Pygame

## Credits
This project is inspired by the classic Flappy Bird game.

## License
This project is open-source and can be used for learning purposes.


