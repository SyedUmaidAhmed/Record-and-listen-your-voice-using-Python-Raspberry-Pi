import os
import sys
import subprocess
from time import sleep
from subprocess import Popen


proc = subprocess.Popen(['arecord --device=hw:1,0 --duration=10 --format S16_LE --rate 44100 -V mono -c1 test.wav'], shell=True)
sleep(10)
proc.terminate()
print("Closing the recording and wait please....")


print("Listening after two seconds")
broc = subprocess.Popen(['aplay --device=plughw:1,0 test.wav'], shell=True)
