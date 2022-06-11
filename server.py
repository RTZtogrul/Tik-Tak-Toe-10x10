import socket
import virtual
import pygame


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
server.listen(1)

user , adress = server.accept()


game = virtual.Game("o")


while True:
    for event in pygame.event.get():
        
        game.quit_button(event)
        
        game.draw_screen()
        
        game.make_move(event)
        
        game.send_info(user,game.mass)
        
        game.get_info(user)
        
       
    

