import org.json.*;
import java.util.HashMap;

public class SendPremiumSubscription {

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

        /* Specify the numbers that you want to send to in a comma-separated list
            Please ensure you include the country code (+254 for Kenya in this case) */
        String recipients = "+254718769882,+254733YYYZZZ";

        /* Set the message to be sent */
        String message = "Hello, this is a test";

        /* Specify your shortcode */
        String from = "223344";
        
        /* Set your keyword */
        String keyword = "ABC";

        int bulkSMSMode = 0;
        // Create a hashmap which would hold the following parameters:
        // keyword: Your premium keyword,
        // retryDurationInHours: The numbers of hours our API should retry to send the message 
        // incase it doesn't go through. It is optional
        HashMap<String, String> options = new HashMap<String, String>();
        options.put("keyword", keyword);
        options.put("retryDurationInHours", "1");

        /* And send the SMS */

        try {
            JSONArray results = gateway.sendMessage(recipients, message, from, bulkSMSMode, options);
            for( int i = 0; i < results.length(); ++i ) {
                JSONObject result = results.getJSONObject(i);
                System.out.print(result.getString("status") + ","); // status is either "Success" or "error message"
                // System.out.print(result.getString("statusCode") + ",");
                System.out.print(result.getString("number") + ",");
                System.out.print(result.getString("messageId") + ",");
                System.out.println(result.getString("cost"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}