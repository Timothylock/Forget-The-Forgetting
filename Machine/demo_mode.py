import sys
import os
import database.database as db
import NestInput.nestCom as cam
import ImageProc.im_proc as imgProc
import ObjRecognition.imageRecognition as recognize

print("=======================")
print("       Demo Mode       ")
print("=======================")
print("")
import first_time
print("-----------")
while True:
    # Take first picture
    if (cam.pullImage("img1.jpg") == 0):
        print("Picture 1 taken")
    else:
        print("Unexpected error. Check your internet connection and make sure your camera is connected.")
        input= raw_input("Press Enter to exit...")
        sys.exit()
        
    input= raw_input("Emulate exit detection. Press any key to send leave command...")
    # Take second picture
    if (cam.pullImage("img2.jpg") == 0):
        print("Picture 2 taken")
    else:
        print("Unexpected error. Check your internet connection and make sure your camera is connected.")
        input= raw_input("Press Enter to exit...")
        sys.exit()

    # Call Detection
    list_gone = imgProc.find("img1.jpg", "img2.jpg")
    os.remove("data.jpg")
    os.rename("1.jpg", "data.jpg")
    taken = []
    should_get = db.getListShouldTake()
    forgot = []
    # Item processing
    for i in range(list_gone):
        x = db.getObjectsInArea(list[i][0], list[i][1], list[i][2], list[i][3])
        if len(x) == 1:
            for item in x:
                taken.append(str(item))
        else:
            x = recognize.doRequest()
            taken.append(x)
    #Check if all items taken
    for item in should_get:
        if str(item) not in taken:
            forgot.append(str(item))

    # Send out Twillio
    print(str(forgot))
    
    
