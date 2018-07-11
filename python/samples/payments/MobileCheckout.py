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

        # Specify the name of your Africa's Talking payment product
        productName = "ABC"
        # The phone number of the customer checking out
        phoneNumber = "+25471XXXXXX"
        # The 3-Letter ISO currency code for the checkout amount
        currencyCode = "KES"
        # The checkout amount
        amount = 100.50
        # Any metadata that you would like to send along with this request
        # This metadata will be  included when we send back the final payment notification
        metadata = {"agentId" : "654", "productId" : "321"}
        # The provider channel the payment will be initiated from e.g a paybill number
        providerChannel = None

        try:
            # Initiate the checkout. If successful, you will get back a transactionId
            transactionId = gateway.initiateMobilePaymentCheckout(
                productName, phoneNumber, currencyCode, amount, metadata, providerChannel)
            print "The transactionId is " + transactionId
        except AfricasTalkingGatewayException, e:
            print 'Received error response: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().checkout()
