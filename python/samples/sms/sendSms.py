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

    def send(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        # Specify the numbers that you want to send to in a comma-separated list
        # Please ensure you include the country code (+254 for Kenya)
        recipeints = "+254713YYYZZZ,+254733YYYZZZ"
        # Set the message to be sent
        message = "Hello, this is a test";
        # And send the SMS
        try:
            results = gateway.sendMessage(recipeints, message)
            for recipient in results:
                # status is either "Success" or "error message"
                print 'number = %s; status = %s; messageId = %s; cost = %s' % (
                    recipient['number'], recipient['status'],recipient['messageId'], recipient['cost'])

        except AfricasTalkingGatewayException as e:
            print 'Encountered an error while sending: %s' % str(e)


if __name__ == '__main__':
    SMS().send();
