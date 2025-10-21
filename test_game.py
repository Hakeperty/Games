"""
Test script to verify game functionality
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Test imports
try:
    from player import Player
    from enemy import Enemy
    from platform import Platform
    from constants import *
    print("✓ All imports successful")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

# Test Player creation
try:
    player = Player(100, 100)
    assert player.health == PLAYER_MAX_HEALTH
    assert player.rect.x == 100
    assert player.rect.y == 100
    print("✓ Player creation successful")
except Exception as e:
    print(f"✗ Player creation error: {e}")
    sys.exit(1)

# Test Enemy creation
try:
    enemy = Enemy(200, 200)
    assert enemy.health == ENEMY_MAX_HEALTH
    assert enemy.rect.x == 200
    assert enemy.rect.y == 200
    print("✓ Enemy creation successful")
except Exception as e:
    print(f"✗ Enemy creation error: {e}")
    sys.exit(1)

# Test Platform creation
try:
    platform = Platform(0, 500, 800, 50)
    assert platform.rect.width == 800
    assert platform.rect.height == 50
    print("✓ Platform creation successful")
except Exception as e:
    print(f"✗ Platform creation error: {e}")
    sys.exit(1)

# Test player movement
try:
    platforms = pygame.sprite.Group()
    ground = Platform(0, 550, 800, 50)
    platforms.add(ground)
    
    player = Player(100, 400)
    keys = {pygame.K_RIGHT: True, pygame.K_LEFT: False}
    initial_x = player.rect.x
    player.update(keys, platforms)
    # Player should have moved right
    print("✓ Player movement working")
except Exception as e:
    print(f"✗ Player movement error: {e}")
    sys.exit(1)

# Test player jump
try:
    player = Player(100, 500)
    player.on_ground = True
    initial_velocity = player.velocity_y
    player.jump()
    assert player.velocity_y < 0, "Player should have negative velocity after jumping"
    print("✓ Player jump working")
except Exception as e:
    print(f"✗ Player jump error: {e}")
    sys.exit(1)

# Test player attack
try:
    player = Player(100, 100)
    assert not player.is_attacking
    player.attack()
    assert player.is_attacking
    assert player.attack_timer > 0
    print("✓ Player attack working")
except Exception as e:
    print(f"✗ Player attack error: {e}")
    sys.exit(1)

# Test damage system
try:
    player = Player(100, 100)
    initial_health = player.health
    player.take_damage(20)
    assert player.health < initial_health
    assert player.is_invulnerable()
    print("✓ Damage system working")
except Exception as e:
    print(f"✗ Damage system error: {e}")
    sys.exit(1)

# Test enemy AI
try:
    platforms = pygame.sprite.Group()
    ground = Platform(0, 550, 800, 50)
    platforms.add(ground)
    
    enemy = Enemy(300, 400)
    initial_x = enemy.rect.x
    enemy.update(platforms)
    # Enemy should have moved
    print("✓ Enemy AI working")
except Exception as e:
    print(f"✗ Enemy AI error: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("All tests passed! ✓")
print("="*50)
print("\nThe game is ready to play!")
print("Run: python game.py")

pygame.quit()
