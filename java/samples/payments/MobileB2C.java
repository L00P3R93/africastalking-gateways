import org.json.*;
import java.util.*;

public class MobileB2C {

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
}