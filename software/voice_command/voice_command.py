import speech_recognition as sr
import os
import pygame

#Initialize pygame
pygame.init()

#crete the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

frame_dir = os.path.join("img", "frames")
#list of animations. These should match the name of the folders in img/frames
animation_dir = [
    "congratulations",
]
frame_rate = 41 #this is in milliseconds. a frame every 41 millisecods ~= 24 frames/sec

#dictionary that will store the name of the animation and list of loaded img frames as key value pairs
animations = {

}

def load_image(name, color_key=None, ret_surf=False):
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print("Cannot load image:", name)
        raise SystemExit("Uh oh")

    if ret_surf:
        return image
    image = image.convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0,0))
        image.set_colorkey(color_key, pygame.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    audio_dir = os.path.join('audio', name)
    return pygame.mixer.Sound(audio_dir)

responses = {
    'lorane': load_sound("1. talking to lorane.wav"),
    'bmo_time': load_sound("2. Its BMO time.wav"),
    'video_games': load_sound("3. who wants to play video games.wav"),
    'dancing_machine': load_sound("4. I'm a dancing machine.wav"),
    'dance_party': load_sound("5. Get ready for the dance party.wav"),
    'being_boring': load_sound("6. Being too boring.wav"),
    'terrible': load_sound("7.That's terrible.wav"),
    'does_computer': load_sound("8. That does compute.wav"),
    'fantastic': load_sound("9. That's fantastic.wav"),
    'rather_pizza': load_sound("10. Rather be eating pizza.wav"),
    'congratulations': load_sound("11. Congratulations.wav"),
    'bmo_likes': load_sound("12. BMO likes.wav"),
}

def load_animations():
    for anim in animation_dir:
        dir = os.path.join(frame_dir, anim)
        animations.update({anim: []})
        for filename in os.listdir(dir):
            file = os.path.join(dir, filename)
            if os.path.isfile(file):
                img = load_image(file)
                animations[anim].append(img)

def play(animation_name):
    pygame.mixer.Sound.play(responses.get(animation_name))

def play_anim(animation_name, start_ticks):
    frames = animations.get(animation_name)
    frames_temp = frames.copy()
    img = None
    popped_at = 0

    while len(frames_temp) > 0:
        milli_seconds = (pygame.time.get_ticks()-start_ticks)
        if milli_seconds % 41 == 0 and milli_seconds != popped_at:
            popped_at = milli_seconds
            print(milli_seconds)
            img, _ = frames_temp.pop(0)
            screen.blit(img, (0, 0))
            pygame.display.update()
       
def main():
    running  = True
    r = sr.Recognizer()
    load_animations()

    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)

        print("listening")
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            tts = r.recognize_google(audio)
            print("You said " + tts)

            #this is where the specific responses go
            if tts == "okay BMO" or tts == "a BMO":
                print("Yaaay!")
            elif tts == "quit":
                running = False
            elif tts == "I did it":
                play("congratulations")
                start_ticks = pygame.time.get_ticks()
                play_anim("congratulations", start_ticks)

        except LookupError:
            print("could not understand audio")
            # say something like I couldn't hear you
        except sr.WaitTimeoutError:
            print("crickets")
            continue
        except Exception:
            print("oop ")


if __name__ == "__main__":
    main()