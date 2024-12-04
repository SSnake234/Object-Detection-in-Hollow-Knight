import cv2 as cv
import numpy as np
import os
import time
from window_capture import WindowCapture
from object_detection import ObjectDectection
import pyautogui


# List all window names
# WindowCapture.list_window_names()
# exit()

#initialize the WindowCapture class
wincap = WindowCapture()
object_dectector_self_left = ObjectDectection("imgs/self_left.png")
object_dectector_self_right = ObjectDectection("imgs/self_right.png")

loop_time = time.time()
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    if object_dectector_self_left.detect(screenshot, threshold=0.5):
        print("Facing left, jumping.")
        pyautogui.keyDown('x')
        time.sleep(1)
        pyautogui.keyUp('x')
    
    elif object_dectector_self_right.detect(screenshot, threshold=0.5):
        print("Facing right, hitting.")
        pyautogui.press('c')
        
    
    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')