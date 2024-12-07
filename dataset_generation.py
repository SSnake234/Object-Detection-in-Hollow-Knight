from window_capture import WindowCapture
import cv2 as cv
import numpy as np
import os
import time

def capture_screenshots(destination_folder, num_screenshots, delay):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    wincap = WindowCapture('Hollow Knight')

    for i in range(num_screenshots):
        screenshot = wincap.get_screenshot()
        filename = os.path.join(destination_folder, f'screenshot_{i+1}.jpg')
        cv.imwrite(filename, screenshot)
        print(f'Screenshot {i+1} saved to {filename}')
        time.sleep(delay)

destination_folder = "grimm_dataset/raw images (pre-annotated)"
num_screenshots = 500
delay = 0.2  # seconds
capture_screenshots(destination_folder, num_screenshots, delay)