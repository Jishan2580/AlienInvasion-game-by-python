
import pygame
from settings import Settings
from ship import Ship  
import game_function as gf
from pygame.sprite import Group
from Ufo import ufo
from game_stats import game_statistics
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_setting=Settings()
    background=pygame.image.load('gallery/bg_image.jpg')
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    stats=game_statistics(ai_setting)
    ship=Ship(screen,ai_setting)
    bullets=Group()
    Ufos=Group()
    sb=Scoreboard(ai_setting,screen,stats)

    #Ufo=ufo(ai_setting,screen)
    gf.create_fleet(ai_setting,screen,ship,Ufos)
    messege=pygame.image.load('gallery/crash.png')
    play_button=Button(ai_setting,screen,'play')
    while True:
        
        gf.check_event(ai_setting,screen,Ufos, ship,bullets,stats,play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting,screen,ship,sb,stats ,bullets,Ufos)   
            gf.update_ufo(ai_setting ,Ufos,ship,stats,screen,bullets)
        gf.update_screen(ai_setting, screen,Ufos,ship,bullets,stats,
            play_button,sb)
       

            


        
       

run_game()
