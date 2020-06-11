import argparse

import speech_recognition as sr
from pynput.keyboard import Key, Controller

def keypress(keyInput):
    keyboard = Controller()
    keyboard.press(keyInput)
    keyboard.release(keyInput)

def play():
    keypress(Key.space)

def fullscreen():
    keypress('f')

def forward():
    keypress(Key.right)

def backward():
    keypress(Key.left)

def vUp():
    keypress(Key.up)

def vDown():
    keypress(Key.down)
    
def run(args):
    r = sr.Recognizer()
    r.energy_threshold = args.threshold
    times = args.skip
    with sr.Microphone() as source:
        while 1:
            audio = r.listen(source, phrase_time_limit=5) 
            try:
                user = r.recognize_google(audio)

                print(user)

                if 'play' in user:
                    play()
                elif 'stop' in user:
                    play()
                elif 'full screen' in user:
                    fullscreen()
                elif 'volume up' in user:
                    vUp()
                elif 'volume down' in user:
                    vDown()
                elif 'forward' in user:
                    for _ in range(int(times)):
                        forward()
                    play()
                elif 'backward' in user:
                    for _ in range(int(times)):
                        backward()
                    play()

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


def main():
    parser = argparse.ArgumentParser(description='Send key inputs using voice commands.')
    parser.add_argument(
        '-thresh', 
        help='Set microphone sensitivity at which it will react to sound. Higher number - lower sensitivity. Default - 4000.', 
        dest='threshold', 
        type=int, 
        default=4000, 
        required=False)
    parser.add_argument(
        '-skip', 
        help='Set the amount of skips (forward and backward) to do after you say "forward" or "backward". Default - 4', 
        dest='skip', 
        type=int, 
        default=4, 
        required=False)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)
    

if __name__ == '__main__':
    main()
