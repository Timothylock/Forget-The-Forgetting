import sys
import database.database as db
import NestInput.nestCom as cam

# Database creation
print("======== First-Time Run ========")
print("Creating new database ...")
db.generateNewDatabase()
print("Done")

# Camera Status Check
print("Checking status of camera")
if (cam.pullImage("img1.jpg") == 0):
    print("Camera online. Good to go")
else:
    print("Camera is offline. Please check your connection")
    input= raw_input("Press Enter to exit...")
    sys.exit()

# First Picture Cal
print("\n\nPlease put your everyday items into the frame. The camera will take a picture")
input= raw_input("Press Enter to continue...")
if (cam.pullImage("img1.jpg") == 0):
    print("Picture taken")
else:
    print("Unexpected error. Check your internet connection and make sure your camera is connected.")
    input= raw_input("Press Enter to exit...")
    sys.exit()
print("\n\nPlease remove the items that you normally take away. The camera will take a picture")
print("Don't worry if you forget something. The system will learn over the next week!")
input= raw_input("Press Enter to continue...")
if (cam.pullImage("img2.jpg") == 0):
    print("Picture taken")
else:
    print("Unexpected error. Check your internet connection and make sure your camera is connected.")
    input= raw_input("Press Enter to exit...")
    sys.exit()

# Send to learn



