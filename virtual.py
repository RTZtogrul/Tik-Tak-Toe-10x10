import pickle , pygame , sys


pygame.init()


size_block=45
margin = 8
sq = 10
width = height = (sq+1)*margin+sq*size_block
size_win = (width,height)

screen = pygame.display.set_mode(size_win)


black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)



def create_emty_mass():
    return [["0"]*sq for i in range(sq)]


    
class Game:
    player_signs = ["x","o"]
    
    def __init__(self):
        self.mass = create_emty_mass()
        
        
    @staticmethod
    def get_info(user):
        response = user.recv(1024)
        try:
            data = pickle.loads(response)
        except: # какая то рандомная ошибка, хз, но вродь пашет 
            pass
        
        return data
    
    
    @staticmethod
    def get_position():
        x_mouse,y_mouse = pygame.mouse.get_pos()
        col = x_mouse // (size_block+margin)
        row = y_mouse // (size_block+margin)
        return (col,row)
    
    
    @staticmethod
    def send_info(user,data):
        user.send(pickle.dumps(data))
        
    @staticmethod
    def quit_button(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
            
            
    def draw_screen(self):
        screen.fill(white)
        
        
        
        
        
        # for row in range(sq):
        #     for col in range(sq):
        #         if self.mass[row][col] == "x":
        #             color = red
        #         elif self.mass[row][col] == "o":
        #             color = green
        #         else:
        #             color = white
        #         x = col*size_block+(col+1)*margin
        #         y = row*size_block+(row+1)*margin
        #         pygame.draw.rect(screen,color,(x,y,size_block,size_block))
                
                
    def upd_main_mass(self,mass):
        self.mass = mass
        
    
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
            
            
            