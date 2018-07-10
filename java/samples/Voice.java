import org.json.*;
import java.util.HashMap;

public class Voice {

    /* Set your credentials */
    static final String APP_USERNAME = "sandbox"; // Your app username, or "sandbox" if you are testing in sandbox
    static final String API_KEY = ""; // Your app or sandox api key

    /*************************************************************************************
        NOTE: If connecting to the sandbox:
        1. Use "sandbox" as the app username
        2. Use the apiKey generated from your sandbox application
            https://account.africastalking.com/apps/sandbox/settings/key
    **************************************************************************************/

    public static void call() {
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

    public static void handleCall() {
        /*
            When AT POSTs to your callback, respond with xml
            e.g. 
            <Response>
                <Say voice="man" playBeep="false" >Your balance is 1234 Shillings</Say>
            </Response>
        */
    }

    public static void fetchQueuedCalls() {
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

    public static void uploadMediaFile() {
        /* Create a gateway object */
        AfricasTalkingGateway gateway = new AfricasTalkingGateway(APP_USERNAME, API_KEY);

        /* Specify your Africa's Talking phone number in international format */
        String from = "+254711082XXX";

        /* Specify the url of the file to be uploaded */
        String url = "http://onlineMediaUrl.com/file.wav";

        /* And upload the file  */

        try {
            gateway.uploadMediaFile(url, from);
            System.out.println("File upload initiated. Time for song and dance!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        call();
        handleCall();
        fetchQueuedCalls();
        uploadMediaFile();
    }
}