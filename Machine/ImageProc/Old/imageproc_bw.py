import cv2
import time
from numpy.linalg import norm
from numpy import sum, average
import numpy as np

def main():
    file1 = cv2.imread("img1.jpg", 1)
    file2 = cv2.imread("img2.jpg", 1)
    file1m = work(file1)
    file2m = work(file2)
    (thresh, im_bw1) = cv2.threshold(file1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, im_bw2) = cv2.threshold(file2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    imageofawesomeness = compare_images(im_bw1, im_bw2)


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
    diff = abs(img1 - img2)  # elementwise for scipy arrays
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
    for x in range(0,1080):
        for y in range(0,1920):
            px = img [x, y]
            if px[0]>=px[1] and px[0]>=px[2]:
                    img [x,y] = [255,0,0]
                    #print (str(x) + " " + str(y) + "Blue")
            elif px[1]>=px[2] and px[1]>=px[0]:
                    img [x,y] = [0,255,0]
                    #print (str(x) + " " + str(y) + "Green")
            elif px[2]>=px[1] and px[2]>=px[0]:
                    img [x,y] = [0,0,255]
                    #print (str(x) + " " + str(y) + "Red")
                    #time.sleep(0.01)
    return img

if __name__ == "__main__":
    main()
