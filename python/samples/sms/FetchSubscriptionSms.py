# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class SMS:
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

    def fetch_subscriptions(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        try:
            # Our gateway will return 100 numbers at a time back to you, starting with
            # what you currently believe is the lastReceivedId. Specify 0 for the first
            # time you access the gateway, and the ID of the last message we sent you
            # on subsequent results
            # Specify your Africa's Talking short code and keyword
            shortCode = "MyAppShortCode";
            keyword   = "MyAppKeyword";
            
            lastReceivedId = 0;

            while True:
                subcriptions = gateway.fetchPremiumSubscriptions(shortCode, keyword, lastReceivedId)
                if len(subcriptions) == 0:
                    print 'No subscription numbers.'
                    break
                for subscription in subscriptions:
                    print 'phone number : %s;' % subscription['phoneNumber']
                    lastReceivedId = subscription['id']

        except AfricasTalkingGatewayException as e:
            print 'Encountered an error while fetching numbers: %s' % str(e)


if __name__ == '__main__':
    SMS().fetch_subscriptions()
