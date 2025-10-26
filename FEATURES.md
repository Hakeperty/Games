# Game Features Documentation

## Shadow Knight - Feature Overview

### Main Menu Screen
When you first launch the game, you'll see:
- **Title**: "Shadow Knight" displayed prominently in the center
- **Instructions**: "Press SPACE to Start"
- **Controls Guide**: 
  - Arrow Keys - Move
  - SPACE - Jump
  - Z - Attack
  - ESC - Menu

### Gameplay Screen

#### Visual Elements:
1. **Player Character**: Blue rectangular sprite (40x60 pixels)
   - Moves left and right with arrow keys
   - Can jump with smooth physics
   - Has attack animation when pressing Z
   - Flashes white when taking damage (invulnerability frames)

2. **Enemies**: Red rectangular sprites (40x50 pixels)
   - Patrol back and forth on platforms
   - Deal damage on contact with player
   - Can be defeated with player attacks
   - Flash white when hit

3. **Platforms**: Gray rectangular platforms
   - Ground platform spanning the entire bottom
   - Multiple elevated platforms for jumping challenges
   - Solid collision detection

4. **HUD (Heads-Up Display)**:
   - Health text display showing current health
   - Visual health bar (red background, green fill)
   - Enemy counter showing remaining enemies

#### Game Mechanics:

**Player Movement**:
- Smooth left/right movement at 5 pixels per frame
- Jump strength of 15 units (press SPACE while on ground)
- Gravity pulls player down at 0.8 pixels per frame
- Maximum fall speed capped at 20 pixels per frame

**Combat System**:
- Attack by pressing Z key
- Attack has a hitbox extending 60 pixels in front of player
- Deals 25 damage per hit
- Attack animation lasts 15 frames (0.25 seconds at 60 FPS)

**Enemy AI**:
- Enemies patrol a fixed distance (100 pixels) from spawn point
- Move at 2 pixels per frame
- Turn around when hitting platforms or reaching patrol boundary
- Have 50 health points
- Deal 10 damage on contact with player

**Damage System**:
- Player starts with 100 health
- Takes 10 damage when hit by enemy
- Becomes invulnerable for 1 second after taking damage
- Flashes during invulnerability period
- Game over when health reaches 0

### Game Over Screen
When player health reaches zero:
- "Game Over" message displayed in red
- "Press R to Restart" option
- "Press ESC for Menu" option

### Victory Condition
- Defeat all enemies on the level
- Current implementation has 2 enemies to defeat

### Technical Details

**Performance**:
- Runs at 60 frames per second (FPS)
- Resolution: 800x600 pixels
- Uses Pygame's sprite groups for efficient collision detection

**Physics**:
- Gravity-based physics system
- Platform collision detection on both X and Y axes
- Prevents player from falling through platforms
- Prevents player from moving through walls

**Color Scheme**:
- Background: Dark blue (20, 20, 40)
- Player: Light blue (100, 200, 255)
- Enemies: Red (255, 100, 100)
- Platforms: Gray (100, 100, 100)
- Health bar: Red/Green
- Text: White

### Level Design

The game features a platforming level with:
1. **Ground level**: Full-width platform at the bottom
2. **Platform 1**: At y=450, starting at x=200, width 200
3. **Platform 2**: At y=350, starting at x=500, width 200
4. **Platform 3**: At y=250, starting at x=100, width 150
5. **Platform 4**: At y=200, starting at x=600, width 200

### Code Architecture

**Modular Design**:
- `game.py`: Main game loop, state management, rendering
- `player.py`: Player class with all movement and combat logic
- `enemy.py`: Enemy class with AI and patrol behavior
- `platform.py`: Simple platform sprite
- `constants.py`: Centralized configuration
- `test_game.py`: Automated test suite

**State Management**:
- Three game states: "menu", "playing", "game_over"
- Clean state transitions
- Reset functionality to restart game

### Extensibility

The game is designed to be easily extended:
- Add new enemy types by extending Enemy class
- Create new levels by modifying platform positions
- Add power-ups or items as new sprite classes
- Implement additional attack types
- Add sound effects and music
- Create multiple levels with progression

### Testing

Included automated tests verify:
- All modules can be imported
- Player creation and initialization
- Enemy creation and initialization
- Platform creation
- Player movement mechanics
- Jump functionality
- Attack system
- Damage and health system
- Enemy AI behavior

All tests pass successfully, confirming the game mechanics work as intended.
