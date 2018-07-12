# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class APPLICATIONDATA:
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

    def user_data(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        try:
            user = gateway.getUserData()
            print user['balance']
            # The result will have the format=> KES XXX
        except AfricasTalkingGatewayException, e:
            print 'Error: %s' % str(e)


if __name__ == '__main__':
    APPLICATIONDATA().user_data()
