"""
Enemy character class
"""

import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        
        # Create enemy sprite
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physics
        self.velocity_x = ENEMY_SPEED
        self.velocity_y = 0
        self.on_ground = False
        
        # Combat
        self.health = ENEMY_MAX_HEALTH
        self.max_health = ENEMY_MAX_HEALTH
        self.damage = ENEMY_DAMAGE
        
        # AI
        self.direction = 1  # 1 for right, -1 for left
        self.patrol_distance = 100
        self.start_x = x
    
    def update(self, platforms):
        """Update enemy state"""
        # Simple patrol AI
        self.velocity_x = ENEMY_SPEED * self.direction
        
        # Check if reached patrol boundary
        if abs(self.rect.x - self.start_x) > self.patrol_distance:
            self.direction *= -1
        
        # Apply gravity
        self.velocity_y += GRAVITY
        if self.velocity_y > MAX_FALL_SPEED:
            self.velocity_y = MAX_FALL_SPEED
        
        # Move horizontally
        self.rect.x += self.velocity_x
        self.check_collision_x(platforms)
        
        # Move vertically
        self.rect.y += self.velocity_y
        self.on_ground = False
        self.check_collision_y(platforms)
    
    def check_collision_x(self, platforms):
        """Check horizontal collisions with platforms"""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                    self.direction = -1
                elif self.velocity_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
                    self.direction = 1
    
    def check_collision_y(self, platforms):
        """Check vertical collisions with platforms"""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Moving up
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
    
    def take_damage(self, damage):
        """Take damage from player"""
        self.health -= damage
        # Flash white when hit
        self.image.fill(WHITE)
        pygame.time.set_timer(pygame.USEREVENT, 100)
