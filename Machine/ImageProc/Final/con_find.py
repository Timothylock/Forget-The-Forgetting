import cv2
import numpy as np

def main():
    x, y, w, h = searchchangepixel('diff.jpg')
    crop("img1.jpg", x, y, w, h)
    
def searchchangepixel (resultant_image):

    img = cv2.imread(resultant_image, 0)
    (ret, thresh) = cv2.threshold(img, 127, 255, 0)
    #print (cv2.findContours(thresh, 1, 2))
    #print (len(cv2.findContours(thresh, 1, 2)))
    uglyvar, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    x = []
    for i in range(1000):
        cnt = contours[i]
        print(cv2.contourArea(cnt))
        x.append(cv2.contourArea(cnt))
    print(max(x))
    large = x.index(max(x))
    cnt = contours[large]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imwrite("something.jpg", img)
    return( x, y, w, h )# where x, y is the coordinate of the upper left coordinate,

def crop(filename, x, y, w, h):
    img = cv2.imread(filename)
    crop_img = img[y: y+h, x: x+w]
    cv2.imwrite("pleasework.jpg", crop_img)
    #cv2.imshow("cropped", crop_img)
    #.waitkey(0)
    
if __name__ == "__main__":
    main()
