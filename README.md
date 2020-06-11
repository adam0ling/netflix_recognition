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

## Making your own
To build this script I use [SpeechRecognition](https://pypi.org/project/SpeechRecognition/2.1.3/) package
