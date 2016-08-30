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
fig1=(((15,1),(15,0),(14,0),(16,0)),((15,2),(15,1),(14,1),(15,0)),((15,1),(16,1),(14,1),(15,0)),((15,2),(15,1),(16,1),(15,0)))
fig2=(((15,0),(16,0),(17,0),(14,0)),((15,3),(15,2),(15,1),(15,0)),((15,0),(16,0),(17,0),(14,0)),((15,3),(15,2),(15,1),(15,0)))
fig3=(((15,1),(16,1),(15,0),(16,0)),((15,1),(16,1),(15,0),(16,0)),((15,1),(16,1),(15,0),(16,0)),((15,1),(16,1),(15,0),(16,0)))
fig4=(((15,1),(16,1),(14,0),(15,0)),((14,2),(14,1),(15,1),(15,0)),((15,1),(16,1),(14,0),(15,0)),((14,2),(14,1),(15,1),(15,0)))
fig5=(((16,1),(15,0),(14,0),(16,0)),((15,2),(15,1),(15,0),(14,0)),((15,1),(14,1),(16,1),(14,0)),((14,2),(15,2),(15,1),(15,0)))

class Board:
    def checkPiecePos(self,mat,x,y):
        if x>29 or y>31:
            return 0
        else:
            if mat[x][y]==2:
                return 0
            else:
                if y == 31:
                    mat[x][y] = 2
                    return 0
                elif y <= 30  :
                    if mat[x][y+1] == 0:
                        return 1
                    elif mat[x][y+1] == 2:
                        mat[x][y]=2
                        return 0
                    else:
                        return 1
                else:
                    return 0
    def fillPiecePos(self,mat,x,y):
        if self.checkPiecePos(mat,x,y)==1 :
            mat[x][y] = 0
            p=y+1;
            if(p<=30):
                mat[x][p]=1
            elif(p==31):
                mat[x][p]=2


class Block(Board):
    def __init__(self):
        self.hi='hi'
    def block_pick(self):#selsect random block
        a=randint(1,5)
        if a==1:
            return fig1
        elif a==2:
            return fig2
        elif a==3:
            return fig3
        elif a==4:
            return fig4
        elif a==5:
            return fig5

    def draw(self,mat,x1,y1,x2,y2,x3,y3,x4,y4):
        if self.checkPiecePos(mat,x1,y1) == 1 and self.checkPiecePos(mat,x2,y2) == 1 and self.checkPiecePos(mat,x3,y3) == 1and self.checkPiecePos(mat,x4,y4) == 1:
            self.fillPiecePos(mat,x1,y1)
            self.fillPiecePos(mat,x2,y2)
            self.fillPiecePos(mat,x3,y3)
            self.fillPiecePos(mat,x4,y4)
            return 0
        else:
            mat_insh(mat,x1,y1,x2,y2,x3,y3,x4,y4,2)
            if y1<=1 or y2<=1 or y3<=1 or y4<=1:
                return 2
            else:
                return 1
    def moveLeft(self,mat,x1,y1,x2,y2,x3,y3,x4,y4):
        if self.checkPiecePos(mat,x1,y1) == 1 and self.checkPiecePos(mat,x2,y2) == 1 and self.checkPiecePos(mat,x3,y3) == 1and self.checkPiecePos(mat,x4,y4) == 1:
            if mat[x1-1][y1]!=2 and mat[x2-1][y2]!=2 and mat[x3-1][y3]!=2 and mat[x4-1][y4]!=2:
                mat_insh(mat,x1,y1,x2,y2,x3,y3,x4,y4,0)
                mat_insh(mat,x1-1,y1,x2-1,y2,x3-1,y3,x4-1,y4,1)
                return 1
            else:
                return 0
        else:
            return 0
    def moveRight(self,mat,x1,y1,x2,y2,x3,y3,x4,y4):
        if self.checkPiecePos(mat,x1,y1) == 1 and self.checkPiecePos(mat,x2,y2) == 1 and self.checkPiecePos(mat,x3,y3) == 1and self.checkPiecePos(mat,x4,y4) == 1:
            if mat[x1+1][y1]!=2 and mat[x2+1][y2]!=2 and mat[x3+1][y3]!=2 and mat[x4+1][y4]!=2:
                mat_insh(mat,x1,y1,x2,y2,x3,y3,x4,y4,0)
                mat_insh(mat,x1+1,y1,x2+1,y2,x3+1,y3,x4+1,y4,1)
                return 1
            else:
                return 0
        else:
            return 0
    def rotate(self,mat,f,i,X,Y):
        fig=f[i]
        mat_insh(mat,fig[0][0]+X,fig[0][1]+Y,fig[1][0]+X,fig[1][1]+Y,fig[2][0]+X,fig[2][1]+Y,fig[3][0]+X,fig[3][1]+Y,0)
        i=(i+1)%4
        fig=f[i]
        mat_insh(mat,fig[0][0]+X,fig[0][1]+Y,fig[1][0]+X,fig[1][1]+Y,fig[2][0]+X,fig[2][1]+Y,fig[3][0]+X,fig[3][1]+Y,1)
        return f[i]
