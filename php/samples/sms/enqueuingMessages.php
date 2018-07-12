<?php
//Message queueing 
require_once('AfricasTalkingGateway.php');
$username   = "MyAppUsername";
$apikey     = "MyAppAPIKey";
$recipients = "+254711XXXYYY,+254733YYYZZZ";
$message    = "I'm a lumberjack and its ok, I sleep all night and I work all day";
$from = 34532; //$from = "shortCode or senderId";
$bulkSMSMode = 1; // This should always be 1 for bulk messages
// enqueue flag is used to queue messages incase you are sending a high volume.
// The default value is 0.
$options = array("enqueue" => 1);
$gateway    = new AfricasTalkingGateway($username, $apikey);
try 
{
   
   $responses = $gateway->sendMessage($recipients, $message, $from, $bulkSMSMode, $options);
            
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