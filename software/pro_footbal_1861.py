import math
from random import randint
from math import e
import pygame
import os


# Initialize pygame
pygame.init()

# create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

WINNING_SCORE = 333

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

class Computer(pygame.sprite.Sprite):
    """CPU Abe"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.base_image, self.base_rect = load_image("AbeLCbase.png", -1)
        self.image, self.rect = load_image("AbeLCbase.png", -1)
        self.throw_img, self.throw_img_rect = load_image('AbeLCthrow.png', -1)
        self.look_up_img, self.look_up_rect = load_image('AbeLCscore.png', -1)
        self.pos = (100, 50)
        self.throw = 0
        self.move = 9
        self.holding_ball = 1
        self.rect = self.rect.move((SCREEN_WIDTH - self.rect.w, 50))
        self.score = 0

    def clear(self):
        self.base_image, self.base_rect = load_image("AbeLCbase.png", -1)
        self.image, self.rect = load_image("AbeLCbase.png", -1)
        self.throw_img, self.throw_img_rect = load_image('AbeLCthrow.png', -1)
        self.look_up_img, self.look_up_rect = load_image('AbeLCscore.png', -1)
        self.pos = (100, 50)
        self.throw = 0
        self.move = 9
        self.holding_ball = 1
        self.rect = self.rect.move((SCREEN_WIDTH - self.rect.w, 50))

    def update(self, ball):
        """Move cpu abe"""

        if self.throw == 0:
            self.pace(ball)
        else:
            self.throw_ball(ball)
            self.holding_ball = 0

    def pace(self, ball):
        direction = randint(-1, 1)
        move = 0
        new_pos = self.rect.move((0, 0))
        if direction == -1: #move left
            new_pos = self.rect.move((-self.move, 0))
            move = -self.move
        elif direction == 1:
            new_pos = self.rect.move((self.move, 0))
            move = self.move
        self.rect = new_pos
        ball.update(move)

    def throw_ball(self, ball):
        """Throw the ball"""
        self.image = self.throw_img
        screen.blit(self.image, self.rect)
        ball.thrown = 1
    
    def look_up(self):
        """Look up"""
        self.image = self.look_up_img
        screen.blit(self.image, self.rect)

    def add_score(self):
        self.score += 33

class Player(pygame.sprite.Sprite):
    """Player Abe"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call Sprite initializer
        self.image, self.rect = load_image("AbeLbase_cropped.png", -1)
        self.default = self.image
        self.default_rect = self.rect
        self.kick_img, self.kick_rect = load_image('AbeLkick_cropped.png', -1)
        self.pos = (50,100)
        self.kicking = 0
        self.move = 9
        self.rect = self.rect.move((50,93))
        self.score = 0

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
            self.image = self.kick_img
            screen.blit(self.image, self.rect)
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)
    
    def add_score(self):
        self.score += 33

class Ball(pygame.sprite.Sprite):
    """The Ball"""

    def __init__(self) -> None:
        super().__init__()
        self.image, self.rect = load_image("ball_cropped.png", -1)
        self.kicked = 0
        self.thrown = 0
        self.rect = self.rect.move((SCREEN_WIDTH - self.rect.w - 150, 130))
        self.move = 5

    def update(self, pos):
        self.rect = self.rect.move((pos, 0))

    def fall_ball(self):
        #ball uses [bell curve formula] for it's arc
        const1 = 1.8
        const2 = 3.3
        b = -0.6
        u = 1.6
        # y = const1 + (const2 * (1/b * math.sqrt(2 * math.pi) * e**(-0.5**((self.rect.x - u)/b)**2 )))
        
        y = 1/1 + (e**-self.move)
        new_pos = self.rect.move((-self.move, y))
        self.rect = new_pos
        # print(self.rect.x, self.rect.y)

    def hit(self):
        self.thrown = 0
        self.kicked = 1
        y = 1/1 + (e**-self.move)
        new_pos = self.rect.move((self.move, -y))
        self.rect = new_pos

def has_won(abe):
    if abe.score >= WINNING_SCORE:
        return True
    return False

def resetComputer(computer, ball):
    ball.__init__()
    computer.clear()
    screen.blit(computer.image, computer.rect)
    print("reset")

def main():
    running = True

    #display the background
    screen.blit(background, (0,0))
    pygame.display.flip()

    #Prepare game objects
    clock = pygame.time.Clock()
    player = Player()
    computer = Computer()
    ball = Ball()
    allsprites = pygame.sprite.RenderPlain((player, computer, ball))
    kick_timeout = 0
    move_timeout = 0
    throw_timer = 0
    hit = False
    debug_mode = False
    debug_count = 0

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.update("right")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.update("left")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hit = player.kick(ball)
                kick_timeout = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                resetComputer(computer, ball)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                debug_mode = not debug_mode 
            #Debug mode stuff
            elif debug_mode and event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                if debug_count == 0:
                    print('computer')
                    print(computer.__dict__)
                elif debug_count == 1:
                    print('ball')
                    print(ball.__dict__)
                elif debug_count == 2:
                    print('player')
                    print(player.__dict__)
                debug_count = (debug_count + 1) % 3
        
        if hit:
            ball.hit()

        #Computer movement
        move_timeout += 1
        if computer.holding_ball == 1:
            if move_timeout % 20 == 0:
                computer.update(ball=ball)

            throw_timer += 1
            if throw_timer % 100 == 0:
                computer.throw = 1

        if ball.thrown == 1:
            ball.fall_ball()

        if (ball.rect.y > SCREEN_HEIGHT or ball.rect.x < 0) or (ball.rect.y < 0 or ball.rect.x > SCREEN_WIDTH):
            if (ball.rect.y > SCREEN_HEIGHT or ball.rect.x < 0):
                computer.add_score()
            else:
                player.add_score()

            print(player.score, computer.score)
            if has_won(player):
                print("Woo! Player won")
                break
            elif has_won(computer):
                print("Computer won. Woo!")
                break

            ball.thrown = 0
            hit = False
            resetComputer(computer, ball)

        #computer look up
        if ball.kicked == 1 and ball.rect.x >= computer.rect.x + 50:
            computer.look_up()

        kick_timeout += 1
        if kick_timeout % 60 == 0:
            player.kicking = 0
            player.image = player.default

        #Draw everything
        screen.blit(background, (0,0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()      

if __name__ == "__main__":
    main()