import sys
import os
import time
import database.database as db
#import NestInput.nestCom as cam
import ImageProc.im_proc as imgProc
import ObjRecognition.imageRecognition as recog
import cv2
import twillio.sendTwillio as twi

camera_port = 1
camera = cv2.VideoCapture(camera_port)
camera.set(3,1920)
camera.set(4,1080)
time.sleep(1)


# Database creation
print("======== First-Time Run ========")
print("Creating new database ...")
db.generateNewDatabase()
print("Done")

# Camera Status Check

print("Checking status of camera")


# First Picture Cal
print("\n\nPlease put your everyday items into the frame. The camera will take a picture")
input= raw_input("Press Enter to continue...")
return_value, image = camera.read()
cv2.imwrite("img1.jpg", image)
time.sleep(1)
return_value, image = camera.read()
cv2.imwrite("img1.jpg", image)
del(camera)
camera_port = 1
camera = cv2.VideoCapture(camera_port)
camera.set(3,1920)
camera.set(4,1080)
time.sleep(1)
print("\n\nPlease remove the items that you normally take away. The camera will take a picture")
print("Don't worry if you forget something. The system will learn over the next week!")
input= raw_input("Press Enter to continue...")
return_value, image = camera.read()
cv2.imwrite("img2.jpg", image)
return_value, image = camera.read()
cv2.imwrite("img2.jpg", image)
del(camera)

# Send to learn
x = imgProc.find("img1.jpg", "img2.jpg")
try:
    os.remove("data.jpg")
except:
    pass
os.rename("1.jpg", "data.jpg")
res = recog.doRequest()
print(res)
twi.sendSMS("+1 647-486-9484", "Trained!")
#db.storeObject(res, -1, -1, True)
while True:
        # First Picture Cal
    print("\n\ndebug1")
    input= raw_input("Press Enter to continue...")
    camera_port = 1
    camera = cv2.VideoCapture(camera_port)
    camera.set(3,1920)
    camera.set(4,1080)
    time.sleep(1)
    return_value, image = camera.read()
    cv2.imwrite("img1.jpg", image)
    time.sleep(1)
    return_value, image = camera.read()
    cv2.imwrite("img1.jpg", image)
    del(camera)
    camera_port = 1
    camera = cv2.VideoCapture(camera_port)
    camera.set(3,1920)
    camera.set(4,1080)
    time.sleep(1)
    print("\n\ndebug2")
    print("Don't worry if you forget something. The system will learn over the next week!")
    input= raw_input("Press Enter to continue...")
    return_value, image = camera.read()
    cv2.imwrite("img2.jpg", image)
    return_value, image = camera.read()
    cv2.imwrite("img2.jpg", image)
    del(camera)

    # Send to learn
    x = imgProc.find("img1.jpg", "img2.jpg")
    try:
        os.remove("data.jpg")
    except:
        pass
    os.rename("1.jpg", "data.jpg")
    res = recog.doRequest()
    print(res)
    twi.sendSMS("+1 647-486-9484", "It looks like your forgot to bring the pen!")








