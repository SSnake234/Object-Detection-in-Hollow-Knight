import cv2 as cv
import numpy as np

class ObjectDectection:
    target_img = None
    target_w = 0
    target_h = 0
    method = None
    
    def __init__(self, target_img_path, method=cv.TM_CCOEFF_NORMED):
        # Load the target image
        self.target_img = cv.imread(target_img_path, cv.IMREAD_UNCHANGED)
        self.target_img = cv.cvtColor(self.target_img, cv.COLOR_BGRA2BGR)
        # Save the dimensions of the target image
        self.target_w = self.target_img.shape[1]
        self.target_h = self.target_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def match(self, background_img, target_img, threshold=0.5):
        result = cv.matchTemplate(background_img, target_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        
        return locations
    
    def draw_rectangle(self, background_img, threshold=0.5):
        # target_flipped = cv.flip(self.target_img, 1)
        locations = self.match(background_img, self.target_img, threshold)
        # locations.extend(self.match(background_img, target_flipped, threshold))

        # Create rectangles and eliminate overlapping ones
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.target_w, self.target_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)


        if len(rectangles):
            print("Found needle.")
            line_color = (0, 255, 0)
            lineType=cv.LINE_4
            
            for (x, y, w, h) in rectangles:
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Draw the boxes
                cv.rectangle(background_img, top_left, bottom_right,
                            color = line_color, lineType=lineType, thickness=2)

            
        cv.imshow("Matches", background_img)
        return
    
    def detect(self, background_img, threshold=0.5):
        match = self.match(background_img, self.target_img, threshold)

        if match:
            return True
        return False