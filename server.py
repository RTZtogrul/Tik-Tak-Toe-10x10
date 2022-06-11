import socket
import virtual
import pygame


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
server.listen(1)

user , adress = server.accept()


game = virtual.Game("o",user)


while True:
    for event in pygame.event.get():
        
        game.quit_button(event)
        
        game.get_info()
        
        game.make_move(event)
        
        game.send_info(game.mass)
        
       
    

