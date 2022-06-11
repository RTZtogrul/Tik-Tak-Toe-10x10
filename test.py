


        
        
while True:
    for event in pygame.event.get():
        
        game.quit_button(event)
        
        game.draw_screen()
        
        game.make_move(event)
        
        game.send_info(user,game.mass)
        
        game.get_info(user)
        
    
        
