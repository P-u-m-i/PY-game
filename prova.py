import pygame, sys
from random import randint
import datetime
from connector import *

pygame.init()
screen_x = 680
screen_y = 480
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("First Pygame Application")

bg = pygame.image.load("./images/alienbg.jpg")
inbg = pygame.image.load('./images/inbg.png')
ss2 = pygame.image.load("./images/spacestation.png") 
ss = pygame.image.load('./images/daicazzo.png')
ss1 = pygame.image.load('./images/starship1.png')
ls = pygame.image.load('./images/shot.png')
bgfin = pygame.image.load('./images/bgperfect.png')
heart = pygame.image.load('./images/hearticon3.png')
start_time = 0

a = 0
l = 1
lifes = 3

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
myfont4 = pygame.font.SysFont('Comic Sans Ms', 25)


mycursor.execute("SELECT MAX(Score) FROM Users")
valmax = mycursor.fetchall()
maxx = list(valmax[0])
if maxx[0] == None :
    maxx = str(0)

    


   
def db():
    sql = "INSERT INTO Users (Username, Level, Score, Gametime ) VALUES (%s, %s, %s, %s)"
    val = [text, l, a, elapsed_time ]
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")     

    
    
    

class Entity:
    def __init__ (self,x,y,color,lato):
        self.x = x
        self.y = y
        self.color = color
        self.lato = lato 

class Player(Entity):
    def __init__(self,x,y,color,lato):
        super().__init__(x,y,color,lato)

    def move(self):
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    b.y -= self.lato
                    self.y -= self.lato                                                         
                if event.key == pygame.K_s and self.y < 480-self.lato:
                    b.y += self.lato
                    self.y += self.lato                        
                if event.key == pygame.K_a and self.x > 0:
                    b.x -= self.lato
                    self.x -= self.lato                        
                if event.key == pygame.K_d and self.x+self.lato < screen_x:
                    b.x += self.lato
                    self.x += self.lato                                       
            

class Bullet(Entity):
    def __init__ (self,x,y,start,color,lato):
        self.start = start
        super().__init__(x,y,color,lato)
    
    def move (self):
        self.y -= self.lato + 10
        
        if self.y<0:
            self.start = self.x
            self.y = p.y-10
             

class Enemy(Entity):
    def __init__(self,x,y,color,lato):
       super().__init__(x,y,color,lato)

    def move(self):
        global lifes

        self.y += 2
        if self.y >= screen_y:
            self.x = randint(0,screen_x - p.lato)
            self.y = 0      
            lifes -=1                    
                            
        '''if lifes == 3:
            screen.blit(heart,(h1.x,h1.y))
            screen.blit(heart,(h2.x,h2.y))
            screen.blit(heart,(h3.x,h3.y))
        if lifes == 2:
            screen.blit(heart,(h1.x,h1.y))
            screen.blit(heart,(h2.x,h2.y))

        if lifes ==1:
            screen.blit(heart,(h1.x,h1.y))
        
        if lifes <= 0:
            
               

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    db()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    db()
                    sys.exit()'''

def gameOver():
    screen.blit(bgfin,(0,0))
    myfont6= pygame.font.SysFont('Double Struck', 100)
    textsurface6 = myfont6.render('GAME OVER!', True, (255,0,0) )
    screen.blit(textsurface6,(120, screen_y/2-50))


def vita(n):
    if n == 0:
        gameOver()
    for i in range(0,n):
        screen.blit(heart,(i*25+60,20))
        
def init():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()   

def scritte():
    textsurface = myfont.render('Score: ' + str(a), False, (200, 0, 0))
    textsurface1 = myfont.render('Time: ' + str(elapsed_time), False, (200, 0, 0))
    textsurface2 = myfont.render('Level: ' + str(l), False, (200, 0, 0))
    textsurface7 = myfont.render('Lifes: ', False, (0,255,255))
    textsurface9 = myfont.render('Score Record: ' + str(maxx[0]), False, (255,255,0))

    screen.blit(textsurface,(0,screen_y - 30))
    screen.blit(textsurface1,(200,screen_y - 30))
    screen.blit(textsurface2,(600,screen_y - 30))
    screen.blit(textsurface7, (5,15))
    screen.blit(textsurface9, (500,15))   
       

p = Player((screen_x/2)-20,400,[255,255,255],40)
b = Bullet(p.x+15,p.y-10,p.x+15,[0,255,0],10)
e = Enemy(randint(0,screen_x - p.lato),0,[255,0,0],40)
f = Enemy(randint(0,screen_x - p.lato),0,[255,0,0],40)



inputboxx = screen_x/2 - 180
inputboxy = screen_y/2 - 40
text = ''
done = False
done1 = False
myfont3 = pygame.font.SysFont('Comic Sans Ms', 30)
myfont5 = pygame.font.SysFont('Italics', 30)

while True:
    init()
    screen.blit(inbg,(0,0))
    textsurface5 = myfont5.render('Tap Enter to play', False, (255,255,255))
    screen.blit(textsurface5, (250, 420))
    for event in pygame.event.get():   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done1= True
    while done1:
        init()
        screen.blit(bgfin,(0,0))
        textsurface3 = myfont3.render('Username: ' , True, (255,255,0))
        screen.blit(textsurface3 ,(screen_x/2 - 180, screen_y/2 - 80))
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    start_time = datetime.datetime.now()
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            

        textsurface4 = myfont4.render( text, False, (255,255,255))
        screen.blit(textsurface4 ,(inputboxx + 5, inputboxy + 10))

        while done: 
            init()

            screen.fill([0,0,0])
            screen.blit(bg,(0,0))
            screen.blit(ss, (e.x,e.y))
            screen.blit(ss2, (f.x,f.y))
            screen.blit(ss1, (p.x, p.y))
            screen.blit(ls, (b.start,b.y))

            elapsed_time = datetime.datetime.now() - start_time

            scritte()            
            
            vita(lifes) 

            p.move()
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
            
            if a >= 5 and a <= 9:
                l = 2
                e.y += 2
                f.y += 2
                b.y -= 2
                bg= pygame.image.load('./images/back4.jpg')
                ss = pygame.image.load('./images/ss3.png')
                ss2 = pygame.image.load('./images/ss4.png')
            if a >= 10 and a <= 14:
                l = 3
                e.y += 4
                f.y += 4
                b.y -= 4
                bg= pygame.image.load('./images/space7.png')
                ss = pygame.image.load('./images/enemy.png')
                ss2 = pygame.image.load('./images/starship2.png')
            if a >= 15 and a <= 20:
                l = 4
                e.y += 6
                f.y += 6
                b.y -= 6
                bg= pygame.image.load('./images/space2.png')
                ss = pygame.image.load('./images/ss5.png')
                ss2 = pygame.image.load('./images/ss6.png')         

            if a >= 21 :
                l = 5
                e.y += 8
                f.y += 8
                b.y -= 8
                bg= pygame.image.load('./images/back3.png')
                ss = pygame.image.load('./images/starsh.png')
                ss2 = pygame.image.load('./images/starship3.png')     
                

