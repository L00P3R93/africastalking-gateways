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

    def call(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify your Africa's Talking phone number in international format
        callFrom = "+254711082XXX"

        # Specify the numbers that you want to call to in a comma-separated list
        # Please ensure you include the country code (+254 for Kenya in this case)
        callTo   = "+254711XXXYYY,+254733YYYZZZ"

        try:
             results = gateway.call(callFrom, callTo)
             for result in results:
                 # Only status "Queued" means the call was successfully placed
                 print "Status : %s; phoneNumber : %s " % (
                     result['status'], result['phoneNumber'])
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while making the call: %s' % str(e)


if __name__ == '__main__':
    VOICE().call();
