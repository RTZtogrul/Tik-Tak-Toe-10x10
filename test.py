import virtual , pygame 

game = virtual.Game()



while True:
    for event in pygame.event.get():
        
        game.quit_button(event)
        
        game.draw_screen()
        
    
        
