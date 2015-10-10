# -*- coding: utf-8 -*-
import requests
import sys, getopt
import time
from ftplib import FTP_TLS

def doRequest():

    # Send the file up to the FTP server
    print ("Upload picture start")
    ftp = FTP_TLS('individual.utoronto.ca', 'USER','PASSWORD')
    file = open('data.jpg','rb')                  # file to send
    ftp.storbinary('STOR data.jpg', file)     # send the file
    file.close()                                    # close file and FTP
    ftp.quit()
    print ("Upload picture complete")
    print ("Requesting file request")
    reqUrlA = 'http://api.cloudsightapi.com/image_requests/' # get token
    reqUrlB = 'http://api.cloudsightapi.com/image_responses/' # get the final recognition result with token

    headers = { 
    'Authorization' : 'CloudSight 149xzcR0nYPrwThNXVLecQ',
    }

    postData = {
    'image_request[remote_image_url]' : "http://individual.utoronto.ca/timlock/data.jpg",
    'image_request[locale]': "en_us",
    'image_request[language]': "en"
    }

    try:
        response = requests.post(reqUrlA, headers=headers, params=postData)
    except Exception, e:
        print 'Error: connection error, please check your Internet and confirm the image url'
        print e
        return ("FAILED")
    if "error" in response.json():
        print "Error: %s" % response.json()["error"]
        return ("FAILED")
    else:
        token = response.json()['token']
        print(token)

        # you may get some response with status 'not completed' for about some times before getting the final result
        reqTimes = 20
        while reqTimes > 0:
            time.sleep(10)
            try:
                response = requests.get(reqUrlB + token, headers=headers)
            except Exception, e:
                print 'Error: connection error, please check your Internet and confirm the image url'
                sys.exit()
            status = response.json()['status']
            if status == 'completed':
                print 'RESULT: '
                print '\timage url:', "http://individual.utoronto.ca/timlock/data.jpg"
                print '\timage name:', response.json()['name']
                return response.json()['name']
                # return response.json()['name']
                break
            elif status == 'not completed':
                print 'recognition in progress'
                reqTimes -= 1

        return ("FAILED")



if __name__ == '__main__':
    doRequest()
