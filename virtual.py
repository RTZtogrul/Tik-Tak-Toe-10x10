import pickle

sq = 10

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
    def send_info(user,data):
        user.send(pickle.dumps(data))
    
    
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
            
    
    def start_game(self,user):
        while True:
            pass
    