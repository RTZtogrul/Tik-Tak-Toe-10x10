import pygame , sys



pygame.init()
size_block=45
margin = 8
sq = 10
width = height = (sq+1)*margin+sq*size_block



size_win = (width,height)
screen= pygame.display.set_mode(size_win)


костыль =str(sq)
костыль2 = костыль+"x"+костыль
pygame.display.set_caption(костыль2)


black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

game = True
turn = True
start_turn = turn
game_over = False

def create_emty_mass():
    return [["0"]*sq for i in range(sq)]

mass = create_emty_mass()




def win(all_lines,disc):                 
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



while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
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


