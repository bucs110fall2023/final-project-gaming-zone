import pygame
from model import Model
class Controller:
    def __init__(self):
        self.event = 0
        self.screen_size = (720,720)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Tic Tac Toe")
        self.LINE_COLOR = "purple"
        self.instructions_font = pygame.font.Font(None,40)

    def mainloop(self):
        while True: #this can also be a variable instead of just True
        #1. Handle events
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   exit()   

    def display_instructions(self):
        instructions = [
            "Tic Tac Toe Instructions:",
            "1. Players take turns to place their 'X' or 'O' on the board.",
            "2. The first player to get three in a row (horizontally, vertically, or diagonally) wins.",
            "3. If the board is full and no player has won, the game is a draw.",
            "4. Click 'Start New Game' to reset the board and start a new game.",
            "5. Have fun!"
            ]
        for i, line in enumerate(instructions):
            text = self.instructions_font.render(line, True, self.LINE_COLOR)
            self.screen.blit(text, (20, 20 + i * 25))

    
    def startmenu(self):
        pygame.init()
        self.smallfont = pygame.font.Font(None,50)
        self.text = self.smallfont.render('Tic Tac Toe' , True , "black")
        self.screen.blit(self.text , (720/2.4,720/4)) 
        game = Model()
        button1 = game.start_game_button("darkorchid1" , "darkorchid3", 0)
        button2 = game.start_game_button("deeppink1" , "deeppink3", 50, "Information")
        running = True
        while running:
    
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if button1.is_clicked(mouse):
                        running = False
                        choose_player()
                        pygame.display.flip()
                    elif button2.is_clicked(mouse):
                        pygame.display.flip()
                        Controller.display_instructions()
                        pass

        pygame.display.flip()
    def tic_tac_toe(self):
        Model.draw_grid()
        
    pygame.quit()

    



        
controller = Controller()
controller.startmenu()
controller.mainloop()
