<?php
require_once "AfricasTalkingGateway.php";
//Specify your credentials
$username   = "MyAppUsername";
$apiKey     = "MyAppAPIKey";

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
// Specify bank accounts of recipients of the money
$recipient1   = array("bankAccount" => array("accountName"   => "Fela Kuti",
                         "accountNumber" => "1234567890",
                         "bankCode"      => 234004),
              "currencyCode" => "NGN",
              "amount"       => "101",
              "narration"    => "May Salary",
              "metadata"     => array("referenceId"  => "1235",
                          "officeBranch" => "201")
              );
$recipient2   = array("bankAccount" => array("accountName"   => "Femi Kuti",
                         "accountNumber" => "234567891",
                         "bankCode"      => 234003),
              "currencyCode" => "NGN",
              "amount"       => "110",
              "narration"    => "May Salary",
              "metadata"     => array("referenceId"  => "1236",
                          "officeBranch" => "205")
              );
// Put the recipients into a list
$recipients = array($recipient1, $recipient2);
try {
  // Initiate the transfer. If successful, you will get back a list of responses
  $responses = $gateway->bankPaymentTransfer($productName,
                         $recipients);
  
  foreach($responses as $response) {
    // Parse the responses and print them out
    print_r($response);
    echo "accountNumber=".$response->accountNumber;
    echo ";status=".$response->status;
    if ($response->status == "Queued") {
      echo ";transactionId=".$response->transactionId;
      echo ";transactionFee=".$response->transactionFee."\n";
    } else {
      echo ";errorMessage=".$response->errorMessage."\n";
    }
  }  
}
catch(AfricasTalkingGatewayException $e){
  echo "Received error response: ".$e->getMessage();
}
    