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
background = pygame.image.load(bg)
mic_image = pygame.image.load(mic)

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
        screen.blit(background, (0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(response)
        time.sleep(10)
        # os.system("shutdown /s /t 1")
    except LookupError:
        print("Could no understand audio")
    except Exception:
        print("something went wrong!")

def main():
    running = True
    asked = False
    answered = False
    start_mic = False

    #display the background
    screen.blit(background, (0,0))
    pygame.display.update()

    clock = pygame.time.Clock()

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
            pygame.mixer.Sound.play(question)
            #ask the question

        #get response
        if asked == True and answered == False and start_mic == True:
            #show microphone
            screen.blit(mic_image, (700, 0))
            pygame.display.update()
            answered = True
            get_response()

        screen.blit(background, (0,0))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()