import pygame
import os

# Initialize pygame
pygame.init()

# create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon


#backgronud
img_dir = os.path.join('img', 'games', 'pro_football')
bg = os.path.join(img_dir, 'football_bg.png')
background = pygame.image.load(bg)

#functions to create our resources
def load_image(name, colorKey=None):
    fullname = os.path.join(img_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit("Uh oh")
    image = image.convert()
    if colorKey is not None:
        if colorKey == -1:
            colorKey = image.get_at((0,0))
        image.set_colorkey(colorKey, pygame.RLEACCEL)
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    """Player Abe"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call Sprite initializer
        self.image, self.rect = load_image("breakdance.gif", -1)
        self.pos = (0,0)
        self.kicking = 0
        self.move = 9

    def update(self, direction):
        """Move abe based on directional buttons"""
       
        if direction == "left":
            #Move left
            newpos = self.rect.move((-self.move, 0))
            # self.image = pygame.transform.flip(self.image, 1, 0)
        else:
            # move right
            newpos = self.rect.move((self.move, 0))
        self.rect = newpos
    
    def kick(self, target):
        """returns true if the kick connects with the ball"""
        if not self.kicking:
            self.kicking = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.collidrect(target.rect)

def main():
    running = True

    #fisplay the background
    screen.blit(background, (0,0))
    pygame.display.flip()

    #Prepare game objects
    clock = pygame.time.Clock()
    player = Player()
    allsprites = pygame.sprite.RenderPlain((player))

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.update("right")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.update("left")
        
        

        #Draw everything
        screen.blit(background, (0,0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()      

if __name__ == "__main__":
    main()