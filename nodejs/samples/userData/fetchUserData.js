var https    = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function fetchUserData(lastReceivedId_) {
    // Build the post string from an object
    var get_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/user?username=' + username,
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
            if (res.statusCode === 200) {
                var userData = jsObject.userDate;
                var logStr   = 'Balance : ' + jsObject.balance;
                console.log(logStr);
            } else {
                console.error(jsObject);
            }
        });
    });

    get_req.end();
}

// Call the fetchUserData method
fetchUserData();

