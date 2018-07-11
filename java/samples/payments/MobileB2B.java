import org.json.*;
import java.util.*;

public class MobileB2B {

    public static void main(String[] args) {
        /* Set your credentials */
        String APP_USERNAME = "sandbox"; // Your app username, or "sandbox" if you are testing in sandbox
        String API_KEY = ""; // Your app or sandox api key

        /*************************************************************************************
            NOTE: If connecting to the sandbox:
            1. Use "sandbox" as the app username
            2. Use the apiKey generated from your sandbox application
                https://account.africastalking.com/apps/sandbox/settings/key
        **************************************************************************************/

        /* Create a gateway object */
        AfricasTalkingGateway gateway = new AfricasTalkingGateway(APP_USERNAME, API_KEY);

        // Specify your product name
        String productName = "ABC";
        
        // Specify the payment provider. eg. MPESA, ATHENA (AfricasTalking Sandbox), etc
        String provider = "ATHENA";
        
        // Specify partner's business channel
        String destinationChannel = "partnerBusinessChannel";
        String destinationAccount = "Accc";
        
        // Specify the transfer purpose
        String transferType = "BusinessToBusinessTransfer";
        
        HashMap<String, String> providerData = new HashMap<String, String>();
        providerData.put("provider", provider);
        providerData.put("destinationChannel", destinationChannel);
        providerData.put("destinationAccount", destinationAccount);
        providerData.put("transferType", transferType);
        
        // Specify 3-Letter ISO currency code and amount
        String currencyCode = "KES";
        float amount = 100;
        
        // Specify the metadata options. These data will be sent to you in a notification when payment has been made.
        //You can add as many parameters as you want
        
        HashMap<String, String> metadata = new HashMap<String, String>();
        metadata.put("shopId", "1234");
        metadata.put("itemId", "abcde");

        /* And initiate the B2B request */
        try {
            JSONObject results = gateway.mobilePaymentB2BRequest(productName, providerData,
            currencyCode, amount, metadata);
            
            System.out.println("Status: " + results.getString("status"));
            
            if(results.getString("status").equals("Queued")) {            
                System.out.println("TransactionId: " + results.getString("transactionId"));      
                System.out.println("TransactionFee: " + results.getString("transactionFee"));            
                System.out.println("ProviderChannel: " + results.getString("providerChannel"));            
            } else {
                System.out.println("ErrorMessage: " + results.getString("errorMessage"));            
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}