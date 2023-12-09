import pygame
class Model:
    screen_size = (720,720)
    screen = pygame.display.set_mode(screen_size)
    def __init__(self):
        pygame.init()
        self.screen_size = (720,720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill("orange")
        self.smallfont = pygame.font.Font(None,35)
        self.color = (255,255,255) 
        self.button1_light = "darkorchid1" 
        self.button2_light = "deeppink1"
        self.button1_dark = "darkorchid3" 
        self.button2_dark = "deeppink3"
        self.width = self.screen.get_width() 
        self.height = self.screen.get_height()

    def start_game_button (self, light_color, dark_color, fav_pos = 0, text = "Start Game"):
        self.text = self.smallfont.render(text , True , self.color)
        self.light_color = light_color
        self.dark_color = dark_color
        self.fav_pos = fav_pos
        mouse = pygame.mouse.get_pos() 

        if self.width/2.5 <= mouse[0] <= self.width/2.5+180 and self.height/2.5 + fav_pos <= mouse[1] <= self.height/2.5 + fav_pos +40: 
            pygame.draw.rect(self.screen, light_color ,[self.width/2.5 ,self.height/2.5 + fav_pos ,180,40]) 
          
        else: 
            pygame.draw.rect(self.screen, dark_color,[self.width/2.5 ,self.height/2.5 + fav_pos,180,40]) 
      

        self.screen.blit(self.text , (self.width/2.5+15,self.height/2.5 + fav_pos)) 
        pygame.display.update()
      
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                return False
              
        #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
                if self.width/2.5 <= mouse[0] <= self.width/2.5+180 and self.height/2.5 + fav_pos <= mouse[1] <= self.height/2.5+40 + fav_pos: 
                    pygame.quit()
                    return False
        return True\
        
    def __init__(self):
        self.grid = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player_turn = 'X'
        self.winner = None
    def make_move(self, rows, columns):
        if self.grid[rows][columns] == '' and not self.winner:
            self.grid[rows][columns] = self.player_turn
            self.check_winner()
            self.switch_player()
    def check_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] !='':
                self.winner = self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] !='':
                self.winner = self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != '':
            self.winner = self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != '':
            self.winner = self.grid[0][2]
    def switch_player(self):
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'
    def is_grid_full(self):
        for row in self.grid:
            if '' in row:
                return False
                return True
    def reset_game(self):
        self.grid = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player_turn = 'X'
        self.winner = None

    def draw_grid(self, model):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.border_color, (i * self.width// 3, 0), (i * self.width // 3, self.height), self.border_width)
            pygame.draw.line(self.screen, self.border_color, (0, i *self.height // 3), (self.width, i * self.height // 3),self.border_width)
            for rows in range(3):
                for column in range(3):
                    if model.grid[rows][column] == 'X':
                        x_pos = column * self.width // 3 + self.width // 6
                        y_pos = rows * self.height // 3 + self.height // 6
                        pygame.draw.line(self.screen, self.border_color, (x_pos - 50, y_pos - 50), (x_pos + 50, y_pos + 50),self.border_width)
                        pygame.draw.line(self.screen, self.border_color, (x_pos+ 50, y_pos - 50), (x_pos - 50, y_pos + 50),self.border_width)
                    elif model.grid[rows][column] == 'O':
                        x_pos = column * self.width// 3 + self.width// 6
                        y_pos = rows * self.height // 3 + self.height // 6
                        pygame.draw.circle(self.screen, self.border_color,(x_pos, y_pos), 50, self.border_width)
