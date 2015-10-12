from twilio.rest import TwilioRestClient 

def sendSMS(recipient, text = ''):
    # put your own credentials here 
    ACCOUNT_SID = "AC67ce6ea275a28268eac662c172e7a07d" 
    AUTH_TOKEN = "c2ac7bdf1aa2a3359cf43a6f2b2b570c" 
     
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
     
    client.messages.create(
            to = recipient, 
            from_ = "+12018993782", 
            body = text,  
    )
    print("Sent SMS")
    return 1;
