<?php
// Be sure to include our gateway class
require_once('AfricasTalkingGateway.php');
// Specify your login credentials
$username   = "MyApp_Username";
$apikey     = "MyApp_APIKey";
// Specify your the url of file to be uploaded
$file_url = "http://onlineMediaUrl.com/file.wav";
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
  $gateway->uploadMediaFile($file_url);
  echo "File upload initiated. Time for song and dance!\n";
  
}
catch ( AfricasTalkingGatewayException $e )
{
  echo "Encountered an error while uploading file: ".$e->getMessage();
}
// DONE!!! 