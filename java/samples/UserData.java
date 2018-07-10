import org.json.*;
import java.util.HashMap;

public class UserData {

    /* Set your credentials */
    static final String APP_USERNAME = "sandbox"; // Your app username, or "sandbox" if you are testing in sandbox
    static final String API_KEY = ""; // Your app or sandox api key

    /*************************************************************************************
        NOTE: If connecting to the sandbox:
        1. Use "sandbox" as the app username
        2. Use the apiKey generated from your sandbox application
            https://account.africastalking.com/apps/sandbox/settings/key
    **************************************************************************************/

    public static void fetchData() {
        /* Create a gateway object */
        AfricasTalkingGateway gateway = new AfricasTalkingGateway(APP_USERNAME, API_KEY);

        /* And fetch the balance */

        try {
            JSONObject result = gateway.getUserData();
            System.out.println(result.getString("balance"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        fetchData();
    }
}