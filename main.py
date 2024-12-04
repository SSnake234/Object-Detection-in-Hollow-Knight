import cv2 as cv
import numpy as np
import os
from time import time
from window_capture import WindowCapture
from object_detection import ObjectDectection


# List all window names
# WindowCapture.list_window_names()
# exit()

#initialize the WindowCapture class
wincap = WindowCapture()
object_dectector_self = ObjectDectection("imgs/self.png")

loop_time = time()
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    object_dectector_self.detect(screenshot, threshold=0.5)
    
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')