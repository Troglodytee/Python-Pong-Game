import pygame
from pygame.locals import *
from random import *

def affich() :
    if ecran == 1 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,800,600))

        myfont = pygame.font.SysFont("Fixedsys",72)
        texte = myfont.render("PONG",False,(0,0,0))
        fenetre.blit(texte,(330,50))

        pygame.draw.rect(fenetre,(0,0,0),(300,250,200,100))
        pygame.draw.rect(fenetre,(255,255,255),(305,255,190,90))
        texte = myfont.render("Jouer",False,(0,0,0))
        fenetre.blit(texte,(330,275))

        myfont = pygame.font.SysFont("Fixedsys",20)
        texte = myfont.render("J1 :",False,(0,0,0))
        fenetre.blit(texte,(10,510))
        myfont = pygame.font.SysFont("Fixedsys",28)
        pygame.draw.rect(fenetre,(0,0,0),(10,560,90,30))
        pygame.draw.rect(fenetre,(255,255,255),(13,563,84,24))
        pygame.draw.rect(fenetre,(0,0,0),(39,531,32,59))
        pygame.draw.rect(fenetre,(255,255,255),(42,534,26,53))
        pygame.draw.rect(fenetre,(0,0,0),(39,560,30,3))
        texte = myfont.render("z",False,(0,0,0))
        fenetre.blit(texte,(50,535))
        texte = myfont.render("q",False,(0,0,0))
        fenetre.blit(texte,(20,565))
        texte = myfont.render("s",False,(0,0,0))
        fenetre.blit(texte,(49,565))
        texte = myfont.render("d",False,(0,0,0))
        fenetre.blit(texte,(78,565))

        myfont = pygame.font.SysFont("Fixedsys",20)
        texte = myfont.render("J2 :",False,(0,0,0))
        fenetre.blit(texte,(700,510))
        myfont = pygame.font.SysFont("Fixedsys",28)
        pygame.draw.rect(fenetre,(0,0,0),(700,560,90,30))
        pygame.draw.rect(fenetre,(255,255,255),(703,563,84,24))
        pygame.draw.rect(fenetre,(0,0,0),(729,531,32,59))
        pygame.draw.rect(fenetre,(255,255,255),(732,534,26,53))
        pygame.draw.rect(fenetre,(0,0,0),(729,560,30,3))
        texte = myfont.render("^",False,(0,0,0))
        fenetre.blit(texte,(740,540))
        texte = myfont.render("<",False,(0,0,0))
        fenetre.blit(texte,(710,565))
        texte = myfont.render("v",False,(0,0,0))
        fenetre.blit(texte,(740,565))
        texte = myfont.render(">",False,(0,0,0))
        fenetre.blit(texte,(770,564))

    elif ecran == 2 or ecran == 3 :
        pygame.draw.rect(fenetre,(0,0,0),(0,0,800,600))
        for i in range (75) :
            if i%2 == 1 :
                pygame.draw.rect(fenetre,(255,255,255),(398,i*8,4,8))
        pygame.draw.rect(fenetre,(255,255,255),(coord[0],coord[1],10,100))
        pygame.draw.rect(fenetre,(255,255,255),(coord[2],coord[3],10,100))
        pygame.draw.rect(fenetre,(255,255,255),(coord_balle[0],coord_balle[1],10,10))

        myfont = pygame.font.SysFont("Fixedsys",80)
        texte = myfont.render(str(score1),False,(255,255,255))
        fenetre.blit(texte,(390-len(str(score1))*30,10))
        myfont = pygame.font.SysFont("Fixedsys",80)
        texte = myfont.render(str(score2),False,(255,255,255))
        fenetre.blit(texte,(410,10))

    pygame.display.flip()

