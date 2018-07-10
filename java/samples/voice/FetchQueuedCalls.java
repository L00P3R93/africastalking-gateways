import org.json.*;
import java.util.HashMap;

public class FetchQueuedCalls {

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

        /* And fetch the queue */

        try {
            JSONArray queuedCalls = gateway.getNumQueuedCalls(from); 
            // For a specific queue, specify the queue name eg:
            // String queueName = "myQueueName"
            // JSONArray queuedCalls = gateway.getNumQueuedCalls(phoneNumber, queueName);
            int length = queuedCalls.length();
            System.out.println("Queue Length: " + length);
            for(int i = 0; i < length; i++) {
                JSONObject result = queuedCalls.getJSONObject(i);
                System.out.println("Phone number: " + result.getString("phoneNumber"));
                System.out.println("Queue name: " + result.getString("queueName"));
                System.out.println("Number of queued calls: " + result.getString("numCalls"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}