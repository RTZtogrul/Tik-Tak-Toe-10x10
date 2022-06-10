import socket
import virtual
import pygame,sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
server.listen(1)

user , adress = server.accept()

game = virtual.Game()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col , row = game.get_position()
            if turn and mass[row][col] == "0" :
                mass[row][col] = "x"
                turn = not turn
            elif mass[row][col] == "0" and not turn:
                mass[row][col] = "o"
                turn = not turn
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(black)
            game_over =False
            mass = create_emty_mass()
            turn = start_turn
            start_turn = not start_turn

    
    if not game_over:
        for row in range(sq):
            for col in range(sq):
                if mass [row][col] == "x":
                    color = red
                elif mass [row][col] == "o":
                    color = green
                else:
                    color = white
                x = col*size_block+(col+1)*margin
                y = row*size_block+(row+1)*margin
                pygame.draw.rect(screen,color,(x,y,size_block,size_block))
        

    if not turn:
        game_over = win(mass,"x")

    else:
        game_over = win(mass,"o")


    if game_over:
        screen.fill(black)
        font= pygame.font.SysFont("stxinqkai", 100, bold=True, italic=False)
        text1 = font.render(game_over,True,white)
        text_rect = text1.get_rect()
        text_x = screen.get_width()/2-text_rect.width /2
        text_y = screen.get_width()/2-text_rect.height /2
        screen.blit(text1,[text_x,text_y])
        game_over = not game_over

    pygame.display.update()




    
    
       
    

