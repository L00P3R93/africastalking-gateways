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

    def transfer(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)
        recipient1 = {
            'bankAccount'  : { 'accountName'   : 'Femi Kuti',
                               'accountNumber' : '11100223456',
                               'bankCode'      : 234003
            },
            'currencyCode' : 'NGN',
            'amount'       : 100,
            'narration'    : 'May Salary',
            'metadata'     : { 'referenceId'  : '1235',
                               'officeBranch' : '201' }
        }
        recipient2 = {
            'bankAccount'  : { 'accountName'   : 'Fela Kuti',
                               'accountNumber' : '22200223456',
                               'bankCode'      : 234004
            },
            'currencyCode' : 'NGN',
            'amount'       : 50,
            'narration'    : 'May Salary',
            'metadata'     : { 'referenceId'  : '1236',
                               'officeBranch' : '201' }
        }
        recipients = [recipient1, recipient2]
        try:
            responses = gateway.bankPaymentTransfer(
                productName_  = 'Airtime Distribution',
                recipients_   = recipients
            )
            for response in responses:
                print "accountNumber=%s;status=%s;" % (response['accountNumber'],
                                                       response['status'])
                if response['status'] == 'Queued':
                    print "transactionId=%s;transactionFee=%s;" % (response['transactionId'],
                                                                   response['transactionFee'])
                else:
                    print "errorMessage=%s;" % response['errorMessage']
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while transfering: %s' % str(e)


if __name__ == '__main__':
    PAYMENTS().transfer()
