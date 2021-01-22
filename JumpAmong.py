import pygame, sys # import pygame and sys
from os import path #aktiviert Pfad 


clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygame modules
pygame.init() # initiate pygame
pygame.mixer.init()

#MUSIK wird INITIALISIERT-----------------------------------------------------
music = path.join(path.dirname(__file__), 'Music')#Musik einschalten
jumpsound = pygame.mixer.Sound(path.join(music,'Jump.wav'))



#BILDSCHIRM GRÖßEN ------------------------------------------------------------------------------------
pygame.display.set_caption('AmongJump') # set the window name

SCREEN_SIZE = 800
WINDOW_SIZE = (SCREEN_SIZE,600) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

display = pygame.Surface((300, 200))
bg = pygame.image.load('Grafiken/bg2.png')
bg_rect= bg.get_rect()


#IMAGES--------------------------------------------------------------------------------------------------
player_image = pygame.image.load('Grafiken/tenor-0.png').convert()
player_image.set_alpha(250)
player_image.set_colorkey((0,0,0))


laufen_rechts = [pygame.image.load('Grafiken/tenor-0.png'), pygame.image.load('Grafiken/tenor-1.png'),pygame.image.load('Grafiken/tenor-2.png'),pygame.image.load('Grafiken/tenor-3.png'),pygame.image.load('Grafiken/tenor-4.png')]
laufen_links = [pygame.image.load('Grafiken/tenor-5.png'), pygame.image.load('Grafiken/tenor-6.png'),pygame.image.load('Grafiken/tenor-7.png'),pygame.image.load('Grafiken/tenor-8.png'),pygame.image.load('Grafiken/tenor-9.png')]
lauf_zaehler = 0


#GEGNER-------------------------------------------------------------------------------------------------

