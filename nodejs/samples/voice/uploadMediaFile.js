var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function uploadMediaFile() {
    var locationUrl = 'http://onlineMediaUrl.com/file.wav';

    var post_data = queryString.stringify({
        'username' : username,
        'url'      : locationUrl,
    });

    var post_options = {
        host   : 'voice.africastalking.com',
        port   : 443,
        path   : '/mediaUpload',
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
                console.log('File uploaded!');
            } else {
                console.error(jsObject);
            }
        });
    });

    // Add post parameters to the http request
    post_req.write(post_data);
    post_req.end();
}

// Call the uploadMediaFile method
uploadMediaFile();

