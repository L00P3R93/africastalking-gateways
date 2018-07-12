<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials

$username   = "MyAppUsername";
$apiKey     = "MyAppAPIKey";
//Create an instance of our awesome gateway class and pass your credentials
$gateway = new AfricasTalkingGateway($username, $apiKey);
// NOTE: If connecting to the sandbox, please add the sandbox flag to the constructor:
// $gateway = new AfricasTalkingGateway($username, $apiKey, "sandbox");
// Provide the transacitonId that was returned by the charge request
$transactionId = "ATPid_7444b64859882dca9ee9621276fc7c7f";
// Provide the OTP that the bank sent to the owner of the bank account
$otp           = "1234";
try {
  // Initiate the checkout. If successful, you will get back a transactionId
  $gateway->bankPaymentCheckoutValidation($transactionId,
                      $otp);
  echo "The transaction was completed successfully";
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
    
    