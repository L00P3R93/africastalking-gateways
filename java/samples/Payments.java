import org.json.*;
import java.util.*;

public class Payments {

    /* Set your credentials */
    static final String APP_USERNAME = "sandbox"; // Your app username, or "sandbox" if you are testing in sandbox
    static final String API_KEY = "32ae08f93abf6890029cdcb0d482920a9921ffabec95eba5221d43afe688851e"; // Your app or sandox api key

    /*************************************************************************************
        NOTE: If connecting to the sandbox:
        1. Use "sandbox" as the app username
        2. Use the apiKey generated from your sandbox application
            https://account.africastalking.com/apps/sandbox/settings/key
    **************************************************************************************/

    public static void mobileCheckout() {
        /* Create a gateway object */
        AfricasTalkingGateway gateway = new AfricasTalkingGateway(APP_USERNAME, API_KEY);

        // Specify the name of your Africa's Talking payment product
        String productName  = "ABC";
        // The phone number of the customer checking out
        String phoneNumber  = "+25471XXXXXX";
        // The 3-Letter ISO currency code for the checkout amount
        String currencyCode = "KES";
        // The checkout amount
        Double amount       = 100.50;
        // Any metadata that you would like to send along with this request
        // This metadata will be  included when we send back the final payment notification
        HashMap<String, String> metadata = new HashMap<String, String>();    
        metadata.put("agentId", "654");
        metadata.put("productId", "321");

        /* And initiate a checkout */
        try {
            JSONObject result = gateway.initiateMobilePaymentCheckout(productName, phoneNumber, currencyCode, amount, metadata);
            System.out.println(result.getString("status"));
            System.out.println(result.getString("description"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void mobileB2C() {
        /* Create a gateway object */
        AfricasTalkingGateway gateway = new AfricasTalkingGateway(APP_USERNAME, API_KEY);

        // Specify the name of your Africa's Talking payment product
        String productName  = "ABC";
        // The 3-Letter ISO currency code for the checkout amount
        String currencyCode = "KES";
        // Provide the details of a mobile money recipient
        MobilePaymentB2CRecipient recipient1 = new MobilePaymentB2CRecipient("+254718XXXYYY",
                                             "KES",
                                             10.50);
        recipient1.addMetadata("name", "Clerk");
        recipient1.addMetadata("reason", "May Salary");
        
        // You can provide up to 10 recipients at a time
        MobilePaymentB2CRecipient recipient2 = new MobilePaymentB2CRecipient("+254718YYYXXX",
                                             "KES",
                                             50.10);
        recipient2.addMetadata("name", "Accountant");
        recipient2.addMetadata("reason", "May Salary");
        // Put the recipients into an array
        List<MobilePaymentB2CRecipient> recipients  = new ArrayList<MobilePaymentB2CRecipient>();
        recipients.add(recipient1);
        recipients.add(recipient2);

        /* And initiate the B2C request */
        try {
            JSONArray responses = gateway.mobilePaymentB2CRequest(productName, recipients);
            for( int i = 0; i < responses.length(); ++i ) {
                // Parse the responses and print them out
                JSONObject response = responses.getJSONObject(i);
                System.out.print("phoneNumber=" + response.getString("phoneNumber"));
                String status = response.getString("status");
                System.out.print(";status=" + response.getString("status"));
                if ( status.equals("Queued") ) {
                    System.out.print(";transactionId=" + response.getString("transactionId"));
                    System.out.print(";provider=" + response.getString("provider"));
                    System.out.print(";providerChannel=" + response.getString("providerChannel"));
                    System.out.print(";value=" + response.getString("value"));
                    System.out.println(";transactionFee=" + response.getString("transactionFee"));
                } else {
                    System.out.println(";errorMessage=" + response.getString("errorMessage"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void mobileB2B() {
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

    public static void main(String[] args) {
        mobileCheckout();
        mobileB2C();
        mobileB2B();
        // bankTransfer();
        // bankCheckout();
        // bankCheckoutValidation();
        // cardCheckout();
        // cardCheckoutValidation();
    }
}