var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function fetchQueuedCalls() {
    // Specify your AfricasTalking phone number in the international format
    // Comma separate the  numbers if they are more than one
    var phoneNumber = '+254711082XXX';

    // queueName is an optional parameter
    var queueName = 'myQueueName';

    var post_data = queryString.stringify({
        'username'    : username,
        'phoneNumber' : phoneNumber,
        'queueName'   : queueName,
    });

    var post_options = {
        host   : 'voice.africastalking.com',
        port   : 443,
        path   : '/queueStatus',
        method : 'POST',

        rejectUnauthorized : false,
        requestCert        : true,
        agent              : false,

        headers: {
            'Content-Type'   : 'application/x-www-form-urlencoded',
            'Content-Length' : post_data.length,
            'Accept'         : 'application/json',
            'apiKey'         : apiKey
        }
    };

    var post_req = https.request(post_options, function(res) {
        let body = [];
        res.setEncoding('utf8');
        res
        .on('error', (err) => {
            console.error(err);
        })
        .on('data', function(chunk) {
            body.push(chunk);
        })
        .on('end', function() {
            var jsObject = JSON.parse(body);
            if (jsObject.errorMessage === 'None') {
                var entries = jsObject.entries;
                for (var i = 0; i < enries.length; i += 1) {
                    var logStr = 'phoneNumber= '  + entries[i].phoneNumber;
                    logStr    += 'queueName= '    + entries[i].queueName;
                    logStr    += 'numCalls= '     + entries[i].numCalls;
                    console.log(logStr);
                }
            } else {
                console.error(jsObject);
            }
        });
    });

    // Add post parameters to the http request
    post_req.write(post_data);
    post_req.end();
}

// Call the fetchQueuedCalls method
fetchQueuedCalls();

