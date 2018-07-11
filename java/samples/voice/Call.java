import org.json.*;
import java.util.HashMap;

public class Call {

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

        /* Specify your Africa's Talking phone number in international format */
        String from = "+254711082XXX";

        /* Specify the numbers that you want to call to in a comma-separated list
            Please ensure you include the country code (+254 for Kenya in this case) */
        String to   = "+254711XXXYYY,+254733YYYZZZ";

        /* And make the call */

        try {
            JSONArray results = gateway.call(from, to);
            int len = results.length();
            for(int i = 0; i < len; i++) {
                JSONObject result = results.getJSONObject(i);
                //Only status "Queued" means the call was successfully placed
                System.out.print(result.getString("status") + ",");
                System.out.print(result.getString("phoneNumber") + "\n");
            }
            // Our API will now contact your callback URL once the recipient answers the call!
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}