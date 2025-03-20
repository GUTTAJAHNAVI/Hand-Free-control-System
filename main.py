from threading import *
import os

class Gesture(Thread):
    def run(self):
        os.system("python Gesture_Controller.py")
        return

class bright_volume(Thread):
    def run(self):
        os.system("python volBrtnessControl.py")
        return

t1=Gesture()
t2=bright_volume()
t1.start()
t2.start()