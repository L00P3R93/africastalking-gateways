var queryString = require("querystring");
var https       = require("https");

// Your login credentials
var username = "MyAppsUsername";
var apiKey   = "MyAppsApiKey";

function sendMessage() {
    // Define the recipient numbers in a comma separated string
    // Numbers should be in international format as shown
    var to          = '+254711XXXYYY,+254733YYYZZZ';

    // And of course we want our recipients to know what we really do
    var message     = "I'm a lumberjack and its ok, I sleep all night and I work all day";

    // Define your shortCode or senderId
    // var from        = "shortCode or senderId";

    // This should always be 1 for bulk messages
    var bulkSMSMode = 1; 

    // The enqueue flag is used to queue messages incase you are sendng a high volume
    // The default value is 0.
    var enqueue     = 1;

    // BUild the post string from an object
    var post_data = queryString.stringify({
        'username'    : username,
        'to'          : to,
        'message'     : message,
        'bulkSMSMode' : bulkSMSMode,
        'enqueue'     : enqueue
    });

    var post_options = {
        host   : 'api.africastalking.com',
        port   : 443,
        path   : '/version1/messaging',
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
            var recipients = jsObject.SMSMessageData.Recipients;
            if (recipients.length > 0) {
                for (var i = 0; i < recipients.length; i += 1) {
                    var logStr = 'number= '       + recipients[i].number;
                    logStr    += '; cost= '       + recipients[i].cost;
                    logStr    += '; status= '     + recipients[i].status; // status is either "success" or "error message"
                    logStr    += '; statusCode= ' + recipients[i].statusCode;
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

// Call the sendMessage method
sendMessage();

