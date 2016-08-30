import pygame,sys,random,time,numpy
from random import randint
from pygame.locals import *
import Gameplay
import Block
pygame.init()
display_screen = pygame.display.set_mode((300, 360))#320
pygame.display.set_caption('TETRIS')
FONT = pygame.font.SysFont('freesansbold.ttf',40)
SURFACEFONT = FONT.render('', True ,(1,1,1),(100,1,30))
SURFACER = SURFACEFONT.get_rect()
SURFACER.center=(80,340)
# display_screen.fill((100,1,30))
display_screen.blit(SURFACEFONT,SURFACER)
score = 0
creat_block=1
My_time=.1
gameover=0
mat = [[0 for x in range(32)] for y in range(30)]

def mat_insh(mat,x1,y1,x2,y2,x3,y3,x4,y4,k):
    mat[x1][y1]=k
    mat[x2][y2]=k
    mat[x3][y3]=k
    mat[x4][y4]=k
game = Gameplay.Gameplay(0)
TOTAL=game.score
block = Block.Block()
no_block=0
while True:
    # print TOTAL
    game.updateScreen(mat)
    game.updateScore(TOTAL)
    TOTAL = game.score+TOTAL
    time.sleep(My_time)
    if creat_block == 1:
        no_block=no_block+1
        if no_block%10==0:
            h=no_block/10
            k=str(h)
            game.updateGover('LEVEL : '+ k)
            time.sleep(1)
        con=2
        digram = block.block_pick()
        fig=digram[2]
        My_time=.1
        creat_block=0
        center_posY=0
        center_posX=0
# tag_poi(fig)# x1=fig[0][0]# y1=fig[0][1]# x2=fig[1][0]# y2=fig[1][1]# x3=fig[2][0]# y3=fig[2][1]# x4=fig[3][0]# y4=fig[3][1]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if fig[0][0]+center_posX>0 and fig[1][0]+center_posX>0 and fig[2][0]+center_posX>0 and fig[3][0]+center_posX>0 :
                    if block.moveLeft(mat,fig[0][0]+center_posX,fig[0][1]+center_posY,fig[1][0]+center_posX,fig[1][1]+center_posY,fig[2][0]+center_posX,fig[2][1]+center_posY,fig[3][0]+center_posX,fig[3][1]+center_posY)==1:
                        center_posX=center_posX-1
            if event.key == pygame.K_d:
                if fig[0][0]+center_posX<29 and fig[1][0]+center_posX<29 and fig[2][0]+center_posX<29 and fig[3][0]+center_posX<29 :
                    if block.moveRight(mat,fig[0][0]+center_posX,fig[0][1]+center_posY,fig[1][0]+center_posX,fig[1][1]+center_posY,fig[2][0]+center_posX,fig[2][1]+center_posY,fig[3][0]+center_posX,fig[3][1]+center_posY)==1:
                        center_posX=center_posX+1
            if event.key == pygame.K_SPACE:
                My_time=.01
            if event.key == pygame.K_s:
                fig=block.rotate(mat,digram,con,center_posX,center_posY)
                con=(con+1)%4
    creat_block = block.draw(mat,fig[0][0]+center_posX,fig[0][1]+center_posY,fig[1][0]+center_posX,fig[1][1]+center_posY,fig[2][0]+center_posX,fig[2][1]+center_posY,fig[3][0]+center_posX,fig[3][1]+center_posY)
    if creat_block==1:
        TOTAL=TOTAL+10
    if creat_block==2:
        # print "game over"
        k="GAME OVER"
        game.updateGover(k)
        time.sleep(1)
        k="!!!!BYE BYE!!!!"
        game.updateGover(k)
        time.sleep(1)
        break
    center_posY=center_posY+1
