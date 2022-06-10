import pygame

pygame.init()


size_block=45
margin = 8
sq = 10
width = height = (sq+1)*margin+sq*size_block



black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
mass = [[0]*sq for i in range(sq)]



size_win = (width,height)
screen= pygame.display.set_mode(size_win)
костыль =str(sq)
костыль2 = костыль+"x"+костыль
pygame.display.set_caption(костыль2)


def check_win_condition(all_lines:list , disc:str)->str:                 
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