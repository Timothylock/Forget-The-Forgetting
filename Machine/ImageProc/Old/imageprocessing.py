import cv2
import numpy as np

winname = "GRS"
bgs_mog = cv2.BackgroundSubtractorKNN()
capture = cv2.VideoCapture(2)

img = cv2.imread('image.png',0)
img1 = cv2.imread('image1.png',0)

if __name__ == "__main__":
    #while capture.isOpened():
        #_,frame = capture.read()
       # fgmask = bgs_mog.apply(frame)
        #mask_rbg = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)
        #draw = frame & mask_rbg
        
        imgnew = img-img1
        cv2.imshow(imgnew)
        
        
       # cv2.imshow(winname, fgmask)
        #c = cv2.waitKey(1)
      #  if c == 27:
     #       break
    #cv2.destroyAllWindows()
    