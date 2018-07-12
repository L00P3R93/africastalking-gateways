var queryString  = require("querystring");
var https        = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function fetchMessages(lastReceivedId_) {
    // Build the post string from an object
    var get_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/messaging?username=' + username + '&lastReceivedId=' + lastReceivedId_,
        method : 'GET',

        rejectUnauthorized : false,
        requestCert        : true,
        agent              : false,

        headers: {
            'Accept': 'application/json',
            'apiKey': apiKey
        }
    };

    var get_req = https.request(get_options, function(res) {
        let body = [];
        res.setEncoding('utf8');
        res
        .on('error', function(err) {
            console.error(err);
        })
        .on('data', function(chunk) {
            body.push(chunk);
        })
        .on('end', function() {
            var jsObject = JSON.parse(body);
            var messages = jsObject.SMSMessageData.Messages;
            if (messages.length > 0) {
                for (var i = 0; i < messages.length; i += 1) {
                    var logStr = 'from= '   + messages[i].from;
                    logStr += '; to= '      + messages[i].to;
                    logStr += '; message= ' + messages[i].text;
                    logStr += '; linkId= '  + messages[i].linkId;
                    logStr += '; date= '    + messages[i].date;
                    logStr += '; id= '      + messages[i].id;
                    console.log(logStr);

                    lastReceivedId_ = messages[i].id;
                }

                // Recursively fetch messages
                fetchMessages(lastReceivedId_);
            }
        });
    });

    get_req.end();
    console.log('lastReceivedId: ' + lastReceivedId_);
}

// Call the fetchMessages method with lastReceivedId 
var lastReceivedId = 0;
fetchMessages(lastReceivedId);

