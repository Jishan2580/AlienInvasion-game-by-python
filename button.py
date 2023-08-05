import pygame.font

class Button():
    def __init__(self,ai_setting,screen,msg):
        #initiliaze screen attribute
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #set dimension and properties of button 
        self.width,self.height=300,50
        self.buton_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,58)

        #build button rect object
        self.rect= pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.buton_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center


    def draw_button(self):

        #draw blank button and then messege
        self.screen.fill(self.buton_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)



        