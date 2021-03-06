var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function makeCall() {
    var from = '+254711082XXX';
    var to   = '+254711XXXYYY, +254733YYYXXX';

    var post_data = queryString.stringify({
        'username' : username,
        'from'     : from,
        'to'       : to,
    });

    var post_options = {
        host   : 'voice.africastalking.com',
        port   : 443,
        path   : '/call',
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
            if (jsObject.errorMessage === "None") {
                var entries = jsObject.entries;
                for (var i = 0; i < enries.length; i += 1) {
                    var logStr = 'Status= '      + entries[i].status;
                    logStr    += 'phoneNumber= ' + entries[i].phoneNumber;
                    console.log(logStr);

                    // Our API will now contact your callback URL once recipient answers the call!
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

// Call the call method
makeCall();

