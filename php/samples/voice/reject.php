<?php
// Save this code in handleCalls.php. Configure the callback URL for your phone number
// to point to the location of this script on the web
// e.g http://www.myawesomesite.com/handleCalls.php

// First read a couple of the POST variables passed in with the request

// This is a unique ID generated for this call
$sessionId = $_POST['sessionId'];

// Check to see whether this call is active
$isActive  = $_POST['isActive'];

// Here is our black-listed numbers
$blackListArr = array('+254711XYZXYZ');

if ($isActive == 1)  {
  // Check whether this is the caller that has been giving you
  // sleepless nights
  $callerNumber = $_POST['callerNumber'];
  if ( in_array($callerNumber, $blackListArr) ) {
    // Compose the rejection response  
    $response  = '<?xml version="1.0" encoding="UTF-8"?>';
    $response .= '<Response>';
    $response .= '<Reject/>';
    $response .= '</Response>';
  } else {    
    // Your regular application logic goes here
    $response  = '<?xml version="1.0" encoding="UTF-8"?>';
    $response .= '<Response>';
    $response .= '<Say>Hello world</Say>';
    $response .= '</Response>';    
  }
     
  // Print the response onto the page so that our gateway can read it
  header('Content-type: text/plain');
  echo $response;

} else {
  
  // Read in call details (duration, cost). This flag is set once the call is completed.
  // Note that the gateway does not expect a response in thie case
  
  $duration     = $_POST['durationInSeconds'];
  $currencyCode = $_POST['currencyCode'];
  $amount       = $_POST['amount'];
  
  // You can then store this information in the database for your records

}