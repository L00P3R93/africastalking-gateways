# Gateway supports python 2 and not 3.
import os, sys
# Add parent directory to script path so as to import gateway
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class VOICE:
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

    def upload_media_file(self):
        gateway = AfricasTalkingGateway(self.APP_USERNAME, self.API_KEY)

        # Specify the url of the file to be uploaded
        fileUrl = "http://onlineMediaUrl.com/file.wav";

        try:
            # Upload the file
            gateway.upladMediaFile(fileUrl)
            print "File upload initiated. Time for song and dance!\n";
        except AfricasTalkingGatewayException, e:
            print 'Encountered an error while uploading the file: %s' % str(e)

if __name__ == '__main__':
    VOICE().upload_media_file();
