<?php
// Sending onDemand premium messages
require_once('AfricasTalkingGateway.php');
$username   = "MyAppUsername";
$apikey     = "MyAppAPIKey";
$recipient = "+254711XXXYYY";
$shortCode = "XXXXX";
$keyword   = "premiumKeyword"; // $keyword = null;
$bulkSMSMode = 0;
// Create an array which would hold parameters keyword, retryDurationInHours and linkId
// linkId is received from the message sent by subscriber to your onDemand service
$linkId = "messageLinkId";
$options = array(
            'keyword'             => $keyword,
            'linkId'              => $linkId,
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