# netflix_recognition

This is a simple script to achieve voice controlled netflix just because I'm lazy.

## Requirements
* Python 3.8.3
* PyAudio           0.2.11
* pynput            1.6.8
* SpeechRecognition 3.8.1

## Usage
Clone the repository and run $ python netflix_recognition.py

Possible arguments and usage:
```
netflix_recognition.py [-h] [-thresh THRESHOLD] [-skip SKIP]

Send key inputs using voice commands.

optional arguments:
  -h, --help         show this help message and exit
  -thresh THRESHOLD  Set microphone sensitivity at which it will react to sound. Higher number - lower sensitivity. Default - 4000.
  -skip SKIP         Set the amount of skips (forward and backward) to do after you say "forward" or "backward". Default - 4
```
When it's running just make the browser screen where netflix or youtube is on active and lay back, relax and enjoy your remote free experience.

## Making your own
To recognize voice commands [SpeechRecognition](https://pypi.org/project/SpeechRecognition/2.1.3/) package is used and then the needed key presses to do stuff are sent using [pynput](https://pypi.org/project/pynput/). 

The logic behind the script is quite simple:
* Decided what commands you want to send (such as play/pause/go forward)
* Decided on keywords that you want to map to the said commands
* Make a function for each command 
* Map functions to keywords in run function

That's about it. You're done.

## Making it a usable script
As it's a script that you may be using in different enviroments instead of changing microphone sensitivity in the code all the time the script is done using argparse. [Argparse](https://pypi.org/project/argparse/) is a great way to make your script runnable from the shell and makes it easy to add options for needed changes. See [Usage](#Usage)
