import sys 
import pygame
from bullet import Bullet
from Ufo import ufo
from time import sleep

def check_event(ai_setting,screen,Ufos ,ship,bullets,stats,play_button):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            elif event.key == pygame.K_SPACE:
                if len(bullets)<ai_setting.bullets_allowed:#limiting bullts

                    new_bullets=Bullet(ai_setting,screen,ship)
                    bullets.add(new_bullets)
            elif event.key==pygame.K_q:
                sys.exit()
        #this is for checking cursor on play button  
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,ai_setting,screen,Ufos,bullets,ship,play_button,mouse_x,mouse_y)
        


        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False
           # elif event.key == pygame.K_SPACE:
           #     new_bullets=Bullet(ai_setting,screen,ship)
           #     bullets.add(new_bullets)
           
            
def check_play_button(stats,ai_setting,screen,Ufos,bullets,ship,play_button,mouse_x,mouse_y):
    #if play button click then only will active
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initiliaze_dynamic_setting()
    
        #reset game statistics
        stats.reset_stats()
        stats.game_active=True
        Ufos.empty()
        bullets.empty()
        ship.center_ship()


def update_screen(ai_setting,screen,Ufos,ship,bullets,stats,
    play_button,sb):
    screen.fill(ai_setting.bg_color)
    screen.blit(ai_setting.image,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    Ufos.draw(screen)
    #Ufo.blitme()
    sb.show_score()
    if not stats.game_active:
        pygame.image.load('gallery/start.png')

        play_button.draw_button()


    pygame.display.flip()

#this functio is also use for update score when bullet fire 
def update_bullets(ai_setting,screen,ship,sb,stats,bullets,Ufos):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collision=pygame.sprite.groupcollide(bullets,Ufos,True,True)
    if collision:
        stats.score += ai_setting.ufo_points
        sb.prep_score()
    #creating new fleet 
    if len(Ufos)==0:
        bullets.empty()
        ai_setting.increase_speed()
        ai_setting.fleet_drop_speed +=10#increase speed of fleet every loop
        create_fleet(ai_setting,screen,ship,Ufos)


def get_number_ufo_x(ai_setting,ufo_width):
    available_space_x=ai_setting.screen_width - 2*ufo_width
    number_Ufo=int(available_space_x/(2*ufo_width))
    return number_Ufo

def get_number_ufo_y(ai_setting,ship_height,ufo_height):
    available_space_y = (ai_setting.screen_height -

                          (3 * ufo_height) - ship_height)
    number_rows = int(available_space_y / (2 * ufo_height))
    return number_rows

def create_ufo(ai_setting,screen,Ufos,ufo_number,rows_number):
    Ufo=ufo(ai_setting,screen)
    ufo_width=Ufo.rect.width
    Ufo.x=ufo_width +2 * ufo_width *ufo_number
    Ufo.rect.x=Ufo.x
    Ufo.rect.y = Ufo.rect.height + 2 * Ufo.rect.height * rows_number
    Ufos.add(Ufo)





def create_fleet( ai_setting,screen,ship,Ufos):
    Ufo=ufo(ai_setting,screen)
    number_Ufo=get_number_ufo_x(ai_setting,Ufo.rect.width)
    number_rows=get_number_ufo_y(ai_setting,ship.rect.height,Ufo.rect.height)
    for rows_number in range(number_rows):
        for ufo_number in range(number_Ufo):
            create_ufo(ai_setting,screen,Ufos, ufo_number,rows_number)

def check_fleet_edges(ai_setting,Ufos):
    for Ufo in Ufos.sprites():
        if Ufo.check_edges():
            change_fleet_direction(ai_setting,Ufos)
            break

def change_fleet_direction(ai_setting,Ufos):
    for Ufo in Ufos.sprites():
        Ufo.rect.y +=ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def ship_hit(ai_setting,stats,screen,ship,bullets,Ufos):
    if stats.ship_left>0:
        stats.ship_left -= 1
        Ufos.empty()
        bullets.empty()
        create_fleet(ai_setting,screen,ship,Ufos)
        ship.center_ship()

        sleep(0.5)# remain adding image
    else:
        stats.game_active=False
        pygame.image.load('gallery/crash.png')
    
def check_ufo_bottom(ai_setting,stats,screen,ship,bullets,Ufos):
    screen_rect=screen.get_rect()
    for Ufo in Ufos.sprites():
        if Ufo.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_setting,stats,screen,ship,bullets,Ufos)
            break




def update_ufo(ai_setting,Ufos,ship,stats,screen,bullets):
    check_fleet_edges(ai_setting,Ufos)
    Ufos.update()

    if pygame.sprite.spritecollideany(ship,Ufos):
      
       
        ship_hit(ai_setting,stats,screen,ship,bullets,Ufos)
        check_ufo_bottom(ai_setting,stats,screen,ship,bullets,Ufos)


    
   
        




 