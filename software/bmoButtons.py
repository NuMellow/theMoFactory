from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
import RPi.GPIO as GPIO
import time

keyboard = keyboardController()
mouse = mouseController()

rightPin = 11
upPin = 13
downPin = 15
leftPin = 16
greenPin = 18
redPin = 31
bluePin = 29

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(upPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(downPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(leftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(rightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(redPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(greenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(bluePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

   #add button press event listener
   GPIO.add_event_detect(upPin, GPIO.BOTH, callback=up, bouncetime=200)
   GPIO.add_event_detect(downPin, GPIO.BOTH, callback=down, bouncetime=200)
   GPIO.add_event_detect(rightPin, GPIO.BOTH, callback=right, bouncetime=200)
   GPIO.add_event_detect(leftPin, GPIO.BOTH, callback=left, bouncetime=200)
   GPIO.add_event_detect(redPin, GPIO.BOTH, callback=enter, bouncetime=200)
   GPIO.add_event_detect(greenPin, GPIO.BOTH, callback=tab, bouncetime=200)
   GPIO.add_event_detect(bluePin, GPIO.BOTH, callback=esc, bouncetime=200)

def up(sig):
   keyboard.press(Key.up)
   keyboard.release(Key.up)

def down(sig):
   keyboard.press(Key.down)
   keyboard.release(Key.down)

def left(sig):
   keyboard.press(Key.left)
   keyboard.release(Key.left)

def right(sig):
   keyboard.press(Key.right)
   keyboard.release(Key.right)

def click(sig):
   mouse.click(Button.left)

def rightClick(sig):
   mouse.click(Button.right)

def enter(sig):
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)

def tab(sig):
   keyboard.press(Key.tab)
   keyboard.release(Key.tab)


def esc(sig):
   keyboard.press(Key.esc)
   keyboard.release(Key.esc)

def destroy():
   GPIO.cleanup()

def loop():
   while True:
      pass

if __name__ == '__main__':
   setup()
   try:
      loop()
   except KeyboardInterrupt:
      destroy()
