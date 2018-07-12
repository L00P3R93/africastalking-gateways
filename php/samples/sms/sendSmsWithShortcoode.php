<?php
//Sending Messages using sender id/short code
require_once('AfricasTalkingGateway.php');
$username   = "MyAppUsername";
$apiKey     = "MyAppAPIKey";
$recipients = "+254711XXXYYY,+254733YYYZZZ";
$message    = "I'm a lumberjack and its ok, I sleep all night and I work all day";
// Specify your AfricasTalking shortCode or sender id
$from = "shortCode or senderId";
$gateway    = new AfricasTalkingGateway($username, $apiKey);
try 
{
   
   $responses = $gateway->sendMessage($recipients, $message, $from);
            
  foreach($responses as $response) {
    echo " Number: " .$response->number;
    echo " Status: " .$response->status;
    echo " StatusCode: " .$response->statusCode;
    echo " MessageId: " .$response->messageId;
    echo " Cost: "   .$response->cost."\n";
  }
}
catch ( AfricasTalkingGatewayException $e )
{
  echo "Encountered an error while sending: ".$e->getMessage();
}
// DONE!!! 