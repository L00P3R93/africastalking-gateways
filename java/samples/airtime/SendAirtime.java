import org.json.*;
import java.util.HashMap;

public class SendAirtime {

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

        /* Specify the phone number/s and amount in json format
           Specify the country currency and the amount as shown below (+254 for Kenya in this case)
           Please ensure you include the country code for phone numbers (KES for Kenya in this case)
        
           e.g. [{"amount":"KES 100", "phoneNumber":+254711XXXYYY},{"amount":"KES 100", "phoneNumber":+254733YYYZZZ}]
       */
        String recipientStringFormat = "[{\"amount\":\"KES 100\", \"phoneNumber\":\"+254711XXXYYY\"},{\"amount\":\"KES 100\", \"phoneNumber\":\"+254733YYYZZZ\"}]";

        /* And send the airtime */

        try {
            JSONArray results = gateway.sendAirtime(recipientStringFormat);
            int length = results.length();
            for(int i = 0; i < length; i++) {
                JSONObject result = results.getJSONObject(i);
                System.out.println(result.getString("status"));
                System.out.println(result.getString("amount"));
                System.out.println(result.getString("phoneNumber"));
                System.out.println(result.getString("discount"));
                System.out.println(result.getString("requestId"));
                //Error message is important when the status is not Success
                System.out.println(result.getString("errorMessage"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}