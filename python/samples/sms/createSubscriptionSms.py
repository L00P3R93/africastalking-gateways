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

    def create_subscription(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        # Specify the number that you want to subscribe
        # Please ensure you include the country code (+254 for Kenya in this case)
        phoneNumber   = "+254711XXXYYY";
        # Specify your Africa's Talking short code and keyword
        shortCode = "MyAppShortCode";
        keyword   = "MyAppKeyword";
        # create checkout token
        try:
            checkoutToken = gateway.createCheckoutToken(phoneNumber)
        except AfricasTalkingGatewayException as e:
            print "Error generating checkout Token:%s" %str(e)
            return
        # create subscription
        try:
            response = gateway.createSubscription(phoneNumber, shortCode, keyword, checkoutToken)
            # Only status Success signifies the subscription was successfully
            print "Status: %s \n Description: %s" %(response['status'], response['description'])

        except AfricasTalkingGatewayException as e:
            print "Error creating subscription:%s" %str(e)


if __name__ == '__main__':
    SMS().create_subscription();
