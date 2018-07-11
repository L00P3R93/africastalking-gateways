var https = require('https');

// Your login credentials
var username  = "MyAppsUsername";
var apiKey    = "MyAppsApiKey";

// Your premium product
var shortCode = "12345";
var keyword   = "MyAppsKeyword";

function fetchPremiumSubscriptions(lastReceivedId_) {
    // Build the post string from an object
    var get_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/subscription?username=' + username + '&shortCode=' + shortCode + '&keyword=' + keyword + '&lastReceivedId=' + lastReceivedId_,
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
            if (res.statusCode === 200) {
                var subscriptions = jsObject.responses;
                if (subscriptions.length > 0) {
                    for (var i = 0; i < subscriptions.length; i += 1) {
                        var logStr = 'phoneNumber= ' + subscriptions[i].phoneNumber;
                        logStr    += '; id= '        + subscriptions[i].id;
                        console.log(logStr);

                        lastReceivedId_ = subscriptions[i].id;
                    }

                    // fetch subscriptions recursively
                    fetchPremiumSubscriptions(lastReceivedId_);
                }
            } else {
                console.log(jsObject);
            }
        });
    });

    get_req.end();
    console.log('lastReceivedId: ' + lastReceivedId_);
}

// Call the fetchPremiumSubscriptions method with lastReceivedId
var lastReceivedId = 0;
fetchPremiumSubscriptions(lastReceivedId);

