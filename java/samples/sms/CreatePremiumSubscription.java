import org.json.*;
import java.util.HashMap;

public class CreatePremiumSubscription {

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

        // Specify the number that you want to subscribe
        // Please ensure you include the country code (+254 for Kenya in this case)
        // String phoneNumber   = "+254711XXXYYY";
        
        //Specify your Africa's Talking short code and keyword
        String shortCode = "XXXX";
        String keyword   = "MyAppKeyword";

        /* And create */

        try {

            // First the checkout token
            JSONObject result = gateway.createCheckoutToken(phoneNumber);

            result = gateway.createSubscription(phoneNumber, shortCode, keyword, result.getString("token"));
            //Only status Success signifies the subscription was successfully
            System.out.println(result.getString("status"));
            System.out.println(result.getString("description"));
        } catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
}