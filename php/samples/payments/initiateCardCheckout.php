<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials
//$username = "my-apps-username";
//$apikey   = "my-apps-apikey";
$username   = "sandbox";
$apiKey     = "381b193ffb3f8cc334dd938b49f136d6702efdb6a9d21ce7510cc469612ae02e";
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
// Specify the payment card values of the customer checking out.
$paymentCard  = array(
              "number"      => "123456789012345",
              "countryCode" => "NG",
              "cvvNumber"   => 123,
              "expiryMonth" => 9,
              "expiryYear"  => 2019,
              "authToken"   => "1234");
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
  $transactionId = $gateway->cardPaymentCheckoutCharge($productName,
                               $paymentCard,
                               $currencyCode,
                               $amount,
                               $narration,
                               $metadata);
  echo "The transactionId is: ".$transactionId;
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
