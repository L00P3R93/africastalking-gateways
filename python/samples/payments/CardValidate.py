# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class PAYMENTS:
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

    def validate(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        try:
            checkoutToken = gateway.cardPaymentCheckoutValidation(
                transactionId_ = "ATPid_d33b9f02741397e25b3c5f1e81e23a5b",
                otp_           = "1234"
            )
            print "The checkoutToken is %s" % checkoutToken
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while validating: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().validate()
