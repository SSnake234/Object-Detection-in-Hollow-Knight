import cv2 as cv
import numpy as np

mob_img = cv.imread('imgs/mob.png', cv.IMREAD_UNCHANGED)
background_img = cv.imread('imgs/background.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(background_img, mob_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print(f"Best match top left position: {max_loc}")
print(f"Best match confidence: {max_val}")

threshold = 0.6
if max_val > threshold:
    print("Found the mob.")
    mob_w = mob_img.shape[1]
    mob_h = mob_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + mob_w, top_left[1] + mob_h)
    
    cv.rectangle(background_img, top_left, bottom_right,
                 color = (0, 255, 0), thickness = 2, lineType=cv.LINE_4)
    cv.imshow("Result", background_img)
    cv.waitKey()
    cv.imwrite("imgs/result.png", background_img)
else:
    print("Mob not found!")