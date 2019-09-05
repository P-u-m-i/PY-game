import pygame, sys
from random import randint
#import datetime
import datetime
from connector import *

pygame.init()
screen_x = 680
screen_y = 480
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("First Pygame Application")

bg = pygame.image.load("alienbg.jpg")
#bg1 = pygame.transform.scale(bg, (screen_x,screen_y))
inbg = pygame.image.load('inbg.png')
ss2 = pygame.image.load("spacestation.png") 
ss = pygame.image.load('daicazzo.png')
ss1 = pygame.image.load('starsh.png')
ls = pygame.image.load('shot.png')
bgfin = pygame.image.load('bgperfect.png')
heart = pygame.image.load('hearticon3.png')
start_time = 0

a = 0
l = 1
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
myfont4 = pygame.font.SysFont('Comic Sans Ms', 25)

class Entity:
    def __init__ (self,x,y,color,lato):
        self.x = x
        self.y = y
        self.color = color
        self.lato = lato 

    def draw(self):
        for i in char:
            pygame.draw.rect(screen,i.color,(i.x,i.y,i.lato,i.lato))


class Player(Entity):
    def __init__(self,x,y,color,lato):
        super().__init__(x,y,color,lato)
 

class Bullet(Entity):
    def __init__ (self,x,y,start,color,lato):
        self.start = start
        super().__init__(x,y,color,lato)
    
    def move (self):
        screen.blit(ls, (b.start,b.y))
        self.y -= self.lato + 10
        
        if self.y<0:
            self.start = self.x
            self.y = p.y-10
             

class Enemy(Entity):
    def __init__(self,x,y,color,lato):
       super().__init__(x,y,color,lato)

    def move(self):
        screen.blit(ss, (e.x,e.y))
        screen.blit(ss2, (f.x,f.y))
        self.y += 2
        global screen_y
        if self.y > screen_y:
            self.x = randint(0,screen_x - p.lato)
            self.y = 0      
                
class Heart(Entity):
    def __init__(self,x,y,color,lato):  
        super().__init__(x,y,color,lato)        

p = Player((screen_x/2)-20,400,[255,255,255],40)
b = Bullet(p.x+15,p.y-10,p.x+15,[0,255,0],10)
e = Enemy(randint(0,screen_x - p.lato),0,[255,0,0],40)
f = Enemy(randint(0,screen_x - p.lato),0,[255,0,0],40)

h1 = Heart(60,20, [0,0,0], 20)
h2 = Heart(85,20, [0,0,0], 20)
h3 = Heart(110,20, [0,0,0], 20)

inputboxx = screen_x/2 - 180
inputboxy = screen_y/2 - 40
text = ''
done = False
done1 = False
myfont3 = pygame.font.SysFont('Comic Sans Ms', 30)
myfont5 = pygame.font.SysFont('Italics', 30)
lifes = 3
while True:
    
    screen.blit(inbg,(0,0))
    textsurface5 = myfont5.render('Tap Enter to play', False, (255,255,255))
    screen.blit(textsurface5, (250, 420))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done1= True
    
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()            
   
    while done1:
        screen.blit(bgfin,(0,0))
        textsurface3 = myfont3.render('Username: ' , True, (255,255,0))
        screen.blit(textsurface3 ,(screen_x/2 - 180, screen_y/2 - 80))
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(text)
                    done = True
                    start_time = datetime.datetime.now()
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            

        textsurface4 = myfont4.render( text, False, (255,255,255))
        screen.blit(textsurface4 ,(inputboxx + 5, inputboxy + 10))
        clock = pygame.time.Clock()
        clock.tick(60)
        pygame.display.update()

        while done: 

            screen.fill([0,0,0])
            screen.blit(bg,(0,0))
            elapsed_time = datetime.datetime.now() - start_time

            textsurface = myfont.render('uccisioni = ' + str(a), False, (200, 0, 0))
            textsurface1 = myfont.render('tempo = ' + str(elapsed_time), False, (200, 0, 0))
            textsurface2 = myfont.render('level: ' + str(l), False, (200, 0, 0))
            textsurface7 = myfont.render('lifes: ', False, (0,255,255))
            #textsurface8 = myfont.render('var: ' + str(lifes), False, (255,255,255))
            screen.blit(textsurface,(0,screen_y - 30))
            screen.blit(textsurface1,(200,screen_y - 30))
            screen.blit(textsurface2,(600,screen_y - 30))
            screen.blit(textsurface7, (5,15))
            screen.blit(heart,(h1.x,h1.y))
            screen.blit(heart,(h2.x,h2.y))
            screen.blit(heart,(h3.x,h3.y))
            screen.blit(ss, (e.x,e.y))
            screen.blit(ss2, (f.x,f.y))
            screen.blit(ss1, (p.x, p.y))
            #screen.blit(textsurface8, (600,20))
                        
            b.move()
            f.move()
            e.move()
            
            if b.y <= e.y + e.lato and b.start >= e.x and b.start < e.x + e.lato:
                    
                    e.x = randint(0,screen_x - p.lato)
                    e.y = 0
                    a += 1
            if b.y <= f.y + f.lato and b.start >= f.x and b.start < f.x + f.lato:
                    
                    f.x = randint(0,screen_x - p.lato)
                    f.y = 0
                    a += 1

            if e.y == screen_y or f.y == screen_y:
                lifes -=1
            if lifes == 2:
                h3.x=h2.x
                h3.y=h2.y

            if lifes ==1:
                h3.x=h1.x
                h3.y=h1.y
                h2.x=h1.x
                h2.y=h1.y

            if lifes <= 0:
                screen.blit(bgfin,(0,0))
                myfont6= pygame.font.SysFont('Double Struck', 100)
                textsurface6 = myfont6.render('GAME OVER!', True, (255,0,0) )
                screen.blit(textsurface6,(120, screen_y/2-50))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                        
                        if event.type == pygame.KEYDOWN:
                            sys.exit()    
                    
                    
            for event in pygame.event.get():
                
                if a >= 5 and a <= 9:
                    l = 2
                    e.y += 6
                    b.y -= 3
                    bg= pygame.image.load('back4.jpg')
                    ss = pygame.image.load('ss3.png')
                    ss2 = pygame.image.load('ss4.png')
                '''if a >= 10 and a <= 14:
                    l = 3
                    e.y += 6
                    f.y += 6
                    b.y -=6'''

                if a >= 15:
                    l = 4
                    e.y += 12
                    f.y += 12
                    b.y -=12
                    bg= pygame.image.load('back3.png')
                    ss = pygame.image.load('ss5.png')
                    ss2 = pygame.image.load('ss6.png')
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        b.y -= p.lato
                        p.y -= p.lato                                     
                        screen.blit(ss1, (p.x,p.y))
                        
                    if event.key == pygame.K_s and p.y < 480-p.lato:
                        b.y += p.lato
                        p.y += p.lato                        
                        screen.blit(ss1, (p.x,p.y))
                        
                    if event.key == pygame.K_a and p.x > 0:
                        b.x -= p.lato
                        p.x -= p.lato                        
                        screen.blit(ss1, (p.x,p.y))
                        
                    if event.key == pygame.K_d and p.x+p.lato < screen_x:
                        b.x += p.lato
                        p.x += p.lato                        
                        screen.blit(ss1, (p.x,p.y))
                        
                  
            clock = pygame.time.Clock()
            clock.tick(60)
            pygame.display.update()