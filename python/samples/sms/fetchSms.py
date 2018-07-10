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

    def fetch(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        try:
            # Our gateway will return 10 messages at a time back to you, starting with
            # what you currently believe is the lastReceivedId. Specify 0 for the first
            # time you access the gateway, and the ID of the last message we sent you
            # on subsequent results
            lastReceivedId = 0;

            while True:
                messages = gateway.fetchMessages(lastReceivedId)
                if len(messages) == 0:
                    print 'No sms messages in your inbox.'
                    break
                for message in messages:
                    print 'from = %s; to = %s; date = %s; text = %s; linkId = %s;' % (
                        message['from'], message['to'], message['date'], message['text'], message['linKId'])
                    lastReceivedId = message['id']

        except AfricasTalkingGatewayException as e:
            print 'Encountered an error while fetching messages: %s' % str(e)


if __name__ == '__main__':
    SMS().fetch();
