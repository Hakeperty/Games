"""
Hollow Knight-inspired 2D Platformer Game
A side-scrolling action platformer with combat mechanics
"""

import pygame
import sys
from player import Player
from enemy import Enemy
from platform import Platform
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shadow Knight - A 2D Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "menu"  # menu, playing, game_over
        
        # Game objects
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        # Fonts
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
        self.setup_game()
    
    def setup_game(self):
        """Initialize game objects"""
        # Create player
        self.player = Player(100, SCREEN_HEIGHT - 200)
        self.all_sprites.add(self.player)
        
        # Create platforms
        platforms_data = [
            (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),  # Ground
            (200, SCREEN_HEIGHT - 150, 200, 20),
            (500, SCREEN_HEIGHT - 250, 200, 20),
            (100, SCREEN_HEIGHT - 350, 150, 20),
            (600, SCREEN_HEIGHT - 400, 200, 20),
        ]
        
        for x, y, width, height in platforms_data:
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
        
        # Create enemies
        enemy_positions = [
            (400, SCREEN_HEIGHT - 150),
            (650, SCREEN_HEIGHT - 300),
        ]
        
        for x, y in enemy_positions:
            enemy = Enemy(x, y)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def reset_game(self):
        """Reset game to initial state"""
        self.all_sprites.empty()
        self.platforms.empty()
        self.enemies.empty()
        self.setup_game()
        self.game_state = "playing"
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if self.game_state == "menu":
                    if event.key == pygame.K_SPACE:
                        self.game_state = "playing"
                elif self.game_state == "game_over":
                    if event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = "menu"
                elif self.game_state == "playing":
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    elif event.key == pygame.K_z:
                        self.player.attack()
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = "menu"
    
    def update(self):
        """Update game state"""
        if self.game_state == "playing":
            # Get keys for continuous movement
            keys = pygame.key.get_pressed()
            self.player.update(keys, self.platforms)
            
            # Update enemies
            for enemy in self.enemies:
                enemy.update(self.platforms)
            
            # Check player-enemy collisions
            if self.player.is_attacking:
                hit_enemies = pygame.sprite.spritecollide(
                    self.player, self.enemies, False,
                    pygame.sprite.collide_mask
                )
                for enemy in hit_enemies:
                    if self.player.attack_rect.colliderect(enemy.rect):
                        enemy.take_damage(self.player.attack_damage)
                        if enemy.health <= 0:
                            enemy.kill()
            
            # Check if enemy hits player
            enemy_collisions = pygame.sprite.spritecollide(
                self.player, self.enemies, False
            )
            for enemy in enemy_collisions:
                if not self.player.is_invulnerable():
                    self.player.take_damage(enemy.damage)
                    if self.player.health <= 0:
                        self.game_state = "game_over"
    
    def draw(self):
        """Draw everything"""
        self.screen.fill(BACKGROUND_COLOR)
        
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            self.draw_game()
        elif self.game_state == "game_over":
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw main menu"""
        title = self.font_large.render("Shadow Knight", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(title, title_rect)
        
        instruction = self.font_small.render("Press SPACE to Start", True, WHITE)
        instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(instruction, instruction_rect)
        
        controls = [
            "Controls:",
            "Arrow Keys - Move",
            "SPACE - Jump",
            "Z - Attack",
            "ESC - Menu"
        ]
        
        y_offset = SCREEN_HEIGHT // 2 + 100
        for line in controls:
            text = self.font_small.render(line, True, GRAY)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def draw_game(self):
        """Draw game elements"""
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        
        # Draw health bar
        health_text = self.font_small.render(f"Health: {self.player.health}", True, RED)
        self.screen.blit(health_text, (10, 10))
        
        # Draw health bar
        pygame.draw.rect(self.screen, RED, (10, 50, 200, 20))
        health_width = int((self.player.health / self.player.max_health) * 200)
        pygame.draw.rect(self.screen, GREEN, (10, 50, health_width, 20))
        
        # Draw enemy count
        enemy_text = self.font_small.render(f"Enemies: {len(self.enemies)}", True, WHITE)
        self.screen.blit(enemy_text, (10, 80))
    
    def draw_game_over(self):
        """Draw game over screen"""
        game_over_text = self.font_large.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(game_over_text, game_over_rect)
        
        restart_text = self.font_medium.render("Press R to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(restart_text, restart_rect)
        
        menu_text = self.font_small.render("Press ESC for Menu", True, WHITE)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(menu_text, menu_rect)
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
