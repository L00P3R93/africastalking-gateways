<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials
$username   = "MyAppUsername";
$apiKey     = "MyAppAPIKey";
        
//Create an instance of our awesome gateway class and pass your credentials
$gateway = new AfricasTalkingGateway($username, $apiKey);
// NOTE: If connecting to the sandbox, please add the sandbox flag to the constructor:
// $gateway = new AfricasTalkingGateway($username, $apiKey, "sandbox");
// Specify the name of your Africa's Talking payment product
$productName  = "Airtime Distribution";
// Specify the bank account of the customer checking out.
$bankAccount  = array(
              "accountName"   => "Fela Kuti",
              "accountNumber" => "1234567890",
              "bankCode"      => 234004
              );
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
  $transactionId = $gateway->bankPaymentCheckoutCharge($productName,
                               $bankAccount,
                               $currencyCode,
                               $amount,
                               $narration,
                               $metadata);
  echo "The transactionId is: ".$transactionId;
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
