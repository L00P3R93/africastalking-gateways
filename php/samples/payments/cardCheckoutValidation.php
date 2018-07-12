<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials
$username = "my-apps-username";
$apiKey   = "my-apps-apikey";
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
// Provide the transactionId that was returned by the charge request
$transactionId = "ATPid_e092c250f2bd1bcd6938b05633ba1c13";
// Provide the OTP that the bank sent to the owner of the bank account
$otp           = "1234";
try {
  // Initiate the checkout. If successful, you will get back a checkoutToken
  $checkoutToken = $gateway->cardPaymentCheckoutValidation($transactionId,
                                              $otp);
  echo "The checkout token for future transactions is ".$checkoutToken;
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
    