import numpy as np
import cv2 as cv
import win32gui, win32ui, win32con
import mss
import mss.tools

class WindowCapture:
    # properties
    w = 1920
    h = 1080
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        

    def get_screenshot(self):
        # Using win32gui
        # wDC = win32gui.GetWindowDC(self.hwnd)
        # dcObj = win32ui.CreateDCFromHandle(wDC)
        # cDC = dcObj.CreateCompatibleDC()
        # dataBitMap = win32ui.CreateBitmap()
        # dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        # cDC.SelectObject(dataBitMap)
        # cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        # signedIntsArray = dataBitMap.GetBitmapBits(True)
        # screenshot = np.frombuffer(signedIntsArray, dtype='uint8')
        # screenshot.shape = (self.h, self.w, 4)

        # dcObj.DeleteDC()
        # cDC.DeleteDC()
        # win32gui.ReleaseDC(self.hwnd, wDC)
        # win32gui.DeleteObject(dataBitMap.GetHandle())
        
        # screenshot = screenshot[...,:3]
        # screenshot = np.ascontiguousarray(screenshot)
        
        # Using mss (faster)
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        with mss.mss() as sct:
            screenshot = sct.grab(monitor)
            
        screenshot = np.array(screenshot) 
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGRA2BGR)
        
        return screenshot

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)