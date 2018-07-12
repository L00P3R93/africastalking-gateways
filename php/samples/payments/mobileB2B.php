<?php
// Be sure to include the file you've just downloaded
require_once('AfricasTalkingGateway.php');
// Specify your login credentials
$username   = "MyAppUsername";
$apikey     = "MyAppAPIKey";
// Specify your product name
$productName = "myPaymentProductName";
// Specify the payment provider. eg. MPESA, ATHENA (AfricasTalking Sandbox), etc
$provider = "myPaymentProvider";
// Specify partner's business channel
$destinationChannel = "partnerBusinessChannel";
// Specify the transfer purpose
$transferType = "BusinessToBusinessTransfer";
$providerData = array('provider' => $provider,
                      'destinationChannel' => $destinationChannel,
                      'transferType' => $transferType);
// The 3-Letter ISO currency code for the checkout amount
$currencyCode = "KES";
$amount = 100;
// Specify the metadata options. These data will be sent to you in a notification when payment has been made
$metadata = array('shopId' => "1234",
                  'itemId' => "abcde");
// Create a new instance of our awesome gateway class
$gateway    = new AfricasTalkingGateway($username, $apikey);
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
  // Thats it, hit send and we'll take care of the rest. 
  $responses = $gateway->mobilePaymentB2BRequest($productName, $providerData, $currencyCode, $amount, $metadata);
  if($responses->status == "Queued") {
    echo "TransactionId: " . $responses->transactionId;
    echo "\nTransactionFee: " . $responses->transactionFee;
    echo "\nProviderChannel: " . $responses->providerChannel;
  }
  else {
    echo "ErrorMessage: " . $responses->errorMessage;
  }
}
catch ( AfricasTalkingGatewayException $e )
{
  echo "Encountered an error while sending: ".$e->getMessage();
}
?>
    