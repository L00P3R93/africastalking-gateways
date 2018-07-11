var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function getCheckoutToken(phoneNumber_) {
    return new Promise(function(resolve, reject) {
        var post_data = queryString.stringify({
            'phoneNumber': phoneNumber
        });

        var post_options = {
            host   : 'api.africastalking.com',
            port   : 443,
            path   : '/checkout/token/create',
            method : 'POST',

            rejectUnauthorized : false,
            requestCert        : true,
            agent              : false,

            headers: {
                'Content-Type'   : 'application/x-www-form-urlencoded',
                'Content-Length' : post_data.length,
                'Accept'         : 'application/json'
            }
        };

        var post_req = https.request(post_options, function(res) {
            let body = [];
            res.setEncoding('utf8');
            res
            .on('error', function(err) {
                reject(err);
            })
            .on('data', function(chunk) {
                body.push(chunk);
            })
            .on('end', function() {
                var jsObject = JSON.parse(body);
                resolve(jsObject);
            });
        });

        // Add post parameters to the http request
        post_req.write(post_data);
        post_req.end();
    });
}

function createSubscription(phoneNumber_, shortCode_, keyword_, checkoutToken_) {
    var post_data = queryString.stringify({
        'username'     : username,
        'phoneNumber'  : phoneNumber_,
        'shortCode'    : shortCode_,
        'keyword'      : keyword_,
        checkoutToken  : checkoutToken_
    });

    var post_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/subscription/create',
        method : 'POST',

        rejectUnauthorized : false,
        requestCert        : true,
        agent              : false,

        headers: {
            'Content-Type'   : 'application/x-www-form-urlencoded',
            'Content-Length' : post_data.length,
            'apiKey'         : apiKey,
            'Accept'         : 'application/json'
        }
    };

    var post_req = https.request(post_options, function(res) {
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
            if (res.statusCode === 201)  {
                var logStr = 'Status: '   + jsObject.status;
                logStr     = '; Description ' + jsObject.description;
                console.log(logStr);
            } else {
                console.log(jsObject);
            }
        });
    });

    post_req.write(post_data);
    post_req.end();
}

var phoneNumber = "+254711XXXYYY";
var shortCode   = "12345";
var keyword     = "myKeyword";

// Begin by getting a checkoutToken and
// then create the checkout subscription
getCheckoutToken(phoneNumber)
    .then(function(checkoutTokenRes) {
        if (checkoutTokenRes.description !== 'Success') {
            throw new Error(checkoutTokenRes.description);
        }

        var checkoutToken = checkoutTokenRes.token;
        createSubscription(phoneNumber, shortCode, keyword, checkoutToken);
    })
    .catch(function(err) {
        console.error(err);
    });

