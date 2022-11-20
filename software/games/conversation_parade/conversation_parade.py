import speech_recognition as sr
import os
import time
import pygame


# Initialize pygame
pygame.init()

#crete the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Title and icon

#background
bg = os.path.join('img', 'cp_bg.png')
mic = os.path.join('img', 'mic_scaled.png')
blue_bg = os.path.join('img', 'blue_bg.png')
background = pygame.image.load(bg)
mic_image = pygame.image.load(mic)
blue_background = pygame.image.load(blue_bg)
question_img_name = ["q1.png", "q2.png", "q3.png", "q4.png", "q5.png", "q6.png", "q7.png", "q8.png", "q9.png", "q10.png"]

def load_image(name, color_key=None, ret_surf=False):
    full_path = os.path.join('img', name)
    try:
        image = pygame.image.load(full_path)
    except pygame.error:
        print("Cannot load image:", full_path)
        raise SystemExit("Uh oh")

    if ret_surf:
        return image
    image = image.convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0,0))
        image.set_colorkey(color_key, pygame.RLEACCEL)
    return image, image.get_rect()

class Balloon(pygame.sprite.Sprite):
    """The Balloons"""

    def __init__(self, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        # cols = ['red', 'green', 'orange', 'yellow']
        self.img_path = ''
        self.pos = (0,0)
        self.color = color
        self.move = 5

        if self.color == 'red':
            self.img_path = "balloon_r.png"
            self.pos = (10, 480)
        elif self.color == 'yellow':
            self.img_path = "balloon_y.png"
            self.pos = (200, 550)
        elif self.color == 'orange':
            self.img_path = "balloon_o.png"
            self.pos = (600, 500)
        elif self.color == 'green':
             self.img_path = "balloon_g.png"
             self.pos = (400, 600)

        self.image, self.rect = load_image(self.img_path, -1)
        self.rect = self.rect.move(self.pos)

    
    def update(self):
        self.rect = self.rect.move((0, -self.move))

        if self.color == "green":
            if self.rect.y <= 30:
                self.image, _ = load_image("balloon_g_pop.png", -1)

        if self.rect.y < -self.rect.height:
            self.__init__(self.color)



#audio
def load_sound(name):
    audio_dir = os.path.join('audio', name)
    return pygame.mixer.Sound(audio_dir)

question = load_sound("question.wav")
response = load_sound("response.wav")

def get_response():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        print("You said " + r.recognize_google(audio))
        # screen.blit(background, (0,0))
        # pygame.display.update()
        pygame.mixer.Sound.play(response)
        # time.sleep(10)
        # os.system("shutdown /s /t 1")
    except LookupError:
        print("Could not understand audio")
    except Exception:
        print("something went wrong!")

def main():
    running = True
    asked = False
    answered = False
    start_mic = False
    q_image = None

    #display the background
    screen.blit(background, (0,0))
    pygame.display.update()

    clock = pygame.time.Clock()

    #initialize balloons
    red_balloon = Balloon("red")
    yellow_balloon = Balloon("yellow")
    green_balloon = Balloon("green")
    orange_balloon = Balloon("orange")
    allsprites = pygame.sprite.RenderPlain((red_balloon, yellow_balloon, green_balloon, orange_balloon))

    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = True
                running = False
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                start = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                start_mic = True

        #play video or audio with animation
        if asked == False:
            asked = True
            #ask the question
            pygame.mixer.Sound.play(question)
            start_ticks = pygame.time.get_ticks()

        screen.blit(blue_background, (0,0))
        red_balloon.update()
        green_balloon.update()
        yellow_balloon.update()
        orange_balloon.update()

        if start_ticks and not start_mic:
            seconds = (pygame.time.get_ticks()-start_ticks)/1000
            #show text
            if seconds < 0.7:
                q_image = load_image(question_img_name[0], -1, True)
            elif seconds > 0.7 and seconds < 1.1:
                q_image = load_image(question_img_name[1], -1, True)
            elif seconds > 1.1 and seconds < 1.5:
                q_image = load_image(question_img_name[2], -1, True)
            elif seconds > 1.5 and seconds < 2:
                q_image = load_image(question_img_name[3], -1, True)
            elif seconds > 2 and seconds < 2.4:
                q_image = load_image(question_img_name[4], -1, True)
            elif seconds > 2.4 and seconds < 2.8:
                q_image = load_image(question_img_name[5], -1, True)
            elif seconds > 2.8 and seconds < 3.6:
                q_image = load_image(question_img_name[6], -1, True)
            elif seconds > 3.6 and seconds < 3.9:
                q_image = load_image(question_img_name[7], -1, True)
            elif seconds > 3.9 and seconds < 4.3:
                q_image = load_image(question_img_name[8], -1, True)
            elif seconds > 4.3:
                q_image = load_image(question_img_name[9], -1, True)
            if seconds >= 5 and start_mic == False:
                start_mic = True

        #get response
        if asked == True and answered == False and start_mic == True:
            #show microphone
            screen.blit(mic_image, (700, 0))
            pygame.display.update()
            answered = True
            get_response()

        # screen.blit(background, (0,0))
        allsprites.draw(screen)
        if q_image:
            screen.blit(q_image, (0, 0)) 
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()