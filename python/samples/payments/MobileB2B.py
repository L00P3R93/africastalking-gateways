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

    def b2b(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify the name of your Africa's Talking payment product
        productName = "ABC"
        # The 3-Letter ISO currency code for the checkout amount
        currencyCode = "KES"
        # Specify the amount to transfer
        amount = 100
        # Specify the payment provider. eg. MPESA, ATHENA (AfricasTalking Sandbox), etc
        provider = "myPaymentProvider"
        # Specify partner's business channel
        destinationChannel = "partnerBusinessChannel"
        # Specify partner's business channel account if needed. This is optional
        destinationAccount = "partnerBusinessChannelAccount"
        # Specify the transfer purpose
        transferType = "BusinessToBusinessTransfer"
        # Group providerData in a dict. This is done for convenience
        providerData = {
                        'provider' : provider,
                        'destinationChannel' : destinationChannel,
                        'destinationAccount' : destinationAccount,
                        'transferType' : transferType
                        }
        # Specify the metadata options. These data will be sent to you in a notification when payment has been made
        metadata = {'shopId' : "1234",
                    'itemId' : "abcde"}
        try:
            response = gateway.mobilePaymentB2BRequest(productName, providerData, currencyCode, amount, metadata)
            print 'Encountered an error while sending: %s' % response['status']
            if (response['status'] == "Queued"):
                print 'transactionId=%s;transactionFee=%s;providerChannel=%s;' % (
                    response['transactionId'], recipient['transactionFee'], recipient['providerChannel'])
            else:
                print 'errorMessage: %s' % response['errorMessage']
        except AfricasTalkingGatewayException, e:
            print 'Received error response: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().b2b()
