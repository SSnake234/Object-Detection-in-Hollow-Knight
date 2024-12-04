# import mss
# from PIL import Image, ImageGrab
# import pyautogui
# import pygetwindow as gw
# import cv2 as cv
# import numpy as np
# import time

# # Get the dimensions of the selected window
# selected_window = gw.getWindowsWithTitle("Zalo")[0]
# left, top, right, bottom = selected_window.left, selected_window.top, selected_window.right, selected_window.bottom

# # Set the monitor bounds based on the selected window
# monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
# print(f"Window bounds: {monitor}")

# img = None
# t0 = time.time()
# n_frames = 1

# with mss.mss() as sct:
#     while True:
#         img = sct.grab(monitor)  # Capture only the selected window
#         img = np.array(img)      # Convert to NumPy array
        
#         # Optional: Convert RGB to BGR for OpenCV
#         # img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        
#         small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
#         cv.imshow("Computer Vision - Specific Window", small)

#         # Break loop and end test
#         key = cv.waitKey(1)
#         if key == ord('q'):
#             break
        
#         elapsed_time = time.time() - t0
#         avg_fps = (n_frames / elapsed_time)
#         print(f"Average FPS: {avg_fps:.2f}")
#         n_frames += 1

# cv.destroyAllWindows()