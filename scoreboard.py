import pygame.font


class Scoreboard():
    def __init__(self,ai_setting,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_setting=ai_setting
        self.stats=stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,30)
        self.prep_score()

    def prep_score(self):
        score_str=str(self.stats.score)#here dont use self. because we have to convert and store score in it 
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right - 20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
