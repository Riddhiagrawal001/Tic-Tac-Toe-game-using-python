import pygame,sys
import numpy as np

pygame.init()

width=600
height=600
line_width=15
board_rows=3
board_cols=3
circle_radius=60
circle_width=15
cross_width=25
space=55
# colors are in rgb format : red blue green
red=(255,0,0)
bg_color=(28,170,156)
line_color=(23,145,135)
circle_color=(239,231,200)
cross_color=(66,66,66)

screen= pygame.display.set_mode((width,height) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

#console board
board=np.zeros((board_rows,board_cols))


def draw_lines():
    #1st horizontal
    pygame.draw.line(screen ,line_color,(0,200),(600,200),line_width)
    #2nd horizontal
    pygame.draw.line(screen ,line_color,(0,400),(600,400),line_width)

    #1st vertical
    pygame.draw.line(screen ,line_color,(200,0),(200,600),line_width)
    #2nd vertical
    pygame.draw.line(screen ,line_color ,(400,0),(400,600),line_width)

def draw_figures():
    for rows in range(board_rows):
        for cols in range(board_cols):
            if board[rows][cols]==1:
                pygame.draw.circle(screen,circle_color,(int(cols * 200 + 100),int (rows * 200 + 100)),circle_radius,circle_width)
            elif board[rows][cols]==2:
                pygame.draw.line(screen ,cross_color ,(cols * 200 + space ,rows * 200 + 200 - space ),(cols * 200 + 200 - space ,rows * 200 + space ),cross_width)
                pygame.draw.line(screen ,cross_color ,(cols * 200 + space ,rows * 200 + space ),(cols * 200 + 200 - space ,rows * 200 + 200 - space ),cross_width)


def mark_squares(row,col,player):
    board[row][col]=player

def available_square(row,col):
    return board[row][col]==0

def is_board_full():
   for row in range(board_rows):
      for col in range(board_cols):
          if board[row][col]==0:
              return False
   return True

def check_win(player):
    #vertical win check
    for col in range(board_cols):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col,player)
            return True
    # horizontal win check
    for row in range(board_rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    #ascending win check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_ascending_winning_line(player)
        return True
    # descending win check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_descending_winning_line(player)
        return True
    return False

def draw_vertical_winning_line(col,player):
    pos_x=col * 200 + 100

    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen ,color,(pos_x,15),(pos_x,height-15),15)

def draw_horizontal_winning_line(row,player):
    pos_y=row * 200 + 100

    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen ,color,(15,pos_y),(width - 15 , 15 ),15)

def draw_ascending_winning_line(player):
        if player==1:
            color=circle_color
        elif player==2:
            color=cross_color
        pygame.draw.line(screen ,color,(15,height - 15 ),(width - 15 , 15 ),15)

def draw_descending_winning_line(player):
        if player==1:
            color=circle_color
        elif player==2:
            color=cross_color
        pygame.draw.line(screen ,color,(15,15),(width - 15 ,height - 15 ),15)

def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col]=0

draw_lines()

player=1
game_over=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:

            mouse_x=event.pos[0] # x co-ordinate
            mouse_y=event.pos[1] # y co-ordiante

            clicked_row=int(mouse_y//200)
            clicked_col=int(mouse_x//200)

            if available_square(clicked_row,clicked_col):
                if player == 1 :
                    mark_squares(clicked_row,clicked_col,1)
                    if check_win(player):
                         game_over=True
                    player=2

                elif player ==2:
                    mark_squares(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over=True
                    player=1

                draw_figures()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                 restart()
                 player=1
                 game_over=False

    pygame.display.update()
