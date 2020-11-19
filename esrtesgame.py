import pygame
pygame.init()

win = pygame.display.set_mode((600,480))


walkRight = [pygame.image.load('pg5.xcf'), pygame.image.load('pg6.xcf'),pygame.image.load('pg7.xcf'),pygame.image.load('pg8.xcf')]
walkLeft = [pygame.image.load('pg1.xcf'), pygame.image.load('pg2.xcf'),pygame.image.load('pg3.xcf'),pygame.image.load('pg4.xcf'),pygame.image.load('pg9.xcf')]
bg = pygame.image.load('background.xcf')
char = pygame.image.load('pg5.xcf')


clock = pygame.time.Clock()

screenWitdh = 600
pygame.display.set_caption("Erstes Spiel")
x = 10
y = 400
witdh = 64
height = 64
vel = 10
left = False
right = False
walkcount = 0

isJump  = False
jumpcount = 10

#Display neu zeichnen 
def redrawGameWindow():
     global walkcount
     win.blit(bg, (0,0)) #Hintergtund einfügen
     # pygame.draw.rect(win,  (255, 0, 0), (x, y, witdh, height))
     
     if walkcount +1 >= 27:
       walkcount = 0
       
     if left:
             win.blit(walkLeft[walkcount//10], (x, y))
             walkcount += 1
     elif right:
             win.blit(walkRight[walkcount//10], (x, y))
             walkcount += 1
     else:
         win.blit(char, (x, y))
    
        
     pygame.display.update()    
            


#Main()
run = True
while run:
    clock.tick(32)
    #pygame.time.delay(50) # Framerate
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWitdh - witdh - vel:
            x += vel
            right = True
            left = False
    else:
        right = False
        left = False
        walkcount = 0
        
    if not (isJump):
        #if keys[pygame.K_UP] and y  >  vel:
          #  y -= vel
        
       # if keys[pygame.K_DOWN] and y < screenWitdh - height - vel:
          #  y += vel
        
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkcount = 0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
            
        else:
            isJump = False
            jumpcount = 10
            
    redrawGameWindow()
    
    
pygame.quit()