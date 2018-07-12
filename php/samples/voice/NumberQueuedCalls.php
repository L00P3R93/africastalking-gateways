<?php
// Be sure to include our gateway class
require_once('AfricasTalkingGateway.php');
// Specify your login credentials
$username   = "MyApp_Username";
$apikey     = "MyApp_APIKey";
// Specify your Africa's Talking phone number in international format
// Comma separate them if they are more than one
$phoneNumber = "+254711082XXX";
// Create a new instance of our awesome gateway class
$gateway = new AfricasTalkingGateway($username, $apikey);
/*************************************************************************************
  NOTE: If connecting to the sandbox:
  1. Use "sandbox" as the username
  2. Use the apiKey generated from your sandbox application
     https://account.africastalking.com/apps/sandbox/settings/key
  3. Add the "sandbox" flag to the constructor
  $gateway  = new AfricasTalkingGateway($username, $apiKey, "sandbox");
**************************************************************************************/
// Any gateway errors will be captured by our custom Exception class below, 
// so wrap the call in a try-catch block
try 
{
  $responses = $gateway->getNumQueuedCalls($phoneNumber);
  
  // For a specific queue, specify the queue name eg:
  // $queueName = "myQueueName"
  // $results = $gateway->getNumQueuedCalls($phoneNumber, $queueName);
  
  foreach($responses as $response) {
   echo "Phone number: " . $response->phoneNumber . "; ";
   echo "Queue name: " . $response->queueName . "; ";
   echo "Number of queued calls: " . $response->numCalls . "<br/>";
  }
}
catch ( AfricasTalkingGatewayException $e )
{
  echo "Encountered an error while making the call: ".$e->getMessage();
}
