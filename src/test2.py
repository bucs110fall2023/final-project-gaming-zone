import pygame
pygame.init()
screen_size = (720,720)
screen = pygame.display.set_mode(screen_size)
screen_size = (720,720)
screen = pygame.display.set_mode(screen_size)
color = (255,255,255) 
button1_light = "darkorchid1" #"deeppink1"
button1_dark = "darkorchid3" #"deeppink3"
width = screen.get_width() 
height = screen.get_height() 
smallfont = pygame.font.Font(None,35) 
text = smallfont.render('Start Game' , True , color)

while True:
    screen.fill("orange") 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    if width/2.5 <= mouse[0] <= width/2.5+180 and height/2.5 <= mouse[1] <= height/2.5+40: 
        pygame.draw.rect(screen,button1_light,[width/2.5,height/2.5,180,40]) 
          
    else: 
        pygame.draw.rect(screen,button1_dark,[width/2.5,height/2.5,180,40]) 
      

        screen.blit(text , (width/2.5+15,height/2.5-15)) 
    
        pygame.display.update()
      
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                    pygame.quit() 
              
        #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
                if width/2.5 <= mouse[0] <= width/2.5+180 and height/2.5 <= mouse[1] <= height/2.5+40: 
                    pygame.quit()