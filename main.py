# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:26:32 2018

@author: Forestf
"""
import pygame ,sys, random

from waz import waz
from jedzenie import jedzenie

def rysuj():
    for i in range(20):
        for j in range(20):
            if (j+i)%2== 0:
                pygame.draw.rect(s , pygame.Color(176,224,230) , (i*30 ,j*30 ,30 ,30) ,0)
            else:
                pygame.draw.rect(s , pygame.Color(173,216,230) , (i*30 ,j*30 ,30 ,30) ,0)
                
                
    for i in range(len(pyton.pozX)):
        if i==0 :
            s.blit(glowa_img, (2+pyton.pozX[i]*30, 2+pyton.pozY[i]*30));
        else:
           s.blit(ogon_img, (2+pyton.pozX[i]*30, 2+pyton.pozY[i]*30));
           
    for i in zarcie:
        if i.zjedzony:
            s.blit(zjedzone_img ,(2+i.pozX*30 ,2+i.pozY*30))
        else:
             s.blit(jedzenie_img ,(2+i.pozX*30 ,2+i.pozY*30))
             
           
    pygame.draw.line(s ,pygame.Color(0,191,255) ,(0 ,0) ,(0,600) ,2)
    pygame.draw.line(s ,pygame.Color(0,191,255) ,(0 ,0) ,(600,0) ,2)
    pygame.draw.line(s ,pygame.Color(0,191,255) ,(0 ,600) ,(600,600) ,4)
    pygame.draw.line(s ,pygame.Color(0,191,255) ,(600 ,0) ,(600,600) ,4)
    pygame.display.update()
    
    
def kolizja(x ,y, punkty):
    if x>19 or x<0 or y>19 or y<0 :
        smierc(punkty)
        
    for i in range(1,len(waz.pozX)-1):
        if waz.pozX[0]== waz.pozX[i] and waz.pozY[0]== waz.pozY[i]:
            sys.exit(0)
        
def dodaj_jedzenie():
    tempx = random.randint(0 ,19)
    tempy =random.randint(0,19)
    for i in range(len(waz.pozX)):
        if waz.pozX[i]== tempx and waz.pozY[i]== tempy:
            dodaj_jedzenie()
    tempjedzenie = jedzenie(tempx, tempy)
    zarcie.insert(0, tempjedzenie)
    
def smierc(punkty):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
  #  clock2 =pygame.time.Clock()
    waz.zyje=False
    text = myfont.render('Zdobyte punkty: '+str(punkty)+'\n Wcisnij "R" aby zaczac od nowa', False, (0, 0, 0))
    s.blit(text,(200,270))
    pygame.display.update()
    while True:
            for event in pygame.event.get():
                if event.type == pygame.K_R:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
        
    

pygame.init();
s=pygame.display.set_mode((600, 600));
pygame.display.set_caption('Snake');

jedzenie_img = pygame.Surface((26, 26));
jedzenie_img.fill((255, 0, 0));
zjedzone_img=pygame.Surface((26,26));
zjedzone_img.fill((240,128,128));
glowa_img = pygame.Surface((26, 26));
glowa_img.fill((153, 153 ,0));
ogon_img= pygame.Surface((26,26));
ogon_img.fill((0 ,128 ,0));
clock = pygame.time.Clock()

zarcie =[]
pyton= waz()

def main():
    punkty =0
    dodaj_jedzenie()
    
    #s.blit(appleimage, 20 , 20);
    while waz.zyje:
        clock.tick(waz.predkosc)
        #rysuj()
        for e in pygame.event.get():
           # e.type == pygame.QUIT:
    		    # sys.exit(0)
    	    if e.type == pygame.KEYDOWN:
    		    	if e.key == pygame.K_UP and waz.kierunek != 1:waz.kierunek = 3
    		    	elif e.key == pygame.K_DOWN and waz.kierunek != 3:waz.kierunek = 1
    		    	elif e.key == pygame.K_LEFT and waz.kierunek != 2:waz.kierunek = 0
    		    	elif e.key == pygame.K_RIGHT and waz.kierunek != 0:waz.kierunek = 2
                
                
        for i in range(len(pyton.pozX)-1 ,0 ,-1):
            if i==0 :
                break
            pyton.pozX[i]=pyton.pozX[i-1]
            pyton.pozY[i]=pyton.pozY[i-1]
            
            
        if pyton.kierunek==0:
            pyton.pozX[0]-=1
        elif pyton.kierunek ==1:
            pyton.pozY[0]+=1
        elif pyton.kierunek ==2:
            pyton.pozX[0]+=1
        elif pyton.kierunek ==3:
            pyton.pozY[0]-=1
            
        kolizja(pyton.pozX[0] , pyton.pozY[0] , punkty)
        
        if zarcie[0].pozX==waz.pozX[0] and zarcie[0].pozY ==waz.pozY[0]:
            zarcie[0].zjedzony =True
            punkty+=1
            dodaj_jedzenie()
        if zarcie[len(zarcie)-1].pozX==waz.pozX[len(waz.pozX)-1] and zarcie[len(zarcie)-1].pozY ==waz.pozY[len(waz.pozY)-1]:
            waz.pozX.insert(len(waz.pozX)-1 ,zarcie[len(zarcie)-1].pozX)
            waz.pozY.insert(len(waz.pozY)-1 ,zarcie[len(zarcie)-1].pozY)
            zarcie.remove(zarcie[len(zarcie)-1])
            #s.fill((255, 255, 255))	

        rysuj()
main()
    