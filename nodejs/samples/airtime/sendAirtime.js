var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function sendAirtime() {
    // Specify an array to hold airtime recipients and amounts
    // Please ensure you include the country code for phone numbers (+254 for Kenya in this case)
    // Please ensure you include the country code for phone numbers (KES for Kenya in this case)
    var recipients = [{
        phoneNUmber : '+254711XXXYYY',
        amount      : 'KES XXX',
    }, {
        phoneNUmber : '+254733XXXYYY',
        amount      : 'KES YYY',
    }];

    var recipients_string = JSON.stringify(recipients);

    var post_data = queryString.stringify({
        'username'   : username,
        'recipients' : recipients_string,
    });

    var post_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/airtime/send',
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
        res.on('error', function(err) {
            console.error(err);
        })
        .on('data', function(chunk) {
            body.push(chunk);
        })
        .on('end', function() {
            var jsObject = JSON.parse(body);
            if (res.statusCode === 201) {
                var recipients = jsObject.responses; 
                for (var i = 0; i < recipients.length; i += 1) {
                    var logStr = 'Status= '         + recipients[i].status;
                    logStr    += '; phoneNUmber= '  + recipients[i].phoneNUmber;
                    logStr    += '; amount= '       + recipients[i].amount;
                    logStr    += '; cost= '         + recipients[i].cost;
                    logsStr   += '; discount= '     + recipients[i].discount;
                    logStr    += '; errorMessage= ' + recipients[i].errorMessage;
                    console.log(logStr);
                }
            } else {
                console.error(jsObject);
            }
        });
    });

    post_req.write(post_data);
    post_req.end();
}

// Call the sendAirtime method
sendAirtime();

