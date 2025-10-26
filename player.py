"""
Player character class
"""

import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        
        # Create player sprite
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        
        # Combat
        self.health = PLAYER_MAX_HEALTH
        self.max_health = PLAYER_MAX_HEALTH
        self.attack_damage = PLAYER_ATTACK_DAMAGE
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_duration = 15  # frames
        self.attack_rect = pygame.Rect(0, 0, 60, 40)
        
        # Facing direction
        self.facing_right = True
        
        # Invulnerability after taking damage
        self.invulnerable_timer = 0
        self.invulnerable_duration = 60  # frames
    
    def update(self, keys, platforms):
        """Update player state"""
        # Horizontal movement
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -PLAYER_SPEED
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.velocity_x = PLAYER_SPEED
            self.facing_right = True
        
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
        
        # Update attack
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
            
            # Update attack hitbox position
            if self.facing_right:
                self.attack_rect.midleft = self.rect.midright
            else:
                self.attack_rect.midright = self.rect.midleft
        
        # Update invulnerability
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= 1
            # Flash effect
            if self.invulnerable_timer % 10 < 5:
                self.image.set_alpha(128)
            else:
                self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
    
    def check_collision_x(self, platforms):
        """Check horizontal collisions with platforms"""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
    
    def check_collision_y(self, platforms):
        """Check vertical collisions with platforms"""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Jumping
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
    
    def jump(self):
        """Make the player jump"""
        if self.on_ground:
            self.velocity_y = -PLAYER_JUMP_STRENGTH
            self.on_ground = False
    
    def attack(self):
        """Perform attack"""
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            
            # Set attack hitbox
            if self.facing_right:
                self.attack_rect.midleft = self.rect.midright
            else:
                self.attack_rect.midright = self.rect.midleft
    
    def take_damage(self, damage):
        """Take damage from enemy"""
        if not self.is_invulnerable():
            self.health -= damage
            self.invulnerable_timer = self.invulnerable_duration
            if self.health < 0:
                self.health = 0
    
    def is_invulnerable(self):
        """Check if player is currently invulnerable"""
        return self.invulnerable_timer > 0
