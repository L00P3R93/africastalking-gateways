<?php
// Sending premium rated messages
require_once('AfricasTalkingGateway.php');
$username   = "MyAppUsername";
$apikey     = "MyAppAPIKey";
$recipient = "+254711XXXYYY";
// Specify your premium shortCode and keyword
$shortCode = "XXXXX";
$keyword   = "premiumKeyword";
// Set the bulkSMSMode flag to 0 so that the subscriber gets charged
$bulkSMSMode = 0;
// Create an array which would hold the following parameters:
// keyword: Your premium keyword,
// retryDurationInHours: The numbers of hours our API should retry to send the message 
// incase it doesn't go through. It is optional
$options = array(
            'keyword'              => $keyword,
            'retryDurationInHours' => "No of hours to retry"
           );
           
$message = "Get your daily message and thats how we roll.";
$gateway    = new AfricasTalkingGateway($username, $apikey);
try 
{ 
  $responses = $gateway->sendMessage($recipient, $message, $shortCode, $bulkSMSMode, $options);
  foreach($responses as $response) {
    echo " Number: " .$response->number;
    echo " Status: " .$response->status;
    echo " StatusCode: " .$response->statusCode;
    echo " MessageId: " .$response->messageId . "\n";
  }
}
catch ( AfricasTalkingGatewayException $e )
{
  echo "Encountered an error while sending: ".$e->getMessage();
}
// DONE!!! 