# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:26:32 2018

@author: Forestf
"""
import pygame ,sys

from waz import waz

def kolizja(x ,y):
    if x>19 or x<0 or y>19 or y<0 :
        sys.exit(0)
    
pygame.init();
s=pygame.display.set_mode((600, 600));
pygame.display.set_caption('Snake');

jedzenie_img = pygame.Surface((8, 8));
jedzenie_img.fill((255, 0, 0));
glowa_img = pygame.Surface((26, 26));
glowa_img.fill((153, 153 ,0));
ogon_img= pygame.Surface((26,26));
ogon_img.fill((0 ,128 ,0));
clock = pygame.time.Clock()


pyton= waz()

#s.blit(appleimage, 20 , 20);
while True:
    clock.tick(20)
    
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
        
    kolizja(pyton.pozX[0] , pyton.pozY[0])
    s.fill((255, 255, 255))	
    for i in range(len(pyton.pozX)):
        if i==0 :
            s.blit(glowa_img, (2+pyton.pozX[i]*30, 2+pyton.pozY[i]*30));
        else:
           s.blit(ogon_img, (2+pyton.pozX[i]*30, 2+pyton.pozY[i]*30));
            
    
    pygame.display.update()