import pygame
import sys
pygame.init()


pygame.display.set_caption("AmongUsJump")



#Klassen ----------------------------------------

class spieler(object):
    
 
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.stand = True 
        
    def walk(self,win): 
            
        if self.walkcount +1 >= 32:
           self.walkcount = 0
       
        if not (self.stand):
            if self.left:
                     win.blit(walkLeft[self.walkcount//10], (self.x, self.y))
                     self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount//10], (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                      win.blit(walkRight[0], (self.x,self.y))
            else:
                      win.blit(walkLeft[0], (self.x,self.y))
                     
#Konfig-----------------------------------

## Bilder
walkRight = [pygame.image.load('pg5.xcf'), pygame.image.load('pg6.xcf'),pygame.image.load('pg7.xcf'),pygame.image.load('pg8.xcf')]
walkLeft = [pygame.image.load('pg1.xcf'), pygame.image.load('pg2.xcf'),pygame.image.load('pg3.xcf'),pygame.image.load('pg9.xcf')]
bg = pygame.image.load('background.xcf')
char = pygame.image.load('pg4.xcf')
ground_image=pygame.image.load('boden.png')



clock = pygame.time.Clock()


##Screengröße
screenSize= (800,600) 
screenWidth = 800
win = pygame.display.set_mode(screenSize,0, 32)

##Surface größe
TILE_SIZE = ground_image.get_width()
display = pygame.Surface((700,600))

##Spieler
am_us_blau = spieler(50, 400, 64, 64)
isJump  = False
jumpcount = 10

#Map erstellen

##Maptxt = "Map.txt"
#Maptxt = open('Map.txt','r')
#for row in Maptxt:
   #game_map = Maptxt.readline()
   
game_map = [['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]
                     
    
#Funktion-------------------------

def quit_game():
     sys.exit()
     

def redrawGameWindow():
    am_us_blau.walk(win)
    pygame.display.update()    



def placeblocks():  
    tile_rects = []  
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
           if tile == '1':
                display.blit(ground_image, (x * TILE_SIZE, y * TILE_SIZE))
           if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
           x += 1
    
        y += 1



def move_player():
    keys = pygame.key.get_pressed()
    
   
    if keys[pygame.K_LEFT] and am_us_blau.x > am_us_blau.vel:
        am_us_blau.x -= am_us_blau.vel
        am_us_blau.left = True
        am_us_blau.right = False
        am_us_blau.stand = False # Setzet False wenn er läuft
    elif keys[pygame.K_RIGHT] and am_us_blau.x < screenWidth - am_us_blau.width - am_us_blau.vel:
           am_us_blau.x += am_us_blau.vel
           am_us_blau.right = True
           am_us_blau.left = False
           am_us_blau.stand = False
    else:
        
        am_us_blau.stand = True 
        am_us_blau.walkcount = 0
        
    if not (am_us_blau.isJump):
      
        if keys[pygame.K_UP]:   # spring funktion
            am_us_blau.isJump = True
            am_us_blau.right = False
            am_us_blau.left = False
            am_us_blau.walkcount = 0
    else:
        if am_us_blau.jumpcount >= -10:
            neg = 1
            if am_us_blau.jumpcount < 0:
                neg = -1
            am_us_blau.y -= (am_us_blau.jumpcount ** 2) * 0.5 * neg
            am_us_blau.jumpcount -= 1
            
        else:
            am_us_blau.isJump = False
            am_us_blau.jumpcount = 10





#Schleifen-Beginn -------------------------
while True:
    clock.tick(32) 
    display.blit(bg,(0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
     
        
    placeblocks() 
    move_player() # Ruft die Funktion auf | Keys (links,rechts,Springen)

            
        
    surf = pygame.transform.scale(display, screenSize)
    win.blit(surf, (0, 0))
    redrawGameWindow()
    
    
    
pygame.quit()

