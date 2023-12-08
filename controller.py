import pygame
from model import Model
class Controller:
    def __init__(self):
        self.event = 0
    def mainloop(self):
        while True: #this can also be a variable instead of just True
        #1. Handle events
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   exit()   
    
    def startMenu(self):
        self.screen_size = (720,720)
        self.screen = pygame.display.set_mode(self.screen_size)
        Model.startGame_button()
       
        #2. detect collisions and update models

        #3. Redraw next frame

        #4. Display next frame
        pygame.display.flip()
        
Controller()