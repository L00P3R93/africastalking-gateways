<?php
// Save this code in checkBalance.php. Configure the callback URL for your phone number
// to point to the location of this script on the web
// e.g http://www.myawesomesite.com/checkBalance.php
// First read in a couple of POST variables passed in with the request
// This is a unique ID generated for this call
$sessionId = $_POST['sessionId'];
// Check to see whether this call is active
$isActive  = $_POST['isActive'];
// For this example, we will assume that you persist the call state in 
// a database table, or in the current session. This function will
// retrieve that. For this example, the state goes from:
// None => PromptSent => Done
$currentCallState = getCallState($sessionId); // Implement this locally!
if ($isActive == 1)  {
  // The call is active
  
  if ($currentCallState == 'None') {
    
    // This is the First request we are receiving. Prompt for the account number
    // Compose the response
    $response  = '<?xml version="1.0" encoding="UTF-8"?>';
    $response .= '<Response>';
    $response .= '<GetDigits finishOnKey="#">';
    $response .= '<Say>Please enter your account number followed by the hash sign</Say>';
    $response .= '</GetDigits>';
    $response .= '</Response>';
    
    // Be sure to change the call state
    $currentCallState = 'PromptSent'
    
  } else if ($currentCallState == 'PromptSent' ){
    
    // This is the second request from Africa's Talking
    
    // You can replace this array with an actual database table
    $balanceArr = array(
            '1234' => 100,
            '1235' => 150,
            '1236' => 190,
            );
    // Read the dtmf digits
    $accountNumber = $_POST['dtmfDigits'];
    
    // Read the account information from the database if necessary
    if ( array_key_exists($accountNumber, $balanceArr) ) {
      $balance = $balanceArr[$accountNumber];
      $text    = "Your balance is " . $balance . " shillings. Good bye.";
    } else {
      $text = "Sorry, we could not find that account number. Good bye";
    }
    
    // Compose the response
    $response  = '<?xml version="1.0" encoding="UTF-8"?>';
    $response .= '<Response>';
    $response .= '<Say>'.$text.'</Say>';
    $response .= '</Response>';
    
    // Be sure to change the call state
    $currentCallState = 'Done'
    
  }
  
  // Ensure you save the call state. This could be a database call or a write to 
  // session storage
  saveCurrentCallState($sessionId, $currentCallState); // Implement this locally!
  
  // Print the response onto the page so that our gateway can read it
  header('Content-type: text/plain');
  echo $response;
} else {
  
  // Read in call details (duration, cost). This flag is set once the call is completed.
  // Note that the gateway does not expect a response in thie case
  
  $callerNumber = $_POST['callerNumber'];
  $duration     = $_POST['durationInSeconds'];
  $currencyCode = $_POST['currencyCode'];
  $amount       = $_POST['amount'];
  
  // You can then store this information in the database for your records
}