class Gegner():
    def __init__(self, x, y, geschw, breite,hoehe,richtg,xMin,xMax):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.height = hoehe
        self.richtg= richtg
        self.laufen_rechts= 0
        self.laufen_links= 0
        self.xMin = xMin
        self.xMax= xMax
        self.gegner_rechts = [pygame.image.load('Grafiken/gegner-00.png'), pygame.image.load('Grafiken/gegner-01.png'),pygame.image.load('Grafiken/gegner-02.png'),pygame.image.load('Grafiken/gegner-03.png'),pygame.image.load('Grafiken/gegner-04.png'),pygame.image.load('Grafiken/gegner-05.png')]
        self.gegner_links =  [pygame.image.load('Grafiken/gegner-06.png'), pygame.image.load('Grafiken/gegner-07.png'),pygame.image.load('Grafiken/gegner-08.png'),pygame.image.load('Grafiken/gegner-09.png'),pygame.image.load('Grafiken/gegner-10.png'),pygame.image.load('Grafiken/gegner-11.png')]
        
        
    def draw_gegner(self):
        if self.laufen_rechts == 10:
            self.laufen_rechts = 0
        if self.laufen_links == 10:
            self.laufen_links  = 0
            
            
        if self.richtg[0]:
            screen.blit(self.gegner_links[self.laufen_links//8], (self.x,self.y))
        if self.richtg[1]:
            screen.blit(self.gegner_rechts[self.laufen_rechts//8], (self.x,self.y))
            
    
    def Laufen(self):
         self.x += self.geschw
         if self.geschw > 0:
            self.richtg = [0,1]
            self.laufen_rechts += 1
         if self.geschw < 0:
            self.richtg = [1,0]
            self.laufen_links += 1
            
    def hinHer(self):
        if self.x > self.xMax:
            self.geschw *= -1
        elif self.x < self.xMin:
            self.geschw *= -1
        self.Laufen()
        
        
        
    
#Animation------------------------------------------------------------------------------------------------
def Gegner_zeichen():
    gegner1.draw_gegner()
    gegner1.hinHer()
    
    gegner2.draw_gegner()
    gegner2.hinHer()
    

def updatePlayerImage(direction):
    global lauf_zaehler, laufen_links, laufen_rechts

    if lauf_zaehler >= 32:
        lauf_zaehler = 0

    if direction == 'left':
        player_image = laufen_links[lauf_zaehler//10]#pygame.image.load(laufen_links[lauf_zaehler//10]).convert()
        player_image.set_alpha(250)
        player_image.set_colorkey((0, 0, 0))
        lauf_zaehler += 1
    elif direction == 'right':
        player_image = laufen_rechts[lauf_zaehler//10]#pygame.image.load(laufen_rechts[lauf_zaehler//10]).convert()
        player_image.set_alpha(250)
        player_image.set_colorkey((0, 0, 0))
        lauf_zaehler += 1
    else:
        lauf_zaehler = 0
        player_image = pygame.image.load('Grafiken/tenor-0.png')


    return player_image


player_image = updatePlayerImage(None)


#----------MAP------------------------------------------------------------------------------------------------------
flur_image = pygame.image.load('Grafiken/flur.png')
tile_size = flur_image.get_width()

boden_image = pygame.image.load('Grafiken/erde.png')

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','2','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]





#COLLISON------------------------------------------------------------------------------------------------
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


#BEWEGEN----------------------------------------------------------------------------------------------
def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types



    
    
    

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
gegner1= Gegner(600,355,4,100,100,[0,0],300,750) #x, y, geschw, breite,hoehe,richtg,xMin,xMax
gegner2=Gegner(500,195,2,100,100,[0,0],330,500) #x, y, geschw, breite,hoehe,richtg,xMin,xMax


#MUSIK--------------------------------------------------------------------------------------------
pygame.mixer.music.load(path.join(music,'song1.mp3'))#Aufruf der Datei
pygame.mixer.music.set_volume(0.4) #Volumen Musik
pygame.mixer.music.play(loops = -1)# Musik wird immer Wiederholt




#MENUE-----------------------------------------------------------
def draw_text(display,text,size,x,y):
    text_rect = text_display.get_rect()
    text_rect.midtop = (x,y)
    display.blit(text_rect)

def main_screen(display):
    background = pygame.image.load('Grafiken/bg2.png')
    background_rect= background.get_rect()
    display.blit(background,background_rect)
    draw_text(display,"JumpAmong",220,screen.width /2 , screen.hight /4)
    draw_text(display,"Press Enter to Start",70,screen.width /2 , screen.hight /2 +200)
    draw_text(display,"Arrow keys to Move and KeyUp to JUMP",30,screen.width /2 , screen.hight -100)
    pygame.display.flip()
    wait = True
    clock = pygame.time.Clock()
    
    while wait:
        clock.tick(120)
        for ecent in pygame.event.get():
            if event.type == pygame.QUIT():
                pygame.quit()
            if event.type== pygame.KEYDOWN:
                if event.type== pygame.K_RETURN:
                    wait=False
    
#MAIN------------------------------------------------------------------------------------------------------------------------
while True: # game loop
    display.blit(bg,bg_rect) #Hintergrund einspielem
    
    
   
    
   
    
    

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(boden_image, (x * tile_size, y * tile_size))
            if tile == '2':
                display.blit(flur_image, (x * tile_size, y * tile_size))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1
        y += 1


    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
        player_image = updatePlayerImage('right')
    elif moving_left:
        player_movement[0] -= 2
        player_image = updatePlayerImage('left')
    else:
        player_image = updatePlayerImage(None)
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3


    player_rect, collisions = move(player_rect, player_movement, tile_rects)  #Rect wird intialisiert

    if collisions['bottom']:
        player_y_momentum = -1
        air_timer = 0
    else:
        air_timer += 1

    display.blit(player_image, (player_rect.x, player_rect.y))

    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
            
            
#-KEYS----------------------------------------------------------------------------       
        if event.type == KEYDOWN:
            if event.key == K_RIGHT: 
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:      
                if air_timer < 6:
                    player_y_momentum = -5
                    jumpsound.play()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            
                
              

  
    
# BILDSCHIRM AUSGABE-------------------------------------------------------------------
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    Gegner_zeichen()
   
   
    pygame.display.update() # update display
    pygame.display.flip()
    clock.tick(60) # maintain 60 fps