def deplacement_balle() :
    global ecran
    global coord_balle
    global coord
    global score1
    global score2
    global pause
    coord_balle2 = list(coord_balle)
    if coord_balle[2] == 1 :
        coord_balle[0] -= 5
        coord_balle[1] -= 5
    elif coord_balle[2] == 2 :
        coord_balle[0] += 5
        coord_balle[1] -= 5
    elif coord_balle[2] == 3 :
        coord_balle[0] += 5
        coord_balle[1] += 5
    elif coord_balle[2] == 4 :
        coord_balle[0] -= 5
        coord_balle[1] += 5
    if coord_balle[0] == 0 :
        score2 += 1
        ecran = 2
        coord = [20,250,770,250]
        coord_balle = [395,295,randint(1,4)]
        pause = 0
        pygame.key.set_repeat(300,100)
    if coord_balle[0]+10 == 800 :
        score1 += 1
        ecran = 2
        coord = [20,250,770,250]
        coord_balle = [395,295,randint(1,4)]
        pause = 0
        pygame.key.set_repeat(300,100)
    if coord_balle[1] == 0 :
        if coord_balle[2] == 1 :
            coord_balle[2] = 4
        elif coord_balle[2] == 2 :
            coord_balle[2] = 3
    if coord_balle[1]+10 == 600 :
        if coord_balle[2] == 3 :
            coord_balle[2] = 2
        elif coord_balle[2] == 4 :
            coord_balle[2] = 1

    if not test() == 0 :
        if coord_balle[2] == 1 :
            if coord_balle[0] == coord[0]+5 and coord_balle[1] == coord[1]+95 or coord_balle[0] == coord[2]+5 and coord_balle[1] == coord[3]+95 :
                coord_balle[2] = 3
            elif coord_balle[0] == coord[0]+5 or coord_balle[0] == coord[2]+5 :
                coord_balle[2] = 2
            elif coord_balle[1] == coord[1]+95 or coord_balle[1] == coord[3]+95 :
                coord_balle[2] = 4
        elif coord_balle[2] == 2 :
            if coord_balle[0]+10 == coord[0]+5 and coord_balle[1] == coord[1]+95 or coord_balle[0]+10 == coord[2]+5 and coord_balle[1] == coord[3]+95 :
                coord_balle[2] = 4
            elif coord_balle[0]+10 == coord[0]+5 or coord_balle[0]+10 == coord[2]+5 :
                coord_balle[2] = 1
            elif coord_balle[1] == coord[1]+95 or coord_balle[1] == coord[3]+95 :
                coord_balle[2] = 3
        elif coord_balle[2] == 3 :
            if coord_balle[0]+10 == coord[0]+5 and coord_balle[1]+10 == coord[1]+5 or coord_balle[0]+10 == coord[2]+5 and coord_balle[1]+10 == coord[3]+5 :
                coord_balle[2] = 1
            elif coord_balle[0]+10 == coord[0]+5 or coord_balle[0]+10 == coord[2]+5 :
                coord_balle[2] = 4
            elif coord_balle[1]+10 == coord[1]+5 or coord_balle[1]+10 == coord[3]+5 :
                coord_balle[2] = 2
        elif coord_balle[2] == 4 :
            if coord_balle[0] == coord[0]+5 and coord_balle[1]+10 == coord[1]+5 or coord_balle[0] == coord[2]+5 and coord_balle[1]+10 == coord[3]+5 :
                coord_balle[2] = 2
            elif coord_balle[0] == coord[0]+5 or coord_balle[0] == coord[2]+5 :
                coord_balle[2] = 3
            elif coord_balle[1]+10 == coord[1]+5 or coord_balle[1]+10 == coord[3]+5 :
                coord_balle[2] = 1
        coord_balle[0] = coord_balle2[0]
        coord_balle[1] = coord_balle2[1]
        if coord_balle[2] == 1 :
            coord_balle[0] -= 5
            coord_balle[1] -= 5
        elif coord_balle[2] == 2 :
            coord_balle[0] += 5
            coord_balle[1] -= 5
        elif coord_balle[2] == 3 :
            coord_balle[0] += 5
            coord_balle[1] += 5
        elif coord_balle[2] == 4 :
            coord_balle[0] -= 5
            coord_balle[1] += 5

