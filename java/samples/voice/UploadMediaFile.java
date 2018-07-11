import org.json.*;
import java.util.HashMap;

public class UploadMediaFile {


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
}