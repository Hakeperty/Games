# Project Structure

```
Games/
├── .gitignore              # Python artifacts to ignore
├── README.md               # Main project documentation
├── FEATURES.md             # Detailed feature documentation
├── requirements.txt        # Python dependencies (pygame==2.5.2)
├── game.py                 # Main game loop and state management
├── player.py               # Player character class
├── enemy.py                # Enemy AI class
├── platform.py             # Platform sprite class
├── constants.py            # Game configuration constants
└── test_game.py            # Automated test suite
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python test_game.py

# Play the game
python game.py
```

## Game Architecture

```
┌─────────────────────────────────────────────┐
│           Game (Main Controller)            │
│  - State Management (menu/playing/gameover) │
│  - Event Handling                           │
│  - Rendering                                │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼─────┐  ┌─────▼──────┐
│   Player   │  │   Enemy    │
│  Sprite    │  │   Sprite   │
│            │  │            │
│ - Movement │  │ - AI       │
│ - Jump     │  │ - Patrol   │
│ - Attack   │  │ - Damage   │
│ - Health   │  │            │
└──────┬─────┘  └─────┬──────┘
       │               │
       └───────┬───────┘
               │
        ┌──────▼──────┐
        │  Platform   │
        │   Sprite    │
        │             │
        │ - Collision │
        └─────────────┘
```

## Class Hierarchy

```
pygame.sprite.Sprite
    ├── Player
    │   └── Methods:
    │       ├── update()
    │       ├── jump()
    │       ├── attack()
    │       ├── take_damage()
    │       └── check_collision_x/y()
    │
    ├── Enemy
    │   └── Methods:
    │       ├── update()
    │       ├── take_damage()
    │       └── check_collision_x/y()
    │
    └── Platform
        └── Simple sprite with rect
```

## Game Flow

```
Start
  │
  ▼
┌──────────┐
│   Menu   │◄──────────┐
└────┬─────┘           │
     │ [SPACE]         │
     ▼                 │
┌──────────┐           │
│ Playing  │           │
│          │           │
│ - Move   │           │
│ - Jump   │           │
│ - Attack │           │
└────┬─────┘           │
     │                 │
     │ [Health = 0]    │ [ESC]
     ▼                 │
┌──────────┐           │
│Game Over │───────────┘
│          │ [R - Restart]
└──────────┘ [ESC - Menu]
```

## Key Features Implementation

### Physics System
- Gravity: 0.8 pixels/frame
- Player Speed: 5 pixels/frame
- Jump Strength: -15 pixels/frame
- Max Fall Speed: 20 pixels/frame

### Combat System
- Attack Range: 60 pixels
- Attack Duration: 15 frames (0.25s)
- Player Damage: 25 per hit
- Enemy Damage: 10 per hit

### Health System
- Player Max Health: 100
- Enemy Max Health: 50
- Invulnerability: 60 frames (1s) after damage

### Collision Detection
- Separate X and Y axis collision checks
- Platform landing detection
- Enemy collision with platforms and patrol boundaries
- Attack hitbox detection

## Files Overview

| File | Lines | Purpose |
|------|-------|---------|
| game.py | ~240 | Main game loop, rendering, state management |
| player.py | ~150 | Player character mechanics |
| enemy.py | ~90 | Enemy AI and behavior |
| platform.py | ~12 | Platform sprite |
| constants.py | ~35 | Configuration values |
| test_game.py | ~110 | Automated tests |
| README.md | ~65 | User documentation |
| FEATURES.md | ~210 | Feature documentation |

**Total: ~840 lines of code and documentation**

## Extension Ideas

1. **Multiple Levels**: Create level files with different platform layouts
2. **Power-ups**: Add collectible items for health/abilities
3. **More Enemy Types**: Flying enemies, boss enemies
4. **Sound Effects**: Attack sounds, jump sounds, background music
5. **Animations**: Sprite sheets for character animations
6. **Scoring System**: Track defeated enemies and time
7. **Save System**: Save progress and high scores
8. **Menu Improvements**: Options, settings, level select
