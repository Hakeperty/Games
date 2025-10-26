# Shadow Knight - A 2D Platformer Game

A side-scrolling 2D platformer game inspired by Hollow Knight, built with Python and Pygame.

## Features

- **Fluid Movement**: Smooth character controls with running and jumping mechanics
- **Combat System**: Attack enemies with a melee attack system
- **Enemy AI**: Patrolling enemies with collision detection
- **Health System**: Player and enemy health management with visual feedback
- **Platform Physics**: Realistic gravity and collision detection
- **Game States**: Main menu, gameplay, and game over screens

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hakeperty/Games.git
cd Games
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

Run the game:
```bash
python game.py
```

### Controls

- **Arrow Keys**: Move left and right
- **SPACE**: Jump
- **Z**: Attack
- **ESC**: Pause/Return to menu
- **R**: Restart (when game over)

## Gameplay

You control a knight exploring a platforming world filled with enemies. Navigate through platforms, defeat enemies, and survive as long as possible!

- Defeat all enemies to win
- Avoid taking too much damage or it's game over
- Use your attack to defeat patrolling enemies
- Time your jumps carefully to navigate the platforms

## Game Structure

- `game.py` - Main game loop and state management
- `player.py` - Player character with movement, jumping, and combat
- `enemy.py` - Enemy AI with patrol behavior
- `platform.py` - Platform objects for the game world
- `constants.py` - Game configuration and constants

## Requirements

- Python 3.7+
- Pygame 2.5.2

## License

This project is open source and available for educational purposes.