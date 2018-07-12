import org.json.*;
import java.util.HashMap;

public class FetchSubscriptions {

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

        // Specify your premium shortcode and keyword
        String shortCode = "XXXXX";
        String keyword   = "myPremiumKeyword";

        // Our gateway will return 10 messages at a time back to you, starting with
        // what you currently believe is the lastReceivedId. Specify 0 for the first
        // time you access the gateway, and the ID of the last message we sent you
        // on subsequent results
        int lastReceivedId = 0;

        /* And fetch the messages */

        try {
            JSONArray results = null;
            do {
                results = gateway.fetchPremiumSubscriptions(shortCode, keyword, lastReceivedId);
                for(int i = 0; i < results.length(); ++ i) {
                    JSONObject result = results.getJSONObject(i);
                    System.out.println(result.getString("phoneNumber"));
                    lastReceivedId = result.getInt("id");
                }
            } while ( results.length() > 0 );
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}