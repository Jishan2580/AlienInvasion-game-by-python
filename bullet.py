import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_setting.bullet_color
        self.speed=ai_setting.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
