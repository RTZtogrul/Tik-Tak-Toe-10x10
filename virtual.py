import pickle , pygame , sys
from typing import NamedTuple



pygame.init()


size_block=45
margin = 8
sq = 10
padding = 0
width = height = (sq+1)*margin+sq*size_block
size_win = (width,height+padding)



black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)



def create_emty_mass():
    return [["0"]*sq for i in range(sq)]


    
class Pos(NamedTuple):
    col: int
    row: int
    
    
class Game:
    player_signs = ["x","o"]
    screen = pygame.display.set_mode(size_win)
    turn : bool
    mass : list
    
    
    def __init__(self,sign,user):
        self.sign = sign
        self.user = user
        if sign == "x":
            self.turn = True
            self.mass = create_emty_mass()
        if sign == "o":
            self.turn = False

        
    def get_info(self):
        response = self.user.recv(1024)
        try:
            data = pickle.loads(response)
        except: # какая то рандомная ошибка, хз, но вродь пашет 
            pass
        
        self.upd_main_mass(data)
        self.turn = True
        

    
    
    @staticmethod
    def get_position():
        x_mouse,y_mouse = pygame.mouse.get_pos()
        col = x_mouse // (size_block+margin)
        row = y_mouse // (size_block+margin)
        
        pos = Pos(col,row)
        return pos
    
    
    def send_info(self, data):
        self.user.send(pickle.dumps(data))
        
        
    @staticmethod
    def quit_button(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
            
    def make_move(self , event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.turn:
            pos = self.get_position()
                
            if self.is_free(pos.col,pos.row):
                self.move(pos.col,pos.row)
                self.turn = False
                self.draw_screen()
                    
         
            
    def is_free(self,col,row):
        if self.mass[row][col] == "0":
            return True
        else:
            return False
            
            
    def move(self,col,row):
        if self.sign in self.player_signs and self.mass[row][col] == "0":
            self.mass[row][col] = self.sign
            return False
        else:
            return True
            
            
            
    def draw_screen(self):
        for row in range(sq):
            for col in range(sq):
                if self.mass[row][col] == "x":
                    color = red
                elif self.mass[row][col] == "o":
                    color = green
                else:
                    color = white
                x = col*size_block+(col+1)*margin
                y = padding + row*size_block+(row+1)*margin
                pygame.draw.rect(self.screen,color,(x,y,size_block,size_block))
        pygame.display.update()
        
              
                
    def upd_main_mass(self,mass):
        self.mass = mass
        self.draw_screen()
        
    
    def check_win_condition(self)->str: 
        all_lines = self.mass
                      
        for disc in self.player_signs:                
            for c in range(sq): #horizontal
                for r in range(sq):
                    try:
                        if all_lines[r][c] ==all_lines[r][c+1] == all_lines[r][c+2] == all_lines[r][c+3] ==  all_lines[r][c+4] == disc:
                            return disc
                    except:
                        pass

            for c in range(sq): #diagonals
                for r in range(sq):
                    try:
                        if all_lines[r][c] == all_lines[r+1][c+1] == all_lines[r+2][c+2] == all_lines[r+3][c+3] == all_lines[r+4][c+4] == disc :
                            return disc
                    except:
                        pass
            for c in range(sq):
                for r in range(sq):
                    try:
                        if all_lines[r][c] == all_lines[r-1][c+1] == all_lines[r-2][c+2] == all_lines[r-3][c+3]== all_lines[r-4][c+4] == disc:
                            return disc
                    except:
                        pass

            for c in range(sq): #vertical
                for r in range(sq):
                    try:
                        if all_lines[r][c] ==  all_lines[r+1][c] == all_lines[r+2][c] == all_lines[r+3][c] == all_lines[r+4][c]== disc :
                            return disc
                    except:
                        pass
            
            
            