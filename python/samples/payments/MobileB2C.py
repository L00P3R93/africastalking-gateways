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

    def b2c(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify the name of your Africa's Talking payment product
        productName = "ABC"
        # The 3-Letter ISO currency code for the checkout amount
        currencyCode = "KES"
        # Provide the details of a mobile money recipient
        recipient1   = {"phoneNumber"  : "+254714556407",
                        "currencyCode" : "KES",
                        "amount"       : 10.50,
                        "metadata"     : {"name"   : "Clerk",
                                          "reason" : "May Salary"}}
        # You can provide up to 10 recipients at a time
        recipient2   = {"phoneNumber"  : "+254711YYYXXX",
                        "currencyCode" : "KES",
                        "amount"       : 50.10,
                        "metadata"     : {"name"   : "Accountant",
                                          "reason" : "May Salary"}}

        # Put the recipients into an array
        recipients  = [recipient1, recipient2]
        try:
            responses = gateway.mobilePaymentB2CRequest(productName, recipients)
            for response in responses:
                # Parse the responses and print them out
                print "phoneNumber=%s;status=%s;" % (response['phoneNumber'],
                                                     response['status'])

                if response['status'] == 'Queued':
                    print "transactionId = %s; provider = %s; providerChannel = %s;" % (
                        response['transactionId'], response['provider'], response['providerChannel'])
                    print "value = %s; transactionFee = %s;" % (
                        response['value'], response['transactionFee'])
                else:
                    print "errorMessage=%s;" % response['errorMessage']
        except AfricasTalkingGatewayException, e:
            print 'Received error response: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().b2c()
