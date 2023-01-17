import speech_recognition as sr
import os
import pygame

#Initialize pygame
pygame.init()

#crete the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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
    'congrats': load_sound("11. Congratulations.wav"),
    'bmo_likes': load_sound("12. BMO likes.wav"),
    'congratulations': load_sound("13. Congrats you are state champion.wav"),
}

def main():
    running  = True
    r = sr.Recognizer()
    
    while running:
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