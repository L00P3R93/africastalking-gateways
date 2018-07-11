# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class VOICE:
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

    def fetch_queued_calls(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify your Africa's Talking phone number in international format
        phoneNumber = "+254711082XXX"

        try:
            # Get queued calls
            queuedcalls = gateway.getNumQueuedCalls(phoneNumber)

            # For a specific queue, specify the queue name eg:
            # queueName = "myQueueName"
            #results = gateway.getNumQueuedCalls(phoneNumber, queueName)

            for result in queuedcalls:
                print "phoneNumber: %s; queueName: %s; number of queued calls: %s \n" % (
                    result['phoneNumber'], result['queueName'], result['numCalls'])
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while getting queued calls: %s' % str(e)

if __name__ == '__main__':
    VOICE().fetch_queued_calls()
