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
                
                
    for i in range(len(python.pozX)):
        if i==0 :
            s.blit(glowa_img, (2+python.pozX[i]*30, 2+python.pozY[i]*30));
        else:
           s.blit(ogon_img, (2+python.pozX[i]*30, 2+python.pozY[i]*30));
           
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
        
    for i in range(1,len(python.pozX)-1):
        if python.pozX[0]== python.pozX[i] and python.pozY[0]== python.pozY[i]:
            smierc(punkty)
        
def dodaj_jedzenie():
    tempx = random.randint(0 ,19)
    tempy =random.randint(0,19)
    for i in range(len(python.pozX)):
        if python.pozX[i]== tempx and python.pozY[i]== tempy:
            dodaj_jedzenie()
            return
    tempjedzenie = jedzenie(tempx, tempy)
    zarcie.insert(0, tempjedzenie)
    
def smierc(punkty):
    #myfont = pygame.font.SysFont('Comic Sans MS', 30)
    myfont = pygame.font.Font(pygame.font.get_default_font(), 24)
  #  clock2 =pygame.time.Clock()
    #python.zyje=False
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
python= waz()

def main():
    punkty =0
    dodaj_jedzenie()
    python.pozX=[10 ,9 ,8]
    python.pozY=[10 ,10 ,10]
    python.kierunek=2
    python.predkosc=3
    #s.blit(appleimage, 20 , 20);
    while python.zyje:
        clock.tick(python.predkosc)
        #rysuj()
        for e in pygame.event.get():
           # e.type == pygame.QUIT:
    		    # sys.exit(0)
    	    if e.type == pygame.KEYDOWN:
    		    	if e.key == pygame.K_UP and python.kierunek != 1:python.kierunek = 3
    		    	elif e.key == pygame.K_DOWN and python.kierunek != 3:python.kierunek = 1
    		    	elif e.key == pygame.K_LEFT and python.kierunek != 2:python.kierunek = 0
    		    	elif e.key == pygame.K_RIGHT and python.kierunek != 0:python.kierunek = 2
                
                
        for i in range(len(python.pozX)-1 ,0 ,-1):
            if i==0 :
                break
            python.pozX[i]=python.pozX[i-1]
            python.pozY[i]=python.pozY[i-1]
            
            
        if python.kierunek==0:
            python.pozX[0]-=1
        elif python.kierunek ==1:
            python.pozY[0]+=1
        elif python.kierunek ==2:
            python.pozX[0]+=1
        elif python.kierunek ==3:
            python.pozY[0]-=1
            
        kolizja(python.pozX[0] , python.pozY[0] , punkty)
        
        if zarcie[0].pozX==python.pozX[0] and zarcie[0].pozY ==python.pozY[0]:
            zarcie[0].zjedzony =True
            punkty+=1
            if python.predkosc<10:
                python.predkosc+=0.5
            dodaj_jedzenie()
        if zarcie[-1].pozX==python.pozX[-1] and zarcie[-1].pozY ==python.pozY[-1]:
            python.pozX.insert(-1 ,zarcie[-1].pozX)
            python.pozY.insert(-1 ,zarcie[-1].pozY)
            zarcie.remove(zarcie[-1])
            #s.fill((255, 255, 255))	

        rysuj(punkty)
main()
    
