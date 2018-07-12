<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials
$username = "MyAppUsername";
$apiKey   = "MyAppApiKey";
//Create an instance of our awesome gateway class and pass your credentials
$gateway = new AfricasTalkingGateway($username, $apiKey);
/*************************************************************************************
 NOTE: If connecting to the sandbox:
 1. Use "sandbox" as the username
 2. Use the apiKey generated from your sandbox application
    https://account.africastalking.com/apps/sandbox/settings/key
 3. Add the "sandbox" flag to the constructor
 $gateway  = new AfricasTalkingGateway($username, $apiKey, "sandbox");
**************************************************************************************/
// Specify the name of your Africa's Talking payment product
$productName  = "My Online Store";
// The 3-Letter ISO currency code for the checkout amount
$currencyCode = "KES";
// Provide the details of a mobile money recipient
$recipient1   = array("phoneNumber" => "+254711XXXYYY",
                       "currencyCode" => "KES",
                       "amount"       => 10.50,
                       "metadata"     => array("name"   => "Clerk",
                                               "reason" => "May Salary")
              );
// You can provide up to 10 recipients at a time
$recipient2   = array("phoneNumber"  => "+254711YYYXXX",
                    "currencyCode" => "KES",
                    "amount"       => 50.10,
                    "metadata"     => array("name"   => "Accountant",
                                            "reason" => "May Salary")
              );
// Put the recipients into an array
$recipients  = array($recipient1, $recipient2);
try {
  $responses = $gateway->mobilePaymentB2CRequest($productName, $recipients);
  
  foreach($responses as $response) {
    // Parse the responses and print them out
    echo "phoneNumber=".$response->phoneNumber;
    echo ";status=".$response->status;
    
    if ($response->status == "Queued") {
      echo ";transactionId=".$response->transactionId;
      echo ";provider=".$response->provider;
      echo ";providerChannel=".$response->providerChannel;
      echo ";value=".$response->value;
      echo ";transactionFee=".$response->transactionFee."\n";
    } else {
      echo ";errorMessage=".$response->errorMessage."\n";
    }
  }
  
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
?>
