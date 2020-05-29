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
    

def mainfunctions(source):
    audio = r.listen(source, phrase_time_limit=5) 
    try:
        user = r.recognize_google(audio)

        print(user)

        if 'play' in user:
            play()
            # r.adjust_for_ambient_noise(source)
        elif 'stop' in user:
            play()
            # r.adjust_for_ambient_noise(source)
        elif 'full screen' in user:
            fullscreen()
        elif 'volume up' in user:
            vUp()
        elif 'volume down' in user:
            vDown()
        elif 'forward' in user:
            times = user.split(' ')[2]
            try:
                times = int(times)
            except ValueError:
                times = 1
            for _ in range(int(times)):
                forward()
            play()
        elif 'backwards' in user:
            times = user.split(' ')[2]
            try:
                times = int(times)
            except ValueError:
                times = 1
            for _ in range(int(times)):
                backward()
            play()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        

if __name__ == '__main__':
    r = sr.Recognizer()
    r.energy_threshold = 8500
    with sr.Microphone() as source:
        # audio = r.listen_in_background(source,)
        while 1:
            mainfunctions(source)
