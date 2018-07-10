import org.json.*;
import java.util.HashMap;

public class USSD {

    public static void handleUSSD() {
        /*
            When AT POSTs to your callback, respond with text/plain starting with
            either CON or END.
            USSD is session driven. Every request we send you will contain a sessionId,
            and this will be maintained until that session is completed
            You will need to let the Mobile Service Provider know whether the session is complete or not.
            If the session is ongoing, please begin your response with CON. If this is the last response for
            that session, begin your response with END. If we get a HTTP error response (Code 40X) from your script,
            or a malformed response (does not begin with CON or END, we will terminate the USSD session gracefully.
            e.g. 
            CON What would you like to do?\n1. Check My Account\n2. Quit
        */
    }


    public static void main(String[] args) {
        handleUSSD();
    }
}