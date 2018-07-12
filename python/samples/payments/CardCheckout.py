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

    def checkout(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        paymentCard = {
            'number'      : '12344568901234',
            'countryCode' : 'NG',
            'cvvNumber'   : 205,
            'expiryMonth' : 9,
            'expiryYear'  : 2019,
            'authToken'   : '1234'
        }
        try:
            # Initiate the checkout. If successful, you will get back a transactionId
            # that you can then use to validate the OTP that is sent to the user
            transactionId = gateway.cardPaymentCheckoutCharge(
                productName_   = 'Airtime Distribution',
                paymentCard_   = paymentCard,
                currencyCode_  = 'NGN',
                amount_        = 100,
                narration_     = 'Airtime Purchase Request',
                metadata_      = {
                    'Reason' : 'To Test The Gateways'
                }
            )
            print "The transactionId is %s" % transactionId
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while checking out: %s' % str(e)

    def checkout_with_token(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        # Any gateway errors will be captured by our custom Exception class below, 
        # so wrap the call in a try-catch block
        try:
            gateway.cardPaymentCheckoutChargeWithToken(
                productName_   = 'Airtime Distribution',
                checkoutToken_ = 'ATCdTkn_ac1b0ce6c8ca6da4f50ab0d',
                currencyCode_  = 'NGN',
                amount_        = 100,
                narration_     = 'Airtime Purchase Request',
                metadata_      = {
                    'Reason' : 'To Test The Gateways'
                }
            )
            print "The transactionId was successful"
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while sending: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().checkout()
    PAYMENTS().checkout_with_token()
