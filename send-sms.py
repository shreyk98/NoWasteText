#from twilio.rest import Client

 #Your Account SID from twilio.com/console
account_sid = "AC94a6d1556476eb249a41d7c90ce69f55"
 # Your Auth Token from twilio.com/console
auth_token  = "f689f4a7479fbcfe5af22d215865b25c"


from flask import Flask, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
import fire


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    #body is the message content sent to us by user
    #number is the phone number of user
    body = request.values.get('Body', None)
    number = request.values.get('From', None)
    #create and update globalbody variabe
    global globalbody 
    #convert to string
    globalbody = str(body)
    #create and update globalnumber
    global globalnumber 
    #convert to string
    globalnumber = str(number)
    
    #number of media files sent to us 
    #num_media = int(request.values.get('NumMedia', 0))
#    
    #list of urls of the media files
    #media_files = [request.values.get("MediaUrl{}".format(i), '')
     #               for i in range(0, num_media)]
   
    #global globalmedia_files
    #globalmedia_files = media_files
    
    print(globalbody)
    print(globalnumber)
    #print (globalmedia_files)
    return redirect(url_for('process'))


@app.route("/process", methods=['GET', 'POST'])
def process():
    #place process here 
    print(globalbody)
    print(globalnumber)
    #IF ELSE STATEMENT HERE 
    #IF ONLY TEXT
    response = fire.mymessage(globalbody, globalnumber)
    #ELIF ONLY IMAGE
    #ELIF BOTH SENT --> error
    #response = globalbody + " " + globalnumber   
    resp = MessagingResponse()
    # Add a message    
    resp.message(response)
    return str(resp)
    
if __name__ == "__main__":
    #app.run(host='127.0.0.1',port=5000)
    app.run(debug=True)