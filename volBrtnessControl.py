import cv2
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import threading

from handLmModel import handDetector  # Import hand tracking module

# ✅ Initialize Hand Detector (Moved outside loop)
handlmsObj = handDetector(detectionCon=0.7, trackCon=0.7)

# ✅ Capture Video
vidObj = cv2.VideoCapture(0)
vidObj.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vidObj.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# ✅ Audio Control Setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVolume, maxVolume = volRange[0], volRange[1]

# ✅ Brightness Control Setup
minBrightness, maxBrightness = 0, 100


# ✅ Functions for Volume & Brightness Control
def setVolume(dist):
    vol = np.interp(int(dist), [35, 215], [minVolume, maxVolume])
    volume.SetMasterVolumeLevel(vol, None)


def setBrightness(dist):
    brightness = np.interp(int(dist), [35, 230], [minBrightness, maxBrightness])
    sbc.set_brightness(int(brightness))


# ✅ Main Loop
while True:
    _, frame = vidObj.read()
    frame = cv2.flip(frame, 1)

    frame = handlmsObj.findHands(frame)  # ✅ Use initialized handDetector
    lndmrks = handlmsObj.findPosition(frame, draw=False)

    if lndmrks:
        xr1, yr1 = lndmrks[1][4][1], lndmrks[1][4][2]  # Thumb
        xr2, yr2 = lndmrks[1][8][1], lndmrks[1][8][2]  # Index Finger
        dist = math.hypot(xr2 - xr1, yr2 - yr1)

        if lndmrks[0] == 'Left':
            setBrightness(dist)
        elif lndmrks[0] == 'Right':
            setVolume(dist)
        elif lndmrks[0] == 'both':
            xl1, yl1 = lndmrks[1][4][1], lndmrks[1][4][2]
            xl2, yl2 = lndmrks[1][8][1], lndmrks[1][8][2]
            distl = math.hypot(xl2 - xl1, yl2 - yl1)

            t1 = threading.Thread(target=setVolume, args=(dist,))
            t2 = threading.Thread(target=setBrightness, args=(distl,))

            t1.start()
            t2.start()

    cv2.imshow("stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
