import pygame

class Ship():
    def __init__(self,screen,ai_setting):
        self.ai_setting=ai_setting
        self.screen=screen
        self.image=pygame.image.load('gallery/new_ship.bmp')
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)   
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center +=self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -=self.ai_setting.ship_speed_factor
        self.rect.centerx=self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx

