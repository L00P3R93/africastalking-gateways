<?php
// Save this code in conferenceCall.php. Configure the callback URL for your phone number
// to point to the location of this script on the web
// e.g http://www.myawesomesite.com/conferenceCall.php

// First read a couple of the POST variables passed in with the request

// This is a unique ID generated for this call
$sessionId = $_POST['sessionId'];

// Check to see whether this call is active
$isActive  = $_POST['isActive'];

if ($isActive == 1)  {
  
  // Add the caller to the conference room
  
  // Compose the response  
  $response  = '<?xml version="1.0" encoding="UTF-8"?>';
  $response .= '<Response>';
  $response .= '<conference>';
  $response .= '</Response>';
       
  // Print the response onto the page so that our gateway can read it
  header('Content-type: text/plain');
  echo $response;

} else {
  
  // Read in call details (duration, cost). This flag is set once the call is completed.
  // Note that the gateway does not expect a response in this case
  
  $duration     = $_POST['durationInSeconds'];
  $currencyCode = $_POST['currencyCode'];
  $amount       = $_POST['amount'];

  // You can then store this information in the database for your records

}
