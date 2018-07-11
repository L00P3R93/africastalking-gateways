# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class AIRTIME:
    def __init__(self):
        self.APP_USERNAME = "sandbox" # Your app username, or "sandbox" if you are testing in sandbox
        self.API_KEY = ""; # Your app or sandbox api key
        #*************************************************************************************
        #  NOTE: If connecting to the sandbox:
        #
        #  1. Use "sandbox" as the username
        #  2. Use the apiKey generated from your sandbox application
        #     https://account.africastalking.com/apps/sandbox/settings/key
        #  3. Add the "sandbox" flag to the constructor
        #
        #  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
        #**************************************************************************************

    def send(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify an array of dicts to hold the recipients and the amount to send
        recipients = [{"phoneNumber" : "+254711XXXYYY", "amount" : "KES XX"}]
        try:
            responses = gateway.sendAirtime(recipients)
            for response in responses:
                print "phoneNumber=%s; amount=%s; status=%s; discount=%s; requestId=%s" % (
                    response['phoneNumber'], response['amount'], response['status'],
                    response['discount'], response['requestId'])
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while sending airtime: %s' % str(e)


if __name__ == '__main__':
    AIRTIME().send()
