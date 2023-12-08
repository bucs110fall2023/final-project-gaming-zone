import pygame
class Model:
    def __init__(self):
        self.screen_size = (720,720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.color = (255,255,255) 
        self.button1_light = "darkorchid1" #"deeppink1"
        self.button1_dark = "darkorchid3" #"deeppink3"
        self.width = self.screen.get_width() 
        self.height = self.screen.get_height() 
        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.text = self.smallfont.render('Start Game' , True , self.color)

    def startGame_button (self):
        while True:
            self.screen.fill("orange") 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
      
            if self.width/2.5 <= mouse[0] <= self.width/2.5+180 and self.height/2.5 <= mouse[1] <= self.height/2.5+40: 
                pygame.draw.rect(self.screen,self.button1_light,[self.width/2.5,self.height/2.5,180,40]) 
          
            else: 
                pygame.draw.rect(self.screen,self.button1_dark,[self.width/2.5,self.height/2.5,180,40]) 
      

            self.screen.blit(self.text , (self.width/2.5+15,self.height/2.5-15)) 
    
            pygame.display.update()
      
            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
              
        #checks if a mouse is clicked 
                if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
                    if self.width/2.5 <= mouse[0] <= self.width/2.5+180 and self.height/2.5 <= mouse[1] <= self.height/2.5+40: 
                        pygame.quit()

    







 


  
# screen resolution 

  
# opens up a window 
  
# white color 
  
# light shade of the button 
  
# dark shade of the button 
  
# stores the width of the 
# screen into a variable 
  
# stores the height of the 
# screen into a variable 
  
# defining a font 
  
# rendering a text written in 
# this font 
  
 
                  
    # fills the screen with a color 
    