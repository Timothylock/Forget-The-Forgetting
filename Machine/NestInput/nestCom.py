import json
import urllib
import urllib2

deviceID = "fSTakRPr6NeOYkI61VcPYJuaAmSa7KsgcjMokpys2VMnyOxrVIBIpA"
authKey = 'c.gKO5d3kPjE7SeGF4RzUHNvzaG5ev8yghBFR27G6Sqfnia5QyORuqQ8pZ4HMdSAOp0rKBqyqDOeyqEFRp7I6be6HUDvwhTPu3NUwKSs0OyASHfmBbx5jFTyayLEPmk9nvflFly6wDZa06N5Pl'

def pullGIF():
    data = getJSON()
    if (data == "ERR") or ((data["cameras"][deviceID]["is_online"]) == False):
        return -1
    urllib.urlretrieve(data["cameras"][deviceID]["last_event"]["animated_image_url"], "nest_animated.gif")
    return 0

def pullImage():
    data = getJSON()
    if (data == "ERR") or ((data["cameras"][deviceID]["is_online"]) == False):
        return -1
    urllib.urlretrieve(data["cameras"][deviceID]["last_event"]["image_url"], "nest_image.jpg")
    return 0

def hasMotion():
    data = getJSON()
    if (data == "ERR") or ((data["cameras"][deviceID]["is_online"]) == False):
        return -1
    return data["cameras"][deviceID]["last_event"]["has_motion"]

def getJSON():
    return json.load(urllib2.urlopen('https://developer-api.nest.com/devices?auth=' + authKey))

if __name__ == "__main__":
    data = pullGIF()
    print("Exites with status: " + str(data))
