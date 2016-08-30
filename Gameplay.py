import pygame,sys,random,time,numpy
from random import randint
from pygame.locals import *
pygame.init()
display_screen = pygame.display.set_mode((300, 360))#320
pygame.display.set_caption('TETRIS')
FONT = pygame.font.SysFont('freesansbold.ttf',40)
SURFACEFONT = FONT.render('', True ,(1,1,1),(100,1,30))
SURFACER = SURFACEFONT.get_rect()
SURFACER.center=(80,340)
# display_screen.fill((100,1,30))
display_screen.blit(SURFACEFONT,SURFACER)
def mat_insh(mat,x1,y1,x2,y2,x3,y3,x4,y4,k):
    mat[x1][y1]=k
    mat[x2][y2]=k
    mat[x3][y3]=k
    mat[x4][y4]=k

class Gameplay:
    def __init__(self,score):
        self.score=score
    def updateScreen(self,mat):
        display_screen.fill((100,1,30))
        for i in range(30):
            for j in range(32):
                if (i+j)%2==0:
                    pygame.draw.rect(display_screen,(50,50,50),Rect((i*10,j*10),(10,10)))
                else:
                    pygame.draw.rect(display_screen,(20,20,20),Rect((i*10,j*10),(10,10)))
                if mat[i][j]==2:
                    pygame.draw.rect(display_screen,(255,255,255),Rect((i*10,j*10),(8,8)))
                elif mat[i][j]==1:
                    pygame.draw.rect(display_screen,(0,100,0),Rect((i*10,j*10),(8,8)))
        self.cheakEmptyrow(mat)
        pygame.display.update()
    def cheakEmptyrow(self,mat):
        for y in range(32):
            flag=1
            for x in range(30):
                if mat[x][y] != 2:
                    flag=0
            if flag == 1:
                self.insertcol(mat,y)
                self.score=90
            else:
                self.score=0
    def insertcol(self,mat,f):
        for a in range(30):
            mat[a][f]=0
        for y in range(f):
            for x in range(30):
                mat[x][f-y]=mat[x][f-1-y]
    def updateScore(self,score):
        SURFACEFONT = FONT.render('SCORE:' + str(score), True ,(255,255,0),(100,1,30))
        display_screen.blit(SURFACEFONT,SURFACER)
        pygame.display.update()

    def updateGover(self,k):
        SURFACEFONT = FONT.render(k, True ,(255,255,0),(100,1,30))
        display_screen.blit(SURFACEFONT,SURFACER)
        pygame.display.update()
