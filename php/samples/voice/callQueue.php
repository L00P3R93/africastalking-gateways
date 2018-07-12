<?php
// Save this code in callCenter.php. Configure the callback URL for BOTH phone numbers
// to point to the location of this script on the web
// e.g http://www.myawesomesite.com/callCenter.php

// Check to see whether this call is active
$isActive  = $_POST['isActive'];

if ($isActive == 1)  {
    // Check to see whether this is the enqueue or dequeue Africas Talking phone number    
    $destinationNumber =  $_POST['destinationNumber'];
    
    if ($destinationNumber == '+254711082XXX') {
        // Assuming this is the phone number you have advertised for people that want to
        // join the queue
       $response  = '<?xml version="1.0" encoding="UTF-8"?>';
       $response .= '<Response>';
       $response .= '<Enqueue url="http://www.mymediaserver.com/audio/callWaiting.wav"/>';
       $response .= '</Response>';
    } else {
       // This must be the phone number that people call to answer these calls. Dequeue
       // by specifying the phone number that adds people to the queue
       $response  = '<?xml version="1.0" encoding="UTF-8"?>';
       $response .= '<Response>';
       $response .= '<Dequeue phoneNumber="+254711082XXX"/>';
       $response .= '</Response>';
    }
         
      // Print the response onto the page so that our gateway can read it
      header('Content-type: text/plain');
      echo $response;

} else {
  
  // Read in call details (duration, cost). This flag is set once the call is completed.
  // In this example (enqueue and dequeue), this call will be made twice, when each caller
  // hangs up
  // Note that the gateway does not expect a properly formatted response

  $sessionId    = $_POST['sessionId']; 
  $duration     = $_POST['durationInSeconds'];
  $currencyCode = $_POST['currencyCode'];
  $amount       = $_POST['amount'];
  
  // You can then store this information in the database for your records

}
