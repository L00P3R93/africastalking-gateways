<?php
// First read a couple of the POST variables passed in with the request

// This is a unique ID generated for this call
$sessionId = $_POST['sessionId'];

// Check to see whether this call is active
$isActive  = $_POST['isActive'];

if ($isActive == 1)  {
	
	// Get the current state of the call. You may use a database or file to store call session data but we have use PHP sessions
	
	$currentState = getCallState($sessionId);
	
	if($currentState == "") {
			//This is the first time the callback has been accessed and we want to prompt the user 
		
			// Compose the response  
			$response  = '<?xml version="1.0" encoding="UTF-8"?>';
			$response .= '<Response>';
			$response .= '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true"/>';
			$response .= '<Say>Please say your name after the beep.</Say>';
			$response .= '</Record>';
			$response .= '</Response>';
			
			// set currentState to PromptName
			saveCurrentCallState($sessionId, "PromptName");
	}
	
	elseif($currentState == "PromptName") {
		  $recordedName = $_POST['recordingUrl'];
			
			//Persist the recordedName in your storage. Its an MP3 file
			
			//Thank the user for leaving their name
			$response  = '<?xml version="1.0" encoding="UTF-8"?>';
			$response .= '<Response>';
			$response .= '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true"/>';
			$response .= '<Say>Please say your location after the beep.</Say>';
			$response .= '</Record>';
			$response .= '</Response>';
			
			saveCurrentCallState($sessionId, "PromptLocation");
	}
	
	
	elseif($currentState == "PromptLocation") {
		  $recordedLocation = $_POST['recordingUrl'];
			
			//Persist the recordedLocation in your storage. Its an MP3 file
			
			//Thank the user for leaving their name
			$response  = '<?xml version="1.0" encoding="UTF-8"?>';
			$response .= '<Response>';
			$response .= '<Say>Thank you for the information. Our pizza delivery guy is on the way.</Say>';
			$response .= '</Response>';
	}
					 
				// Print the response onto the page so that our gateway can read it
	header('Content-type: application/xml');
	echo $response;

} else {
	
	// Read in call details (duration, cost). This flag is set once the call is completed.
	// Note that the gateway does not expect a response in thie case
	
	$duration     = $_POST['durationInSeconds'];
	$currencyCode = $_POST['currencyCode'];
	$amount       = $_POST['amount'];
}
