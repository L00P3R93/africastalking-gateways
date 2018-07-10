import org.json.*;
import java.util.*;

public class MobileCheckout {

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
}