def test() :
    if coord_balle[0] >= coord[0] and coord_balle[0] < coord[0]+10 and coord_balle[1] >= coord[1] and coord_balle[1] < coord[1]+100 :
        return 1
    elif coord_balle[0] >= coord[2] and coord_balle[0] < coord[2]+10 and coord_balle[1] >= coord[3] and coord_balle[1] < coord[3]+100 :
        return 1
    elif coord_balle[0]+10 > coord[0] and coord_balle[0]+10 <= coord[0]+10 and coord_balle[1] >= coord[1] and coord_balle[1] < coord[1]+100 :
        return 2
    elif coord_balle[0]+10 > coord[2] and coord_balle[0]+10 <= coord[2]+10 and coord_balle[1] >= coord[3] and coord_balle[1] < coord[3]+100 :
        return 2
    elif coord_balle[0]+10 > coord[0] and coord_balle[0]+10 <= coord[0]+10 and coord_balle[1]+10 > coord[1] and coord_balle[1]+10 <= coord[1]+100 :
        return 3
    elif coord_balle[0]+10 > coord[2] and coord_balle[0]+10 <= coord[2]+10 and coord_balle[1]+10 > coord[3] and coord_balle[1]+10 <= coord[3]+100 :
        return 3
    elif coord_balle[0] >= coord[0] and coord_balle[0] < coord[0]+10 and coord_balle[1]+10 > coord[1] and coord_balle[1]+10 <= coord[1]+100 :
        return 4
    elif coord_balle[0] >= coord[2] and coord_balle[0] < coord[2]+10 and coord_balle[1]+10 > coord[3] and coord_balle[1]+10 <= coord[3]+100 :
        return 4
    else :
        return 0

pygame.init()

fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")

raccourci = __file__
raccourci = raccourci[0:-8]

icone = pygame.image.load(raccourci+"icone.png")
pygame.display.set_icon(icone)

ecran = 1
obst = 0

affich()

pygame.key.set_repeat(300,100)

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN :
            if ecran == 1 :
                if event.pos[0] > 300 and event.pos[0] < 500 and event.pos[1] > 250 and event.pos[1] < 350 :
                    ecran = 2
                    score1 = 0
                    score2 = 0
                    coord = [20,250,770,250]
                    coord_balle = [395,295,randint(1,4)]
                    pause = 0
                    pygame.key.set_repeat(300,100)

            affich()

        elif event.type == KEYDOWN :
            if ecran == 2 :
                if event.key == K_RETURN :
                    ecran = 3
                    pygame.key.set_repeat(35,35)
                elif event.key == K_ESCAPE :
                    ecran = 1
                    affich()
            elif ecran == 3 :
                if event.key == K_RETURN :
                    if pause == 0 :
                        pause = 1
                        pygame.key.set_repeat(300,100)
                    else :
                        pause = 0
                        pygame.key.set_repeat(35,35)
                elif event.key == K_ESCAPE :
                    ecran = 1
                    affich()
                elif event.key == K_w and coord[1] > 0 and pause == 0 :
                    coord[1] -= 10
                    if not test() == 0 :
                        coord[1] += 10
                elif event.key == K_s and coord[1] < 500 and pause == 0 :
                    coord[1] += 10
                    if not test() == 0 :
                        coord[1] -= 10
                elif event.key == K_a and coord[0] > 20 and pause == 0 :
                    coord[0] -= 10
                    if not test() == 0 :
                        coord[0] += 10
                elif event.key == K_d and coord[0] < 370 and pause == 0 :
                    coord[0] += 10
                    if not test() == 0 :
                        coord[0] -= 10
                elif event.key == K_UP and coord[3] > 0 and pause == 0 :
                    coord[3] -= 10
                    if not test() == 0 :
                        coord[3] += 10
                elif event.key == K_DOWN and coord[3] < 500 and pause == 0 :
                    coord[3] += 10
                    if not test() == 0 :
                        coord[3] -= 10
                elif event.key == K_LEFT and coord[2] > 420 and pause == 0 :
                    coord[2] -= 10
                    if not test() == 0 :
                        coord[2] += 10
                elif event.key == K_RIGHT and coord[2] < 770 and pause == 0 :
                    coord[2] += 10
                    if not test() == 0 :
                        coord[2] -= 10

    if ecran == 3 and pause == 0 :
        a = 15-(score1+score2)
        if a < 7 :
            a = 7
        pygame.time.wait(a)
        deplacement_balle()
        affich()