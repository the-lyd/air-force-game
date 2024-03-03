import pygame

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True


player = pygame.image.load("plane.png")

#---------------------------------------------
#2.1 load more images
background = pygame.image.load("sky background.jpg")
cargo = pygame.image.load("blimp.png")
#---------------------------------------------

while keep_going:

    screen.fill(150)
    
    #----------------------------------------
    #2.2 load the background
    screen.blit(background, (width, height))
    # if you image is small, you need use double loop to fill the background
    #for x in range( int(width/background.get_width())+1):
    #    for y in range(int(height/background.get_height())+1):
    #        screen.blit(background,(x*100,y*100))
    
    # 2.3 load the balloon cargo
    screen.blit(cargo,(0,30))
    screen.blit(cargo,(0,135))
    screen.blit(cargo,(0,240))
    screen.blit(cargo,(0,345))
    #----------------------------------------

    screen.blit(player, (130,100))
    
    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going = False

pygame.quit()
exit(0)