import socket
import virtual
import pygame

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",1234))


game = virtual.Game("x")


while True:
    for event in pygame.event.get():
        
        game.quit_button(event)
        
        game.draw_screen()
        
        game.make_move(event)
        
        game.send_info(client,game.mass)
        
        game.get_info(client)
        
       

    
    
    
    
    