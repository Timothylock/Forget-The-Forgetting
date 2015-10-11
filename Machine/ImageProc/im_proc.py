import cv2
import time
from numpy.linalg import norm
from numpy import sum, average
import numpy as np

def find( fimg1, fimg2):
    file1 = cv2.imread(fimg1, 0)
    file2 = cv2.imread(fimg2, 0)
    fileb1 = gblurring(file1)
    fileb2 = gblurring(file2)
    file1m = work(fileb1)
    file2m = work(fileb2)
    #(thresh, im_bw1) = cv2.threshold(file1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    #(thresh, im_bw2) = cv2.threshold(file2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    imageofawesomeness = compare_images(file1m, file2m)
    cv2.imwrite ("diff.jpg", imageofawesomeness)
    print("image comparing finished")
    x, y, w, h = searchchangepixel('diff.jpg')
    crop(fimg1, x, y, w, h)
    
    #n_m, n_0 = compare_images(img1, img2)
    #print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
    #print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size

def compare_images(img1, img2):
    # normalize to compensate for exposure difference
    #img1 = normalize(img1)
    #img2 = normalize(img2)
    cv2.imwrite ("image1norm.jpg", img1)
    cv2.imwrite ("image2norm.jpg", img2)
    # calculate the difference and its norms
    diff = (img2 - img1)  # elementwise for scipy arrays
    cv2.imwrite('imageofawesomeness1.jpg', diff)
    return (diff)
    #m_norm = sum(abs(diff))  # Manhattan norm
    #z_norm = norm(diff.ravel(), 0)  # Zero norm
    
    return (diff)
    #return (m_norm, z_norm)

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def work(img):
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite('diff.jpg', im_bw)
    return im_bw

def work_OLD(img):
    for x in range(0,1080):
        for y in range(0,1920):
            px = img [x, y]
            if px[0]<=128 or px[1]<=128 or px[2]<=128:
                    img [x,y] = [0,0,0]
                    #print (str(x) + " " + str(y) + "Blue")
            elif px[0]>=129 and px[1]>=129:
                    img [x,y] = [255,255,255]
                    #print (str(x) + " " + str(y) + "Green")
            #elif px[2]>=px[1] and px[2]>=px[0]:
                   # img [x,y] = [0,0,255]
                    #print (str(x) + " " + str(y) + "Red")
                    #time.sleep(0.01)
    print("work processing finished")
    return img

def gblurring(filename):

    imageblur = cv2.GaussianBlur(filename, (9,9), 1)
    cv2.imwrite('blurimage.jpg', imageblur)

    return imageblur

def bilateralblurring (filename):
    imageblur = cv2.bilateralFilter(filename, 9, 75, 75)
    cv2.imwrite('bilateralimage.jpg', imageblur)
    return imageblur


def median (filename):
    imageblur = cv2.medianBlur(filename, 5)
    cv2.imwrite('median.jpg', imageblur)
    return imageblur

    
    
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
    listrequest = [0,0,0,0]
    listrequest[0] = x
    listrequest[1] = y
    listrequest[2] = x+w
    listrequest[3] = y+h
    return( x, y, w, h )# where x, y is the coordinate of the upper left coordinate,

def crop(filename, x, y, w, h):
    img = cv2.imread(filename)
    crop_img = img[y: y+h, x: x+w]
    cv2.imwrite("1.jpg", crop_img)
    #cv2.imshow("cropped", crop_img)
    #.waitkey(0)


if __name__ == "__main__":
    find(0,0)


