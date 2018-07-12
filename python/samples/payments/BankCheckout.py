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
        try:
            transactionId = gateway.bankPaymentCheckoutCharge(
                productName_  = 'Airtime Distribution',
                currencyCode_ = 'NGN',
                amount_       = 100,
                narration_    = 'Airtime Purchase Request',
                bankAccount_  = {
                    'accountName'   : 'Fela Kuti',
                    'accountNumber' : '123456789',
                    'bankCode'      : 234004
                },
                metadata_     = {
                    'Reason' : 'To Test The Gateways'
                }
            )       
            print transactionId
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while sending: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().checkout()
