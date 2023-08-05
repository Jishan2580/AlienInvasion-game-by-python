import pygame
class Settings():
    def __init__(self):
        self.screen_width=1000
        self.screen_height=650
        self.bg_color=(240,140,140)
        self.image=pygame.image.load('gallery/bg_image.jpg')
        self.ship_speed_factor=1.5
        self.bullet_speed=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=240,214,61
        self.bullets_allowed=3
        self.ufo_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        self.ship_limit=2
        self.ufo_points =5
        self.speedup_scale=1.5
        self.initiliaze_dynamic_setting()

    def initiliaze_dynamic_setting(self):

        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale