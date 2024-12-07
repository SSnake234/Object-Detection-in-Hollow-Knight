import numpy as np
import cv2 as cv
import win32gui, win32ui, win32con
import mss
import mss.tools

class WindowCapture:
    # properties
    w = 1920    # change this
    h = 1080    # change this
    hwnd = None

    # constructor
    def __init__(self, window_name=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        
        # window_rect = win32gui.GetWindowRect(self.hwnd)
        # self.w = window_rect[2] - window_rect[0]
        # self.h = window_rect[3] - window_rect[1]

        # border_pixels = 8
        # titlebar_pixels = 30
        # self.w = self.w - (border_pixels * 2)
        # self.h = self.h - titlebar_pixels - border_pixels
        # self.cropped_x = border_pixels
        # self.cropped_y = titlebar_pixels
        

    def get_screenshot(self):
        # Using win32gui
        # wDC = win32gui.GetWindowDC(self.hwnd)
        # dcObj = win32ui.CreateDCFromHandle(wDC)
        # cDC = dcObj.CreateCompatibleDC()
        # dataBitMap = win32ui.CreateBitmap()
        # dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        # cDC.SelectObject(dataBitMap)
        # cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # # convert the raw data into a format opencv can read
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
        
        # Using mss
        monitor = {"top": 0, "left": 0, "width": self.w, "height": self.h}
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
        