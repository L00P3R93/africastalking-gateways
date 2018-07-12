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
// Specify the name of your Africa's Talking payment product
$productName  = "Airtime Distribution";
// Specify a checkout token that you have previously received
$checkoutToken = "ATCdTkn_f6ee319bc9c9b5c8e468dfbe3d903094";
// The 3-Letter ISO currency code for the checkout amount
$currencyCode = "NGN";
// The checkout amount
$amount       = 100;
// A narration describing the transaction on the user's bank statement
$narration    = "Payment for Airtime";
// Any metadata that you would like to send along with this request
// This metadata will be  included when we send back the final payment notification
$metadata     = array(
              "requestId" => "MyRequestId1",
              "productId" => "321"
              );
try {
  // Initiate the checkout. If successful, you will get back a transactionId
  // that you can then use to validate the OTP that is sent to the user
  $transactionId = $gateway->cardPaymentCheckoutChargeWithToken($productName,
                                $checkoutToken,
                                $currencyCode,
                                $amount,
                                $narration,
                                $metadata);
  echo "The transactionId is: ".$transactionId;
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
