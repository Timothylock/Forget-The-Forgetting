import json
import urllib
import urllib2

deviceID = "fSTakRPr6NeOYkI61VcPYJuaAmSa7KsgcjMokpys2VMnyOxrVIBIpA"
authKey = 'c.HVQ2yxxI61Qady6rHUmpQcw555W5ygCwspVYAdHXPdnoH0mzGzScAJflhzr43s68NEOdmCeBVyiI10odtbYOvktxSd924p8sWwTKmm1gOON6Od2VqKvITa2bQQyftjk4pnxyY64gdXKtbW8y'


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
    return json.load(urllib2.urlopen('https://firebase-apiserver02-tah01-iad01.dapi.production.nest.com:9553/devices.json?auth=' + authKey))

#def getPinCode():
   # return json.load(urlib2.urlopen('https://api.home.nest.com/oauth2/access_token?code=J6YJG65G&client_id=a9127997-b75c-47be-8784-7bda53021eec&client_secret=XWOQSS02rRvlMk36U7ySdYH4m&grant_type=authorization_code'))

if __name__ == "__main__":
    #print (getPinCode)
    data = pullGIF()
    print("Exites with status: " + str(data))
    print getJSON()


# given a JSON, find the websites for app, web, gif, image






