# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:26:32 2018

@author: Forestf
"""
import pygame ,sys, random

from waz import waz
from jedzenie import jedzenie

def rysuj(punkty):
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
    text = fontscore.render('Punkty: '+str(punkty), False , (0,0,0))
    s.blit(text,(5,5))
    pygame.display.update()
    
    
def kolizja(x ,y, punkty):
    if x>19 or x<0 or y>19 or y<0 :
        smierc(punkty)
        
    for i in range(1,len(pyton.pozX)-1):
        if pyton.pozX[0]== pyton.pozX[i] and pyton.pozY[0]== pyton.pozY[i]:
            smierc(punkty)
        
def dodaj_jedzenie():
    tempx = random.randint(0 ,19)
    tempy =random.randint(0,19)
    for i in range(len(pyton.pozX)):
        if pyton.pozX[i]== tempx and pyton.pozY[i]== tempy:
            dodaj_jedzenie()
            return
    tempjedzenie = jedzenie(tempx, tempy)
    zarcie.insert(0, tempjedzenie)
    
def smierc(punkty):
    #myfont = pygame.font.SysFont('Comic Sans MS', 30)
    myfont = pygame.font.Font(pygame.font.get_default_font(), 24)
  #  clock2 =pygame.time.Clock()
    #pyton.zyje=False
    text = myfont.render('Zdobyte punkty: '+str(punkty), False, (0, 0, 0))
    text2 = myfont.render(' Wcisnij "R" aby zaczac od nowa' , False , (0,0,0))
    s.blit(text,(200,240))
    s.blit(text2, (120, 270))
    pygame.display.update()
    #klikniety = True
    while True:
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_r:
                   zarcie.clear()
                   main()
                   #klikniety=False
                   return
               else:    #return
                    pygame.quit()
                    sys.exit()
   
    #pygame.display.update()
        
    

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
fontscore = pygame.font.Font(pygame.font.get_default_font(), 16)

zarcie =[]
pyton= waz()

def main():
    punkty =0
    dodaj_jedzenie()
    pyton.pozX=[10 ,9 ,8]
    pyton.pozY=[10 ,10 ,10]
    pyton.kierunek=2
    pyton.predkosc=3
    #s.blit(appleimage, 20 , 20);
    while pyton.zyje:
        clock.tick(pyton.predkosc)
        #rysuj()
        for e in pygame.event.get():
           # e.type == pygame.QUIT:
    		    # sys.exit(0)
    	    if e.type == pygame.KEYDOWN:
    		    	if e.key == pygame.K_UP and pyton.kierunek != 1:pyton.kierunek = 3
    		    	elif e.key == pygame.K_DOWN and pyton.kierunek != 3:pyton.kierunek = 1
    		    	elif e.key == pygame.K_LEFT and pyton.kierunek != 2:pyton.kierunek = 0
    		    	elif e.key == pygame.K_RIGHT and pyton.kierunek != 0:pyton.kierunek = 2
                
                
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
        
        if zarcie[0].pozX==pyton.pozX[0] and zarcie[0].pozY ==pyton.pozY[0]:
            zarcie[0].zjedzony =True
            punkty+=1
            if pyton.predkosc<10:
                pyton.predkosc+=0.5
            dodaj_jedzenie()
        if zarcie[-1].pozX==pyton.pozX[-1] and zarcie[-1].pozY ==pyton.pozY[-1]:
            pyton.pozX.insert(-1 ,zarcie[-1].pozX)
            pyton.pozY.insert(-1 ,zarcie[-1].pozY)
            zarcie.remove(zarcie[-1])
            #s.fill((255, 255, 255))	

        rysuj(punkty)
main()
    