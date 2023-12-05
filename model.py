import pygame
class model():
    pygame.init() 
  
# screen resolution 
screen_size = (720,720)
  
# opens up a window 
screen = pygame.display.set_mode(screen_size) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
button1_light = "darkorchid1" #"deeppink1"
  
# dark shade of the button 
button1_dark = "darkorchid3" #"deeppink3"
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('Start Game' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2.5 <= mouse[0] <= width/2.5+140 and height/2.5 <= mouse[1] <= height/2.5+40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill("orange") 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2.5 <= mouse[0] <= width/2.5+140 and height/2.5 <= mouse[1] <= height/2.5+40: 
        pygame.draw.rect(screen,button1_light,[width/2.5,height/2.5,140,40]) 
          
    else: 
        pygame.draw.rect(screen,button1_dark,[width/2.5,height/2.5,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2.5+50,height/2.5)) 
      
    # updates the frames of the game 
    pygame.display.update()